from django.db import models
from rider.models import Rider
from vendor.models import Vendor


class Order(models.Model):
    product_name = models.CharField(max_length=50, null=False, blank=False)
    product_img = models.ImageField(upload_to='media/orders', null=True, blank=True)
    receiver_name = models.CharField(max_length=50, null=False, blank=False)
    receiver_number = models.CharField(max_length=15, null=False, blank=False)
    receiver_address = models.CharField(max_length=50, null=False, blank=False)
    receiver_alternate_number = models.CharField(max_length=15, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=False, blank=False)
    is_rider_assigned = models.BooleanField(default=False, null=False, blank=False)
    rider_assigned = models.ForeignKey(Rider, on_delete=models.CASCADE, null=True, blank=True)
    rider_assigned_datetime = models.DateTimeField(null=True, blank=True)
    is_delivered = models.BooleanField(default=False, null=False, blank=False,)
    delivered_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.product_name
