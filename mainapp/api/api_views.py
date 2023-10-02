from rest_framework import generics, viewsets
from . import serializers
from ..models import *


class UnitList(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = serializers.UnitSerializer


class UnitDetails(generics.RetrieveAPIView):
    queryset = Unit.objects.all()
    serializer_class = serializers.UnitSerializer


class UnitsForAircraft(generics.ListAPIView):
    serializer_class = serializers.UnitSerializer

    def get_queryset(self):
        return Unit.objects.filter(aircraft=self.kwargs['ar_id'])


class AircraftList(generics.ListAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = serializers.AircraftSerializer


class AircraftDetails(generics.RetrieveAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = serializers.AircraftSerializer


class AircraftsForGarage(generics.ListAPIView):
    serializer_class = serializers.AircraftSerializer

    def get_queryset(self):
        return Aircraft.objects.filter(garage=self.kwargs['gr_id'])


class GarageList(generics.ListAPIView):
    queryset = Garage.objects.all()
    serializer_class = serializers.GarageSerializer


class GarageDetails(generics.RetrieveAPIView):
    queryset = Garage.objects.all()
    serializer_class = serializers.GarageSerializer
