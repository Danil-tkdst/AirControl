from rest_framework import serializers
from ..models import *


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ['id', 'type', 'name', 'garage']


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'aircraft', 'name', 'parttype', 'repairdate',
                  'controldate', 'time_to_fix', 'time_to_control',
                  'comment']


class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = ['id', 'name']
