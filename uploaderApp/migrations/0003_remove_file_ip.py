# Generated by Django 4.0.6 on 2022-11-25 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploaderApp', '0002_file_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='ip',
        ),
    ]
