from rest_framework import serializers
from .models import CoffeeMachines, CoffeePods

class CoffeeMachineSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoffeeMachines
        fields = ('sku','water_line_compatible')
    

class CoffeePodSerializer(serializers.ModelSerializer):

        class Meta:
        model = CoffeePods
        fields = ('sku','coffee_flavor','pack_size')