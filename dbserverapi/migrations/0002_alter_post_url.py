# Generated by Django 5.0.1 on 2024-01-31 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbserverapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
