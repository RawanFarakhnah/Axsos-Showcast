from django.urls import path
from users_app import views

urlpatterns = [
   path('', views.root, name='root'),
   path('create', views.create, name='create_user'),
]