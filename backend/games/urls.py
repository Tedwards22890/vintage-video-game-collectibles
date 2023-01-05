from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('all/', views.game_list),
    path('', views.games_post),
    path('<int:pk>/', views.games_by_id),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)