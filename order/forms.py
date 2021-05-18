from django.forms import ModelForm
from .models import Order
from django import forms


class CreateOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product_name', 'product_img', 'receiver_name', 'receiver_number', 'receiver_address',
                  'receiver_alternate_number']


class AssignRiderForm(ModelForm):
    class Meta:
        model = Order
        # fields = ['is_rider_assigned','rider_assigned']
        fields = ['rider_assigned']


class DeliverOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['is_delivered']