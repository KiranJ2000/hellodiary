from django.urls import path
from . import views

urlpatterns = [
    path('diary/', views.home, name="home"),
    path('allEntries/', views.allEntries, name="all-entries"),
    path('analytics/', views.analytics, name="analytics")

]
