from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('', include('quizapp.urls')),  # Include the quizapp URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Django's built-in auth URLs for login/logout
]
