from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Food, Organisation
from .serializers import FoodSerializer, OrganisationSerializer

# class OrganisationViewSet(viewsets.ModelViewSet):
#     queryset = Organisation.objects.all()
#     serializer_class = OrganisationSerializer

# class FoodViewSet(viewsets.ModelViewSet):
#     queryset = Food.objects.all().order_by('created_at')
#     serializer_class = FoodSerializer

@api_view(['GET', 'POST'])
def food_list(request):
    if request.method == 'GET':
        all_food = Food.objects.all()
        all_food_serialized = FoodSerializer(all_food, many=True)
        return Response(all_food_serialized.data)
    elif request.method == 'POST':
        serializer = FoodSerializer(data=request.data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def food_remove(request, pk):
    obj = Food.objects.get(pk=pk)
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def orgs_list(request):
    if request.method == 'GET':
        all_orgs = Organisation.objects.all()
        all_orgs_serialized = OrganisationSerializer(all_orgs, many=True)
        return Response(all_orgs_serialized.data)
    elif request.method == 'POST':
        serializer = OrganisationSerializer(data=request.data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def orgs_remove(request, pk):
    obj = Organisation.objects.get(pk=pk)
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def simple_login(request, user, passd):
    if passd != "password":
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    if user == "donator":
        return Response(status=status.HTTP_202_ACCEPTED)
    elif user == "distributor":
        return Response(status=status.HTTP_202_ACCEPTED)