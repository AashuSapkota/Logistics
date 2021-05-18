from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateVendorForm
from django.contrib.auth.models import Group
from .models import Vendor
from django.contrib import messages
from django.contrib.auth.models import User
import csv
from account.decorators import allowed_users



def create_vendor(request):
    if request.method == 'POST':
        form = CreateVendorForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            vendor_email = obj.vendor_email
            user = User.objects.filter(email=vendor_email).count()
            if user == 1:
                obj.save()
                return redirect('vendor_list')
            else:
                return HttpResponse('Vendor is not registered')
    else:
        form = CreateVendorForm

    context = {'form': form}
    template = 'vendor/create_vendor.html'
    return render(request, template, context)


def vendor_list(request):
    vendor_list = Vendor.objects.all()
    context = {'vendor_list': vendor_list}
    template = 'vendor/vendor_list.html'
    return render(request, template, context)


def vendor_detail(request, pk):
    vendor_detail = Vendor.objects.get(id=pk)
    context = {'vendor_detail': vendor_detail}
    template = 'vendor/vendor_detail.html'
    return render(request, template, context)


def edit_vendor(request, pk):
    vendor = Vendor.objects.get(id=pk)
    form = CreateVendorForm(instance=vendor)
    if request.method == 'POST':
        form = CreateVendorForm(request.POST, request.FILES, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    context = {'form': form}
    template = 'vendor/create_vendor.html'
    return render(request, template, context)


def delete_vendor(request, pk):
    vendor = Vendor.objects.get(id=pk)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendor_list')
    template = 'vendor/vendor_delete.html'
    context = {'vendor': vendor}
    return render(request, template, context)


def export_vendors_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="vendors.csv"'
    writer = csv.writer(response)
    writer.writerow(['Vendor Name', 'Address', 'Contact Number', 'Contact Person', 'Contact Person Number'])

    vendors = Vendor.objects.all().values_list('vendor_name', 'vendor_address', 'vendor_contact',
                                               'vendor_contact_person', 'vendor_contact_person_number')
    for vendor in vendors:
        writer.writerow(vendor)
    return response
