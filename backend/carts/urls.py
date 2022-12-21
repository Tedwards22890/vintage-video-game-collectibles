from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_all_carts),
    path('<int:pk>/', views.cart_by_id),
    path('', views.cart_post),
]