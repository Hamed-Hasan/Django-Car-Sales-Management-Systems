from django.urls import path
from . import views
from .views import CustomLogoutView
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
  path('logout/', CustomLogoutView.as_view(), name='logout'),]
