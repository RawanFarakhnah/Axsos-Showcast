from django.urls import path
from tv_shows_app import views

urlpatterns = [
    path('shows', views.root, name="root"),
    path('shows/<int:id>', views.view_show , name="view_show"),

    path('shows/new', views.new_show, name="new_show"),
    path('shows/create',views.create_show, name="create_show" ), 

    path('shows/<int:id>/edit', views.edit_show, name="edit_show"),
    path('shows/<int:id>/update',views.update_show, name="update_show"), 

    path('shows/<int:id>/destroy',views.delete_show, name="delete_show"), 
]