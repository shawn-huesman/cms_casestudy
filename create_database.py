import requests
import pandas as pd
import numpy as np
import datetime
import os
import django

from TqdmReader import TqdmReader


def run():
    open_payments_data_url = r"https://openpaymentsdata.cms.gov/api/1/metastore/schemas/dataset/items?show-reference-ids=false"
    general_payment_urls = get_general_payment_urls(open_payments_data_url)

    for general_payment_url in general_payment_urls:
        with requests.get(general_payment_url, params=None, stream=True) as resp:
            df = pd.read_csv(TqdmReader(resp))

            # Standardize all column field name strings to be lowercase
            df.columns = df.columns.str.lower()

            # Convert cells with NaN values to None to be handled easier by django functions
            df = df.replace({np.nan: None})

            payment_items = []
            for index, row in df.iterrows():
                # Import all columns in row into Payment model except the first
                payment_obj = Payment(**parse_row(row)[1::])
                payment_items.append(payment_obj)

            print("processed {} items".format(str(len(payment_items))))

            Payment.objects.bulk_create(payment_items)


def parse_row(row):
    # Convert existing payment dates to accepted Django default format YYYY-MM-DD
    date_of_payment = row['date_of_payment']
    payment_publication_date = row['payment_publication_date']
    initial_date_format = "%m/%d/%Y"
    final_date_format = "%Y-%m-%d"

    formatted_date_of_payment = format_datetime(date_of_payment, initial_date_format, final_date_format)
    formatted_payment_publication_date = format_datetime(payment_publication_date, initial_date_format, final_date_format)

    row['date_of_payment'] = formatted_date_of_payment
    row['payment_publication_date'] = formatted_payment_publication_date

    return row


def format_datetime(date_string, initial_date_format, final_date_format):
    current_datetime = datetime.datetime.strptime(date_string, initial_date_format)
    formatted_datetime = current_datetime.strftime(final_date_format)

    return formatted_datetime


def get_general_payment_urls(open_payments_data_url):
    res = requests.get(open_payments_data_url)
    content = res.json()

    general_payment_download_urls = []
    general_payment_identifier_term = "General Payment Data – Detailed Dataset"
    distribution_key = "distribution"
    for doc in content:
        for key, value in doc.items():
            key = str.lower(key)
            if key == distribution_key:
                distribution_dict = value[0]
                distribution_title = distribution_dict.get('data', {}).get('title')
                distribution_download_url = distribution_dict.get('data', {}).get('downloadURL')
                print(distribution_title)

                if general_payment_identifier_term in distribution_title:
                    general_payment_download_urls.append(distribution_download_url)

    return general_payment_download_urls


if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms_casestudy.settings')
    django.setup()
    from cms.models import Payment

    run()
