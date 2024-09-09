from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from accounts.models import AccountMeter
from balances.models import ElectricityBalance, ElectrictyBalanceLog, Token

# Create your views here.


@login_required(login_url='')
def dashboardView(request):

    user = request.user

    meter_details = get_object_or_404(AccountMeter, account=user)

    current_balance = get_object_or_404(ElectricityBalance, meter_no=meter_details)
    
    context = {
        'current_balance': current_balance,
        'meter_details': meter_details
    }
    return render(request, 'balances/main-dashboard.html', context)


@login_required(login_url='')
def tokenHistoryView(request):

    user = request.user

    meter_details = get_object_or_404(AccountMeter, user=user)

    token_history = Token.objects.filter(meter_no=meter_details)

    context = {
        'token_history': token_history
    }
    return render(request, 'balances/main-dashboard.html', context)

