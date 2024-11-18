from django.db import models


class Country(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.code} - {self.name}'

    class Meta:
        verbose_name_plural = "Countries"


class Timezone(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=80)
    fullname = models.CharField(max_length=80)
    utc_offset = models.CharField(max_length=10)

    def __str__(self):
        return self.code


class AirplaneType(models.Model):
    manufacturer = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    seating_capacity = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Airline(models.Model):
    iata = models.CharField(max_length=10)
    icao = models.CharField(max_length=10)
    name = models.CharField(max_length=80)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True)
    # country_code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.icao} - {self.name}'


class Airplane(models.Model):
    tail_number = models.CharField(max_length=10)
    airplane_type = models.ForeignKey(AirplaneType, on_delete=models.DO_NOTHING, null=True)
    airline = models.ForeignKey(Airline, on_delete=models.DO_NOTHING, null=True)
    # airplane_type_name = models.CharField(max_length=80)
    # airline_name = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.tail_number} - {self.airline} - {self.airplane_type}'


class Airport(models.Model):
    iata = models.CharField(max_length=10)
    name = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True)
    timezone = models.ForeignKey(Timezone, on_delete=models.DO_NOTHING, null=True)
    # country_code = models.CharField(max_length=80)
    # timezone_full = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.iata} - {self.name} - {self.country}'


class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure_datetime = models.DateTimeField()
    arrival_datetime = models.DateTimeField()
    departure_airport = models.ForeignKey(Airport, on_delete=models.DO_NOTHING, related_name='departure')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.DO_NOTHING, related_name='arrival')
    airline = models.ForeignKey(Airline, on_delete=models.DO_NOTHING)
    airplane = models.ForeignKey(Airplane, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.flight_number} - {self.departure_airport} - {self.arrival_airport} - {self.departure_datetime}'


class Ticket(models.Model):
    nr = models.CharField(max_length=20)
    seat_number = models.CharField(max_length=10)
    flight = models.ForeignKey(Flight, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.nr} - {self.seat_number}'


class Passenger(models.Model):
    name = models.CharField(max_length=80)
    residence = models.CharField(max_length=80)
    flight = models.ForeignKey(Ticket, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name} - {self.residence}'
