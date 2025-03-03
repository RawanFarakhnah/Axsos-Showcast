from django.urls import path
from ninja_gold_app import views

urlpatterns = [
    path('game_setup', views.game_setup, name='game_setup'),
    path('', views.root, name="root"),
    path('process_money/<str:location>', views.process_money, name='process_money'),
    path('reset', views.reset, name='reset'),
    path('achievement', views.achievement, name='achievement'), 
]