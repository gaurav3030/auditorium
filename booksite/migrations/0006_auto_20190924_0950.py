# Generated by Django 2.2.5 on 2019-09-24 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksite', '0005_auto_20190924_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('First Half', 'First Half'), ('Second Half', 'Second Half'), ('Full Day', 'Full Day')], max_length=100),
        ),
    ]
