# Generated by Django 3.1.5 on 2021-01-29 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rider', '0004_rider_rider_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rider',
            name='rider_img',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
