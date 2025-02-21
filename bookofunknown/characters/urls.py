from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list, name='character_list'),
    path('<int:character_id>/', views.character_detail, name='character_detail'),
    path('add/', views.add_character, name='add_character'),
]
