# Generated by Django 5.1.1 on 2024-09-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_alter_payment_order_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order_key',
            field=models.CharField(default='3a72f7be89d7422c9b82d40dad27b4', max_length=200),
        ),
    ]
