from django.conf.urls import url
from django.urls import path
from .views import food_list, food_remove, orgs_list, orgs_remove, simple_login

urlpatterns = [
    path('food/', food_list),
    path('orgs/', orgs_list),
    path('food/<int:pk>', food_remove),
    path('orgs/<int:pk>', orgs_remove),
    path('login/<str:usr>/<str:passd>', simple_login)
]