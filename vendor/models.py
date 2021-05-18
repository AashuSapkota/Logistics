from django.db import models



class Vendor(models.Model):
    vendor_name = models.CharField(max_length=50, null=False, blank=False)
    vendor_address = models.CharField(max_length=50, null=False, blank=False)
    vendor_contact = models.CharField(max_length=15, null=False, blank=False)
    vendor_contact_person = models.CharField(max_length=50, null=False, blank=False)
    vendor_contact_person_number = models.CharField(max_length=15, null=False, blank=False)
    vendor_email = models.EmailField(null=False, blank=False)
    vendor_img = models.ImageField(upload_to='media/vendors', null=True, blank=True)

    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    def __str__(self):
        return self.vendor_name
