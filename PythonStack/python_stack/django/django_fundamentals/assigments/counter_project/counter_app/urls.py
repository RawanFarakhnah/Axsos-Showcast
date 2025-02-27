from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='index'),
    path('increase', views.increase),
    path('custom_increase', views.custom_increase),
    path('destroy_session', views.clear_session)
]