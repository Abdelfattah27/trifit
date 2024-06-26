# Generated by Django 4.2.5 on 2024-05-04 22:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='contract_type',
            field=models.CharField(choices=[('monthly', 'شهري'), ('yearly', 'سنوي'), ('half-month', 'نصف شهري')], default='monthly', max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='contact',
            field=models.CharField(help_text='Enter 11-digit contact number', max_length=11),
        ),
        migrations.AlterField(
            model_name='member',
            name='expire_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 4, 1, 49, 55, 183571)),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='member',
            name='initial_amount',
            field=models.CharField(default='200', max_length=10),
        ),
    ]
