# Generated by Django 2.1.7 on 2019-04-29 20:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusBooking',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('service_id', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('From', models.CharField(default='', max_length=100)),
                ('To', models.CharField(default='', max_length=100)),
                ('TravelDate', models.DateField(default=django.utils.timezone.now, null=True)),
                ('booking_date', models.DateField(default=django.utils.timezone.now)),
                ('seats', models.IntegerField(default=0)),
                ('bill', models.IntegerField(default=0)),
            ],
        ),
    ]
