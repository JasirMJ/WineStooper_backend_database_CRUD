"""django_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from warehouse import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warehouse/', views.WareHouseAPI.as_view()),
    path('distributions/', views.DistributionCenterAPI.as_view()),
    path('customers/', views.CustomerAPI.as_view()),
    path('orders/', views.OrderAPI.as_view()),
    path('order-items/', views.OrderItemsAPI.as_view()),
    path('wine-colors/', views.WineColorAPI.as_view()),
    path('wine-country/', views.WineCountryAPI.as_view()),
    path('wines/', views.WineAPI.as_view()),

    # path("")
]
