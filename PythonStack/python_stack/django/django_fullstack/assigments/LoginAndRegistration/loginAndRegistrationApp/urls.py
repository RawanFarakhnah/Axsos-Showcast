from loginAndRegistrationApp import views
from django.urls import path,include

urlpatterns = [
    path('', views.root , name='root'),
    path('register/', views.register , name='register'),
    path('login/', views.login , name='login'),
    path('success/', views.success , name='success'),
    path('logout', views.logout , name='logout'),
]