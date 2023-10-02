"""AirControl URL Configuration"""
from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('exit/', views.LogoutView.as_view(next_page='/'), name='exit'),
    path('unit/<int:un_id>/', login_required(edit), name= 'unt'),
    path('garage/<int:gr_id>/', login_required(AircraftsShow.as_view()), name='garage'),
    path('aircraft/<int:ar_id>/', login_required(UnitsShow.as_view()), name='arcr'),
    path('', login_required(GaragesShow.as_view()), name = 'garages'),
    path('login/', views.LoginView.as_view(), name='login')
]
