from django.urls import path
from books_app import views

urlpatterns = [
    path('', views.root, name='root')
]