# Generated by Django 3.1.5 on 2021-02-16 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rider', '0005_auto_20210129_1310'),
        ('order', '0005_auto_20210210_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='rider_assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rider.rider'),
        ),
    ]
