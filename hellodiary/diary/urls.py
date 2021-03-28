from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name="loginPage"),
    path('logout/', views.logoutUser, name="logoutPage"),
    path('register/', views.register, name="register"),
    path('diary/', views.home, name="home"),
    path('allEntries/', views.allEntries, name="all-entries"),
    path('analytics/', views.analytics, name="analytics")

]
