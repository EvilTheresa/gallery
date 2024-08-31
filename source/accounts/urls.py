from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RegisterView, ProfileView, CustomLogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
]
