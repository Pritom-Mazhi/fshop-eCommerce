# Generated by Django 2.1.7 on 2019-03-24 11:27

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_update_email_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
