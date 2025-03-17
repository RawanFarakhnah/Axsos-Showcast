from django.urls import path
from courses_app import views

urlpatterns = [
    path("", views.main, name="main"),
    path("courses/", views.root, name="root"),
    path("courses/create", views.create, name="create"),
    path("courses/destroy/<int:id>", views.destroy, name="destroy"),
    path("courses/remove/<int:id>", views.remove, name="remove")
]