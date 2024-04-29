from django.urls import path

from . import views

urlpatterns = [
    path('energy/', views.energy, name='index'),
    path("data/", views.upload_excel, name="monthly_consumption"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("userPreferences/", views.userPreferences, name="user_preferences"),
    path("getPreferences/", views.getUserPreferences, name="getUserPreferences")
]