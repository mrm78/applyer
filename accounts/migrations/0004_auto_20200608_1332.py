# Generated by Django 3.0.7 on 2020-06-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_order_transaction_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_no',
            field=models.CharField(max_length=30),
        ),
    ]
