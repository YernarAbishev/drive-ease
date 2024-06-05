from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('cars/list/', views.user_cars_page, name='user_cars_page'),
    path('cars/add/', views.add_user_car, name='add_user_car'),
    path('cars/edit/<int:pk>/', views.edit_user_car, name='edit_user_car'),
    path('cars/delete/<int:pk>/', views.delete_user_car, name='delete_user_car'),
    path('cars/<int:pk>/histories/', views.car_histories_page, name='car_histories_page'),
    path('cars/<int:pk>/histories/add/', views.add_history_page, name='add_history_page'),
    path('histories/<int:pk>/edit/', views.edit_history_page, name='edit_history_page'),
    path('histories/<int:pk>/delete/', views.delete_history_page, name='delete_history_page'),
    path('sign-up/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
]