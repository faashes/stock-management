# Generated by Django 3.2 on 2021-04-27 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storedb', '0014_auto_20210426_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inv_buff',
            name='inv_no',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='inv_no',
            field=models.CharField(max_length=15),
        ),
    ]
