# Generated by Django 3.2 on 2021-04-15 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storedb', '0008_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='cust_id',
        ),
    ]
