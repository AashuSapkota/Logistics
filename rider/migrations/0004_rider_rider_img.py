# Generated by Django 3.1.5 on 2021-01-29 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rider', '0003_remove_rider_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='rider',
            name='rider_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
