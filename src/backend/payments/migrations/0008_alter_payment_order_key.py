# Generated by Django 5.1.1 on 2024-10-02 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_alter_payment_order_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order_key',
            field=models.CharField(default='0b5a28126d6e4f008a2eaddbaf5841', max_length=200),
        ),
    ]
