# from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

# URL configuration
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('hello.urls')),  # Include hello app URLs
    path('', include('home.urls')),  # Include hello app URLs
    path('books/', include('books.urls')),  # Include books app URLs
    path('accounts/', include('django.contrib.auth.urls')),
] # + debug_toolbar_urls()