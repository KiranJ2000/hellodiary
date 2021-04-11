from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name="login_page"),
    path('logout/', views.logout_user, name="logout_page"),
    path('register/', views.register, name="register"),
    path('diary/', views.home, name="home"),
    path('all_entries/', views.all_entries, name="all_entries"),
    path('analytics/', views.analytics, name="analytics"),
    path('create_diary/', views.create_diary, name="create_diary"),
    path('detail_view/<str:pk>/<slug:slug>/', views.detail_view, name="detail_view"),
    path('update_diary/<str:pk>/<slug:slug>/', views.update_diary, name="update_diary"),
    path('delete_diary/<str:pk>/', views.delete_diary, name="delete_diary"),
]
