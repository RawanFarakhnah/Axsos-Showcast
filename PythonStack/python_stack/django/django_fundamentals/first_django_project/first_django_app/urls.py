from django.urls import path
from first_django_app import views

urlpatterns = [
    path('', views.root),
    path('bears', views.one_method),      
    path('bears/<int:my_val>', views.another_method),
    path('bears/<str:name>/poke', views.yet_another),
    path('bears/<int:id>/<str:color>', views.one_more)
]