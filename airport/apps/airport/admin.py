from django.contrib import admin

from .models import *

admin.site.register(Country)
admin.site.register(Airport)
admin.site.register(Airline)
admin.site.register(AirplaneType)
admin.site.register(Airplane)
admin.site.register(Passenger)
admin.site.register(Ticket)
admin.site.register(Flight)
