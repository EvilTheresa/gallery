from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RegisterView, ProfileView

urlpatterns = [
    # Аутентификация
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # Профиль пользователя
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
]
