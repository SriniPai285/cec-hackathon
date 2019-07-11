from rest_framework import viewsets
from .models import Food, Organisation, User
from .serializers import FoodSerializer, OrganisationSerializer

class OrganisationViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all().order_by('created_at')
    serializer_class = FoodSerializer