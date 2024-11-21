from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = [
    path('countries', login_required(countries), name='countries'),
    path('airports', login_required(AirportListView.as_view()), name='airports'),
    path('add_country', login_required(add_country)),
    path('add_country2', login_required(AddCountry.as_view()), name='add_country'),
    path('add_flight', login_required(AddFlight.as_view()), name='add_flight'),

    path('api/v1/countries', CountryViewSet.as_view({'get':'list'}), name='api_countries_list'),
    path('api/v1/countries/<str:pk>', CountryViewSet.as_view({'get':'list'}), name='api_countries_list'),
    path('api/v1/airports', AirportViewSet.as_view({'get':'list'}), name='api_airports_list'),
    path('api/v1/airports/<int:pk>', AirportViewSet.as_view({'get':'list'}), name='api_airports_list'),
]
