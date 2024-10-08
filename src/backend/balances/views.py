from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from accounts.models import AccountMeter
from payments.models import ElectrictyCost, Payment
from balances.models import ElectricityBalance, ElectrictyBalanceLog, Token
from .forms import RechargeForm

# Create your views here.


@login_required(login_url='accounts:login')
def dashboardView(request):

    user = request.user

    meter_details = get_object_or_404(AccountMeter, account=user)

    current_balance = get_object_or_404(ElectricityBalance, meter_no=meter_details)

    form = RechargeForm()
    
    context = {
        'current_balance': current_balance,
        'meter_details': meter_details,
        'form': form,
    }
    return render(request, 'balances/main-dashboard.html', context)


@login_required(login_url='accounts:login')
def tokenHistoryView(request):

    user = request.user

    meter_details = get_object_or_404(AccountMeter, account=user)

    token_history = Token.objects.filter(meter_no=meter_details)

    context = {
        'token_history': token_history
    }
    return render(request, 'balances/history.html', context)


def anomalyDashboard(request):
    
    context = {
        
    }
    return render(request, 'balances/anomaly.html', context)


def rechargeElectricity(request):

    if request.method == 'POST':
        form = RechargeForm(request.POST)
        if form.is_valid():
            meter_number = form.cleaned_data['meter_number']
            amount = form.cleaned_data['amount']

            cost = ElectrictyCost.objects.first()

            total_units = int(amount)/cost.price_per_kwh

            # Payment details 
            payment = Payment.objects.create(
                user=request.user,
                full_name=request.user.first_name + request.user.last_name,
                email = 'admin@gmail.com',
                phone = request.user.phone_number,
                total_paid=amount,
                billing_status=True
            )

            meter = get_object_or_404(AccountMeter, account=request.user)

            token = Token.objects.create(
                payment=payment,
                meter_no=meter,
            )

            balance = ElectricityBalance.objects.get(meter_no=meter)

            balance.balance += int(total_units)

            balance.save()

            return redirect('balances:dashboard')

    return redirect('balances:dashboard') 
