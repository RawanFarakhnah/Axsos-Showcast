from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.root),
    path('some_route', views.some_function),
    path('success', views.show_user)
]