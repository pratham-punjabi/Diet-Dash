from django.urls import path
from .views import login_view, register_view  # Ensure `views.py` exists

urlpatterns = [
    path('login/', login_view, name='login'),  # Example login route
    path('register/', register_view, name='register'),
]
