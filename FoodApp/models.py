from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Organisation(models.Model):
    # user_details = User
    # user_details = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(null=True)
    category = models.CharField(max_length=255, blank=False, null=False)
    address = models.TextField(max_length=65535)
    phone = models.CharField(max_length=100, null=False, default="NO_PHONE")

    def __str__(self):
        return str(self.name)

class Food(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=False)
    created_at = models.DateTimeField('created on ', auto_now_add=True)
    quantity = models.IntegerField(default=0, blank=False, null=False)
    available_till = models.DateTimeField(null=False, blank=False)
    image = models.FileField(upload_to='food/', null=False, blank=False)
    partial_allowed = models.BooleanField(default=False)
    description = models.TextField(max_length=255)
    donator = models.IntegerField(blank=False, null=True)
    alloted_to = models.IntegerField(blank=False, null=True)
    units = models.CharField(max_length=255, default="No.s", blank=False, null=False)

    def __str__(self):
        return self.name