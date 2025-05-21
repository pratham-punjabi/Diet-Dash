from django.db import models

class AdminUser(models.Model):  # Renamed from Admin to AdminUser (to avoid conflict)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128)  # Add password_hash field for authentication

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128)  # Add password_hash field for authentication

class Meal(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()