from rest_framework.decorators import action
from rest_framework.routers import SimpleViewSet

from .models import *

class ApiViewSet(SimpleViewSet):

    @action(methods=['get'], detail=True)
    def get_countries(self, request):
        Country.objects