# Generated by Django 5.1.1 on 2024-09-10 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balances', '0003_alter_electrictybalancelog_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='electrictybalancelog',
            name='apparent_power',
            field=models.FloatField(null=True),
        ),
    ]