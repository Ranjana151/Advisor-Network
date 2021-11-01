from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/advisor/', views.createAdvisor, name="advisor"),
    path('user/register/', views.customerRegister, name="register"),
    path('user/login/', views.customerLogIn, name='LoginIn'),
    path('user/<user_id>/advisor/', views.getAdvisor, name="get advisor"),
    path('user/<user_id>/advisor/booking/', views.getBookingCall, name="get book call"),
    path('user/<user_id>/advisor/<advisor_id>/', views.bookCall, name="book call"),


]