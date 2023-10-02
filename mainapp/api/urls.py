from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import api_views
from rest_framework import routers
app_name = 'api'
router = routers.DefaultRouter()
router.register('units', api_views.UnitList)

urlpatterns =[
    path('', include(router.urls)),
    path('aircrafts/', api_views.AircraftList.as_view()),
    path('garages/', api_views.GarageList.as_view()),
    path('units/<int:pk>/', api_views.UnitDetails.as_view()),
    path('aircrafts/<int:pk>/', api_views.AircraftDetails.as_view()),
    path('garages/<int:pk>/', api_views.GarageDetails.as_view()),
    path('garage/<int:gr_id>', api_views.AircraftsForGarage.as_view()),
    path('aircraft/<int:ar_id>', api_views.UnitsForAircraft.as_view())
]

#urlpatterns = format_suffix_patterns(urlpatterns)
