from django.conf.urls import url
from django.urls import path
from .views import create_order, order_list, edit_order, delete_order, assign_rider, deliver_order, order_detail

urlpatterns = [
    path('', order_list, name='order_list'),
    path('create_order/', create_order, name='create_order'),
    path('order_detail/<str:pk>/', order_detail, name='order_detail'),
    path('edit_order/<str:pk>', edit_order, name='edit_order'),
    path('delete_order/<str:pk>', delete_order, name='delete_order'),
    path('assign_rider/<str:pk>', assign_rider, name='assign_rider'),
    path('deliver_order/<str:pk>', deliver_order, name='deliver_order')
]
