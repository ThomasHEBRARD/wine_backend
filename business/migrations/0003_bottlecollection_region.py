# Generated by Django 3.0.7 on 2021-09-29 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_bottlecollection_winery'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottlecollection',
            name='region',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
