# Generated by Django 3.1.5 on 2021-02-10 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rider', '0005_auto_20210129_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_img', models.ImageField(blank=True, null=True, upload_to='media/orders')),
                ('receiver_name', models.CharField(max_length=50)),
                ('receiver_number', models.CharField(max_length=15)),
                ('receiver_address', models.CharField(max_length=50)),
                ('receiver_alternate_number', models.CharField(blank=True, max_length=15, null=True)),
                ('is_rider_assigned', models.BooleanField(default=False)),
                ('rider_assigned_datetime', models.DateTimeField(default='-')),
                ('is_delivered', models.BooleanField(default=False)),
                ('delivered_datetime', models.DateTimeField(default='-')),
                ('rider_assigned', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rider.rider')),
            ],
        ),
    ]
