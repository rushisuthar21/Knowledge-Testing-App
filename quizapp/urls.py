from django.urls import path
from . import views

app_name = 'quizapp'

urlpatterns = [
    path('', views.HomePageView, name='home'),  # Home page
    path('register/', views.RegisterView, name='register'),  # Registration page
    path('login/', views.LoginView, name='login'),  # Login page
    path('logout/', views.LogoutView, name='logout'),  # Logout view
    path('quiz/', views.QuizView, name='quiz'),  # Quiz page
    path('scores/', views.ScoreView, name='scores'),  # Scores page
    path('admin-dashboard/', views.AdminDashboardView, name='admin_dashboard'),  # Admin dashboard
]
