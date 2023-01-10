from django.db import models


class Payment(models.Model):
    change_type = models.CharField(max_length=50, null=True)

    covered_recipient_type = models.CharField(max_length=50, null=True)
    teaching_hospital_ccn = models.IntegerField(null=True)
    teaching_hospital_id = models.IntegerField(null=True)
    teaching_hospital_name = models.CharField(max_length=100, null=True)

    covered_recipient_profile_id = models.IntegerField(null=True)
    covered_recipient_npi = models.IntegerField(null=True)
    covered_recipient_first_name = models.CharField(max_length=50, null=True)
    covered_recipient_middle_name = models.CharField(max_length=50, null=True)
    covered_recipient_last_name = models.CharField(max_length=50, null=True)
    covered_recipient_name_suffix = models.CharField(max_length=10, null=True)

    recipient_primary_business_street_address_line1 = models.CharField(max_length=100, null=True)
    recipient_primary_business_street_address_line2 = models.CharField(max_length=100, null=True)
    recipient_city = models.CharField(max_length=100, null=True)
    recipient_state = models.CharField(max_length=2, null=True)
    recipient_zip_code = models.CharField(max_length=20, null=True)
    recipient_country = models.CharField(max_length=50, null=True)
    recipient_province = models.CharField(max_length=50, null=True)
    recipient_postal_code = models.CharField(max_length=50, null=True)

    covered_recipient_primary_type_1 = models.CharField(max_length=50, null=True)
    covered_recipient_primary_type_2 = models.CharField(max_length=50, null=True)
    covered_recipient_primary_type_3 = models.CharField(max_length=50, null=True)
    covered_recipient_primary_type_4 = models.CharField(max_length=50, null=True)
    covered_recipient_primary_type_5 = models.CharField(max_length=50, null=True)
    covered_recipient_primary_type_6 = models.CharField(max_length=50, null=True)
    covered_recipient_specialty_1 = models.CharField(max_length=50, null=True)
    covered_recipient_specialty_2 = models.CharField(max_length=50, null=True)
    covered_recipient_specialty_3 = models.CharField(max_length=50, null=True)
    covered_recipient_specialty_4 = models.CharField(max_length=50, null=True)
    covered_recipient_specialty_5 = models.CharField(max_length=50, null=True)
    covered_recipient_specialty_6 = models.CharField(max_length=50, null=True)
    covered_recipient_license_state_code1 = models.CharField(max_length=2, null=True)
    covered_recipient_license_state_code2 = models.CharField(max_length=2, null=True)
    covered_recipient_license_state_code3 = models.CharField(max_length=2, null=True)
    covered_recipient_license_state_code4 = models.CharField(max_length=2, null=True)
    covered_recipient_license_state_code5 = models.CharField(max_length=2, null=True)

    submitting_applicable_manufacturer_or_applicable_gpo_name = models.CharField(max_length=100, null=True)
    applicable_manufacturer_or_applicable_gpo_making_payment_id = models.IntegerField(null=True)
    applicable_manufacturer_or_applicable_gpo_making_payment_name = models.CharField(max_length=100, null=True)
    applicable_manufacturer_or_applicable_gpo_making_payment_state = models.CharField(max_length=2, null=True)
    applicable_manufacturer_or_applicable_gpo_making_payment_country = models.CharField(max_length=50, null=True)

    total_amount_of_payment_usdollars = models.FloatField(max_length=100, null=True)
    date_of_payment = models.DateField(max_length=100, null=True)
    number_of_payments_included_in_total_amount = models.IntegerField(null=True)
    form_of_payment_or_transfer_of_value = models.CharField(max_length=100, null=True)
    nature_of_payment_or_transfer_of_value = models.CharField(max_length=100, null=True)
    city_of_travel = models.CharField(max_length=50, null=True)
    state_of_travel = models.CharField(max_length=2, null=True)
    country_of_travel = models.CharField(max_length=50, null=True)
    physician_ownership_indicator = models.CharField(max_length=3, null=True)
    third_party_payment_recipient_indicator = models.CharField(max_length=50, null=True)
    name_of_third_party_entity_receiving_payment_or_transfer_of_value = models.CharField(max_length=50, null=True)
    charity_indicator = models.CharField(max_length=3, null=True)
    third_party_equals_covered_recipient_indicator = models.CharField(max_length=3, null=True)
    contextual_information = models.CharField(max_length=100, null=True)
    record_id = models.IntegerField(null=True)
    dispute_status_for_publication = models.CharField(max_length=3, null=True)
    related_product_indicator = models.CharField(max_length=3, null=True)

    covered_or_noncovered_indicator_1 = models.CharField(max_length=20, null=True)
    indicate_drug_or_biological_or_device_or_medical_supply_1 = models.CharField(max_length=20, null=True)
    product_category_or_therapeutic_area_1 = models.CharField(max_length=50, null=True)
    name_of_drug_or_biological_or_device_or_medical_supply_1 = models.CharField(max_length=50, null=True)
    associated_drug_or_biological_ndc_1 = models.CharField(max_length=50, null=True)
    associated_device_or_medical_supply_pdi_1 = models.CharField(max_length=50, null=True)

    covered_or_noncovered_indicator_2 = models.CharField(max_length=20, null=True)
    indicate_drug_or_biological_or_device_or_medical_supply_2 = models.CharField(max_length=20, null=True)
    product_category_or_therapeutic_area_2 = models.CharField(max_length=50, null=True)
    name_of_drug_or_biological_or_device_or_medical_supply_2 = models.CharField(max_length=50, null=True)
    associated_drug_or_biological_ndc_2 = models.CharField(max_length=50, null=True)
    associated_device_or_medical_supply_pdi_2 = models.CharField(max_length=50, null=True)

    covered_or_noncovered_indicator_3 = models.CharField(max_length=20, null=True)
    indicate_drug_or_biological_or_device_or_medical_supply_3 = models.CharField(max_length=20, null=True)
    product_category_or_therapeutic_area_3 = models.CharField(max_length=50, null=True)
    name_of_drug_or_biological_or_device_or_medical_supply_3 = models.CharField(max_length=50, null=True)
    associated_drug_or_biological_ndc_3 = models.CharField(max_length=50, null=True)
    associated_device_or_medical_supply_pdi_3 = models.CharField(max_length=50, null=True)

    covered_or_noncovered_indicator_4 = models.CharField(max_length=20, null=True)
    indicate_drug_or_biological_or_device_or_medical_supply_4 = models.CharField(max_length=20, null=True)
    product_category_or_therapeutic_area_4 = models.CharField(max_length=50, null=True)
    name_of_drug_or_biological_or_device_or_medical_supply_4 = models.CharField(max_length=50, null=True)
    associated_drug_or_biological_ndc_4 = models.CharField(max_length=50, null=True)
    associated_device_or_medical_supply_pdi_4 = models.CharField(max_length=50, null=True)

    covered_or_noncovered_indicator_5 = models.CharField(max_length=20, null=True)
    indicate_drug_or_biological_or_device_or_medical_supply_5 = models.CharField(max_length=20, null=True)
    product_category_or_therapeutic_area_5 = models.CharField(max_length=50, null=True)
    name_of_drug_or_biological_or_device_or_medical_supply_5 = models.CharField(max_length=50, null=True)
    associated_drug_or_biological_ndc_5 = models.CharField(max_length=50, null=True)
    associated_device_or_medical_supply_pdi_5 = models.CharField(max_length=50, null=True)

    program_year = models.IntegerField(null=True)
    payment_publication_date = models.DateField(max_length=50, null=True)

    delay_in_publication_indicator = models.CharField(max_length=50, null=True)
