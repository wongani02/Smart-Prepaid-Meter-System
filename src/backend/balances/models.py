
from django.db import models

from payments.models import Payment
from accounts.models import AccountMeter

# Create your models here.

class Token(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT, related_name='token_payment')

    meter_no = models.ForeignKey(AccountMeter, on_delete=models.CASCADE, null=True)
    token = models.PositiveIntegerField(unique=True)

    is_used = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.token)
    

class ElectricityBalance(models.Model):
    meter_no = models.OneToOneField(AccountMeter, on_delete=models.CASCADE, null=True, related_name='meter_balance')
    balance = models.FloatField(null=True, default=0)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.balance)
    

class ElectrictyBalanceLog(models.Model):
    meter_no = models.ForeignKey(AccountMeter, on_delete=models.CASCADE, null=True)
    balance = models.FloatField(null=True)
    current_usage = models.FloatField(null=True)
    voltage_usage = models.FloatField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.balance)
