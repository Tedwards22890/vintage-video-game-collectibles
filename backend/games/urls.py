from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.game_list),
    path('', views.games),
    path('<str:video_id>/', views.game_by_game_id)
]