# cms_casestudy

This app uses data from Centers for Medicare & Medicaid Services (CMS) Open Payment's General Payment datasets from years 2015-2021. 

The attached database uses the first 10K rows of each excel file from each year. Optionally the database creation script can be used to download and import
the datasets directly from the CMS API. However, each excel file is approximately 5GB large with >10M rows and takes multiple hours to set up.

The search function works on the following fields which are considered relevant:
*"covered_recipient_first_name", "covered_recipient_last_name", "physician_first_name", "physician_last_name", "recipient_city", "recipient_state", 
"recipient_zip_code", "recipient_country", "covered_recipient_specialty_1", "submitting_applicable_manufacturer_or_applicable_gpo_name",
"total_amount_of_payment_usdollars", "date_of_payment", "form_of_payment_or_transfer_of_value", "nature_of_payment_or_transfer_of_value"*

However, when exported to Excel, all fields found in the dataset are exported.

# Installation

(If any of these commands do not work, try either 'python3' or 'python3.11' in place of 'python')

1. Download Python 3.11 from https://www.python.org/downloads/

2. Download Pip package manager

Usually Python3 comes with Pip installed, but in case it does not, use these terminal commands:

(Windows, Mac)
```
python get-pip.py
```

(Linux)
```
sudo apt-get install python3-pip
```

if these do not work, try the following
```
sudo easy_install pip
```

3. Clone this repo or download as zip file.

4. (Optional) Create and activate Python virtual environment

Creation (Windows, Mac, Linux):
```
python -m venv venv
```

Activate (Windows):
```
.\venv\Scripts\activate
```

Activate (Mac, Linux):
```
source venv/bin/activate
```

5. Install requirements
(Windows, Mac, Linux):
```
pip install -r requirements.txt
```

6. Migrate App
(Windows, Mac, Linux):
```
python manage.py migrate
```

7. Run Server
(Windows, Mac, Linux):
```
python manage.py runserver
```

# Notes for Improvement

To improve this application with more time I would look into the following:
- Normalize legacy fields from the dataset from the year 2015 such as physician_first_name and physician_last_name which is 
covered_recipient_first_name and covered_recipient_last_name in subsequent years.

- Speed up QuerySet filtering and django_tables2 display and rendering on larger datasets.

- Implement auto-complete by using the popular typehead.js JavaScript library rather than a standard Django form input typeahead.
