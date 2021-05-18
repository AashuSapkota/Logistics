from django.shortcuts import render, redirect
from .forms import CreateOrderForm, AssignRiderForm, DeliverOrderForm
from .models import Order
from datetime import datetime
import csv
from django.contrib.auth.models import User
from vendor.models import Vendor
from account.decorators import allowed_users



@allowed_users(allowed_roles=['vendor'])
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            user_email = request.user.email
            vendor = Vendor.objects.only('id').get(vendor_email=user_email).id

            return redirect('order_list')
    else:
        form = CreateOrderForm

    context = {'form': form}
    template = 'order/create_order.html'
    return render(request, template, context)


def order_list(request):
    order_list = Order.objects.all()
    context = {'order_list': order_list}
    template = 'order/order_list.html'
    return render(request, template, context)


def edit_order(request, pk):
    order = Order.objects.get(id=pk)
    form = CreateOrderForm(instance=order)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    context = {'form': form}
    template = 'order/create_order.html'
    return render(request, template, context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    template = 'order/order_delete.html'
    context = {'order': order}
    return render(request, template, context)


def assign_rider(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        form = AssignRiderForm(request.POST, instance=order)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.is_rider_assigned = True
            obj.rider_assigned_datetime = datetime.now()
            obj.save()
            return redirect('order_list')
    else:
        form = AssignRiderForm

    context = {'form': form}
    template = 'order/assign_rider.html'
    return render(request, template, context)


def deliver_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        form = DeliverOrderForm(request.POST, instance=order)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.delivered_datetime = datetime.now()
            obj.save()
            return redirect('order_list')
    else:
        form = DeliverOrderForm

    context = {'form': form}
    template = 'order/deliver_order.html'
    return render(request, template, context)


def order_detail(request, pk):
    order_details = Order.objects.get(id=pk)
    context = {'order_details': order_details}
    template = 'order/order_details.html'
    return render(request, template, context)
