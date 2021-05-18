from django.conf.urls import url
from django.urls import path
from .views import create_rider, rider_list, rider_detail, delete_rider, edit_rider, export_riders_csv

urlpatterns = [
    path('', rider_list, name='rider_list'),
    path('create_rider/', create_rider, name='create_rider'),
    path('rider_detail/<str:pk>/', rider_detail, name='rider_detail'),
    path('edit_rider/<str:pk>', edit_rider, name='edit_rider'),
    path('delete_rider/<str:pk>', delete_rider, name='delete_rider'),
    url(r'^export/csv/$', export_riders_csv, name='export_riders_csv'),
]