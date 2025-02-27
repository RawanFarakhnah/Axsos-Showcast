from django.urls import path
from first_app import views 

urlpatterns = [
    path('', views.root),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/edit', views.edit),
    path('blogs/json', views.json),
]