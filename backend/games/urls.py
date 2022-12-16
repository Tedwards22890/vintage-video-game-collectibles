from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.game_list),
    path('', views.games),
    path('<str:video_id>/', views.games_by_id)
]