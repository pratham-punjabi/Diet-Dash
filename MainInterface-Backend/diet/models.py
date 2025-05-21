from django.db import models

class Meal(models.Model):
    meal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image_url = models.URLField(max_length=500)  # 👉 Add this line for image link
    calories = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    fat = models.IntegerField()
    type = models.CharField(max_length=20)  # Veg / Non-Veg
    created_by = models.IntegerField()
    goal = models.CharField(max_length=50)

    class Meta:
        db_table = 'meals'  # 👈 Map to your existing MySQL table
