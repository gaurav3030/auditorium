# Generated by Django 2.2.5 on 2019-09-24 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksite', '0006_auto_20190924_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='approve',
            field=models.CharField(choices=[('Not Approved', 'Not Approved'), ('Approved', 'Approved')], default='Not Approved', max_length=100),
        ),
    ]
