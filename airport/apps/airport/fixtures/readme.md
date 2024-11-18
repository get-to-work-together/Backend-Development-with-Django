### import fixtures

python manage.py loaddata apps/airport/fixtures/countries.json
python manage.py loaddata apps/airport/fixtures/timezones.json
python manage.py loaddata apps/airport/fixtures/airports.json
python manage.py loaddata apps/airport/fixtures/airlines.json
python manage.py loaddata apps/airport/fixtures/airplane_types.json
python manage.py loaddata apps/airport/fixtures/airplanes.json

### set foreign keys:

update airport_airplane
set airline_id = 
  (select id from airport_airline where name =  airline_name)

update airport_airport
set country_id = 
  (select id from airport_country where code = airport_port.country_code)


update airport_airport
set timezone_id = 
  (select id from airport_timezone where name = timezone_full)


update airport_airline
set country_id = 
  (select id from airport_country where code = airport_airline.country_code)

update airport_airplane
set airplane_type_id = 
  (select id from airport_airplanetype where name = airplane_type_name);

### Dump data to fixtures

python manage.py dumpdata airport.Country > apps/airport/fixtures/dump_countries.json
python manage.py dumpdata airport.Timezone > apps/airport/fixtures/dump_timezones.json
python manage.py dumpdata airport.Airport > apps/airport/fixtures/dump_airports.json 
python manage.py dumpdata airport.Airline > apps/airport/fixtures/dump_airlines.json
python manage.py dumpdata airport.AirplaneType > apps/airport/fixtures/dump_airplane_types.json
python manage.py dumpdata airport.Airplane > apps/airport/fixtures/dump_airplanes.json  