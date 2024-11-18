from django.contrib import admin
from django.urls import path, include


# URL configuration
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),  # Include hello app URLs
]
