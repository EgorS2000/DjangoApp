from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from api.api_views import (
    PersonalDataView,
    CompaniesView,
    companies_creation_view
)

urlpatterns = [
    path(
        "companies_creation/",
        csrf_exempt(companies_creation_view),
        name='companies_creation'
    ),
    path(
        "employees/",
        PersonalDataView.as_view(),
        name='employees'
    ),
    path(
        "companies/",
        CompaniesView.as_view(),
        name='companies'
    ),
]
