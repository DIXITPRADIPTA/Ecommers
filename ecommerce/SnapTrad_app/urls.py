from django.urls import path
from . import views

urlpatterns = [
    path('login/customer/', views.customer_login, name='customer_login'),
    path('login/seller/', views.seller_login, name='seller_login'),
    path('', views.home, name='home'),
]
