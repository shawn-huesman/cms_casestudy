from functools import reduce
import operator

from django.views.generic import TemplateView
from django.db.models import Q

import django_tables2 as tables
from django_tables2 import SingleTableView

from .models import Payment


relevant_fields = ["covered_recipient_first_name", "covered_recipient_last_name",
                       "recipient_city", "recipient_state", "recipient_zip_code",
                       "recipient_country", "covered_recipient_specialty_1",
                       "submitting_applicable_manufacturer_or_applicable_gpo_name",
                       "total_amount_of_payment_usdollars", "date_of_payment",
                       "form_of_payment_or_transfer_of_value",
                       "nature_of_payment_or_transfer_of_value"]


class HomePageView(TemplateView):
    template_name = 'home.html'


class PaymentTable(tables.Table):
    class Meta:
        model = Payment
        fields = relevant_fields


class SearchResultsView(SingleTableView):
    model = Payment
    table_class = PaymentTable
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        # Return payment rows from query in relevant fields
        object_list = Payment.objects.filter(reduce(operator.or_,
                                                    [Q(**{f"{field}__icontains": query}) for field in relevant_fields]))
        return object_list

    def get(self, request, *args, **kwargs):
        self.query = self.request.GET.get("q")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.query
        return context

