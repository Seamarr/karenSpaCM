# Generated by Django 3.1 on 2020-08-11 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0002_auto_20200811_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='asolea',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='No', max_length=3),
        ),
    ]
