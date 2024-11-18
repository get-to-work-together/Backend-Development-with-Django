from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required

from rest_framework import permissions, viewsets

from .models import *
from .forms import *
from.serializers import *


def countries(request):
    country = request.GET.get('country', None)
    if country:
        qs = Country.objects.filter(code__icontains=country)
    else:
        qs = Country.objects.all()
    return render(request, 'countries.html', {'title':'Countries',
                                              'countries': qs})


def add_country(request):
    form = CountryForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            return redirect('/airport/countries')
        else:
            form = CountryForm()

    return render(request, 'add_country.html', {'form': form})


class AddCountry(CreateView):
    model = Country
    success_url = '/airport/countries'
    fields = ['name', 'code', 'time_zone']


@login_required
def airports(request):
    country = request.GET.get('country', None)
    if country:
        qs = Airport.objects.filter(country__icontains=country).order_by('name')
    else:
        qs = Airport.objects.all().order_by('name')
    return render(request, 'airports.html', {'title':'Airports',
                                             'airports': qs})


# @login_required
class AirportListView(ListView): 
    model = Airport
    template_name = 'airports.html'
    extra_context = {'title':'Airports'}


class AddFlight(CreateView):
    model = Flight
    success_url = '/airport/countries'
    fields = ['flight_number', 
              'departure_datetime',
              'arrival_datetime',
              'airline',
              'departure_airport',
              'arrival_airport',
              'airplane']



# API views

class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows countries to be viewed or edited.
    """
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    # permission_classes = [permissions.IsAuthenticated]


class AirportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = AirportSerializer
    def get_queryset(self):
        queryset = Airport.objects.all()
        country = self.request.query_params.get('country')
        if country is not None:
            queryset = queryset.filter(country=country)
        return queryset
    # permission_classes = [permissions.IsAuthenticated]