from rest_framework import serializers
from .models import SmartHome

class SmartHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartHome
        fields = ('id', 'plug')