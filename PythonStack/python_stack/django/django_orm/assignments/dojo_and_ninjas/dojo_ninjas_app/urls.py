from django.urls import path
from dojo_ninjas_app import views

urlpatterns = [
    path('', views.root, name='root'),
    path('create_dojo', views.create_dojo, name="create_dojo"),
    path('create_ninja', views.create_ninja, name="create_ninja"),
    path('delete_dojo/<int:id>', views.delete_dojo, name='delete_dojo')
]
