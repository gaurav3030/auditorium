# Generated by Django 2.2.5 on 2019-09-24 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksite', '0003_auto_20190923_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='college',
            field=models.CharField(choices=[('VES College of Architecture', 'VES College of Architecture'), ('VES Institute of Technology', 'VES Institute of Technology'), ('VES College of Pharmacy', 'VES College of Pharmacy'), ('VES College of Law', 'VES College of Law'), ('VES Institute of Management', 'VES Institute of Management')], max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('FULL DAY', 'FULL DAY'), ('FIRST HALF', 'FIRST HALF'), ('SECOND HALF', 'SECOND HALF')], max_length=100),
        ),
    ]
