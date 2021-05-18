from django.forms import ModelForm
from .models import Vendor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateVendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor_name', 'vendor_address', 'vendor_contact', 'vendor_contact_person',
                  'vendor_contact_person_number','vendor_email', 'vendor_img']
