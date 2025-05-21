from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Meal
from .serializers import MealSerializer


class MealFilterByGoal(APIView):
    def get(self, request, *args, **kwargs):
        goal = request.query_params.get('goal', None)
        if goal:
            meals = Meal.objects.filter(goal=goal)
        else:
            meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
