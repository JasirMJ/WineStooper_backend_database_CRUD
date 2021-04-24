from django.urls import path


from .views import *

urlpatterns = [
    path('countrylist/',CountryAPI.as_view(),name='index'),
    path('color/',ColorAPI.as_view(),name='index')
    ]

