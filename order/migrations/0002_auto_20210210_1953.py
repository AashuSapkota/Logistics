# Generated by Django 3.1.5 on 2021-02-10 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='rider_assigned_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
