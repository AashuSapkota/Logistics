from django.db import models


class Rider(models.Model):
    first_name = models.CharField(max_length=20, null=False, blank=False)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    contact_number = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)
    vehicle_number = models.CharField(max_length=15, null=False, blank=False)
    rider_img = models.ImageField(upload_to='media', null=True, blank=True)

    class Meta:
        verbose_name = 'Rider'
        verbose_name_plural = 'Riders'

    def __str__(self):
        return self.first_name + " " + self.last_name
