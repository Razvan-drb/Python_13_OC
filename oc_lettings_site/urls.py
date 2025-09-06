"""
URL configuration for oc_lettings_site project.
Includes the main routes for the home page, admin, and the lettings/profiles apps.
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.http import HttpResponse


def trigger_error(request):
    division_by_zero = 1 / 0
    return HttpResponse("Hello")


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
