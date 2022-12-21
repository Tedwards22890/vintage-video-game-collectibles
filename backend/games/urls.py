from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.game_list),
    path('', views.games_post),
    path('<int:pk>/', views.games_by_id)
]