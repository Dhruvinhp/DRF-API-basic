# Generated by Django 3.2.5 on 2021-09-13 08:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
