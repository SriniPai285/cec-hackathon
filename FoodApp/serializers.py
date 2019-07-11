from rest_framework import serializers
from .models import Food, Organisation
from django.contrib.auth.models import User

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Organisation
        fields = ('id', 'name', 'email', 'category', 'address', 'phone')

class FoodSerializer(serializers.ModelSerializer):
    donator_set = OrganisationSerializer(many=True, read_only=True)
    alloted_to_set = OrganisationSerializer(many=True, read_only=True)
    class Meta:
        model  = Food
        fields = ('name', 'available_till', 'image', 'partial_allowed', 'donator_set', 'created_at', 'description', 'alloted_to_set')