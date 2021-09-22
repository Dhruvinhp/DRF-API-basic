# Generated by Django 3.2.5 on 2021-09-17 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_basic', '0005_remove_article_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article', to=settings.AUTH_USER_MODEL),
        ),
    ]
