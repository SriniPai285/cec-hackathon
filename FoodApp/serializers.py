from rest_framework import serializers
from .models import Food, Organisation

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Organisation
        fields = ('id', 'name', 'email', 'category', 'address', 'phone')
        read_only_fields = ('id', 'name', 'email', 'category', 'address', 'phone')

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Food
        fields = ('id', 'name', 'available_till', 'image', 'partial_allowed', 'donator', 'created_at', 'quantity', 'units', 'description', 'alloted_to')