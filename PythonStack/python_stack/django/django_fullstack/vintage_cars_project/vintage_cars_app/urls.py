from django.urls import path
from vintage_cars_app import views


urlpatterns = [
    path('', views.root, name='root'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cars/' , views.cars, name='cars'),
    path('cars/new/', views.new_car, name="new_car"),
    path('cars/create/', views.create_car, name='create_car'),
    path('cars/view/<int:car_id>/' , views.view_car, name='view'),
    path('cars/edit/<int:car_id>/' , views.edit_car, name='edit'),
    path('cars/update/<int:car_id>/' , views.update_car, name='update_car'),
    path('cars/destroy/<int:car_id>/' , views.destroy_car, name='destroy'),
    path('cars/order/<int:car_id>/', views.order_car, name='order'),
    path('cars/purchase_orders',views.purchase_orders, name='purchase_orders' ),
    path('cars/cancle_purchase_order/<int:car_id>/',views.cancle_purchase_order, name='cancle_purchase_order'),    
]
