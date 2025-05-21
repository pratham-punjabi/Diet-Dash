from django.urls import path
from .views import MealFilterByGoal  # only import what you're using
  # ya home_redirect if redirect karna hai
  

urlpatterns = [
    path('meals/', MealFilterByGoal.as_view(), name='meal-filter'),
]

