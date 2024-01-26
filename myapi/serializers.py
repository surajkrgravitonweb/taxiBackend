from rest_framework import serializers
from .models import *

class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserRegistration
        fields='__all__'


class GetTaxiFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetTaxiForm
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


