# Generated by Django 4.2.7 on 2023-11-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avto',
            name='price',
            field=models.IntegerField(default=10000),
        ),
    ]
