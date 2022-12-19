from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_all_carts),
    path('<str:video_id>/', views.comment_by_video_id)
]