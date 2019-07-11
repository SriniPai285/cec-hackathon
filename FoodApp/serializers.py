from rest_framework import serializers
from .models import Food, Organisation
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ('id', 'username', 'email')

class OrganisationSerializer(serializers.HyperlinkedModelSerializer):
    user_details = UserSerializer()#many=True, read_only=True)
    class Meta:
        model  = Organisation
        fields = ('user_details', 'category', 'address', 'phone')

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    donator = OrganisationSerializer(many=True, read_only=True)
    class Meta:
        model  = Food
        fields = ('name', 'available_till', 'image', 'partial_allowed', 'donator', 'created_at', 'description', 'alloted_to')