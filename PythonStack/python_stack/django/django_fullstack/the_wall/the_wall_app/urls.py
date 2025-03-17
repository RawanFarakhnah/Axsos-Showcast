from django.urls import path
from the_wall_app import views

urlpatterns = [
    path('', views.root, name='root'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('wall/' , views.wall, name='wall'),
    path('wall/create_message/' , views.create_message, name='create_message'),
    path('wall/create_comment/' , views.create_comment, name='create_comment'),
    path('wall/delete_message/<int:message_id>', views.delete_message, name='delete_message')
]