# Generated by Django 5.0 on 2024-02-08 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essential_events_main', '0004_alter_staticmodel_statictype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticmodel',
            name='image',
            field=models.ImageField(upload_to='staticModel'),
        ),
    ]
