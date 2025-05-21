from django.contrib import admin
from django.urls import path, include  # Ensure `include` is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # This must match `accounts/urls.py`
]