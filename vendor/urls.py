from django.conf.urls import url
from django.urls import path
from .views import create_vendor,  vendor_list, vendor_detail, edit_vendor, delete_vendor, export_vendors_csv

urlpatterns = [
    path('', vendor_list, name='vendor_list'),
    path('create_vendor/', create_vendor, name='create_vendor'),
    path('vendor_detail/<str:pk>/', vendor_detail, name='vendor_detail'),
    path('edit_vendor/<str:pk>', edit_vendor, name='edit_vendor'),
    path('delete_vendor/<str:pk>', delete_vendor, name='delete_vendor'),
    url(r'^export/csv/$', export_vendors_csv, name='export_vendors_csv'),
]
