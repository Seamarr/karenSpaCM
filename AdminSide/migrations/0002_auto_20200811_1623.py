# Generated by Django 3.1 on 2020-08-11 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='asolea',
            field=models.CharField(choices=[('Yes', 'Sii'), ('Noo', 'No')], default='Noo', max_length=3),
        ),
    ]
