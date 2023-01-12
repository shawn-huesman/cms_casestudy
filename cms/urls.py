from django.urls import path
from cms.views import HomePageView, SearchResultsView, export_excel

urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("", HomePageView.as_view(), name="home"),
    path('remove_item/<str:q>/', export_excel, name='export_excel')
]
