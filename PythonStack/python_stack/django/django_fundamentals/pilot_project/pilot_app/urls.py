from pilot_app import views
from django.urls import path

urlpatterns = [
    path('', views.root),
    path('another_route', views.another_method),
    path('redirected_route', views.redirected_method)
]

