from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateRiderForm
from .models import Rider
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
import csv
from account.decorators import allowed_users


@allowed_users(allowed_roles=['rider'])
def create_rider(request):
    if request.method == 'POST':
        form = CreateRiderForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            rider_email = obj.email
            user = User.objects.filter(email=rider_email).count()
            if user == 1:
                obj.save()
                return redirect('rider_list')
            else:
                return HttpResponse('Rider is not registered')
    else:
        form = CreateRiderForm

    context = {'form': form}
    template = 'rider/create_rider.html'
    return render(request, template, context)


def rider_list(request):
    rider_list = Rider.objects.all()
    context = {'rider_list': rider_list}
    template = 'rider/rider_list.html'
    return render(request, template, context)


def rider_detail(request, pk):
    rider_detail = Rider.objects.get(id=pk)
    context = {'rider_detail': rider_detail}
    template = 'rider/rider_detail.html'
    return render(request, template, context)


def edit_rider(request, pk):
    rider = Rider.objects.get(id=pk)
    form = CreateRiderForm(instance=rider)
    if request.method == 'POST':
        form = CreateRiderForm(request.POST, request.FILES, instance=rider)
        if form.is_valid():
            form.save()
            return redirect('rider_list')
    context = {'form': form}
    template = 'rider/create_rider.html'
    return render(request, template, context)


def delete_rider(request, pk):
    rider = Rider.objects.get(id=pk)
    if request.method == 'POST':
        rider.delete()
        return redirect('rider_list')
    template = 'rider/rider_delete.html'
    context = {'rider': rider}
    return render(request, template, context)


def export_riders_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="riders.csv"'
    writer = csv.writer(response)
    writer.writerow(['First Name', 'Middle Name', 'Last Name', 'Contact Number', 'Address', 'Vehicle Number'])

    riders = Rider.objects.all().values_list('first_name', 'middle_name', 'last_name', 'contact_number', 'address',
                                             'vehicle_number')
    for rider in riders:
        writer.writerow(rider)
    return response
