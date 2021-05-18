from django.forms import ModelForm
from .models import Rider
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateRiderForm(ModelForm):
    class Meta:
        model = Rider
        fields = ['first_name', 'middle_name', 'last_name', 'contact_number', 'address', 'vehicle_number', 'rider_img']
