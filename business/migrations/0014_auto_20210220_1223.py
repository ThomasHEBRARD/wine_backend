# Generated by Django 3.0.7 on 2021-02-20 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0013_auto_20210220_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottle',
            name='code',
        ),
        migrations.RemoveField(
            model_name='bottle',
            name='name',
        ),
    ]
