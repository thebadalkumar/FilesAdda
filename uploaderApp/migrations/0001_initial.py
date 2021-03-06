# Generated by Django 4.0.6 on 2022-07-10 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uploaderApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=uploaderApp.models.custom_path)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('desc', models.CharField(blank=True, max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(blank=True, max_length=15, unique=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('is_fav', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
