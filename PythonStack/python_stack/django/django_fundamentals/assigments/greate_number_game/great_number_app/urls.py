from django.urls import path
from great_number_app import views

urlpatterns = [
    path('', views.root, name='root'),
    path('try_again', views.try_again),
    path('guess_number', views.guess_number)
]