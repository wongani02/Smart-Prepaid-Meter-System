from django import forms


class RechargeForm(forms.Form):
    meter_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-input mt-1.5 h-9 w-full rounded-lg border border-slate-300 bg-transparent px-3 py-2 placeholder:text-slate-400/70 hover:border-slate-400 focus:border-primary dark:border-navy-450 dark:hover:border-navy-400 dark:focus:border-accent'}
        )
    )
    amount = forms.CharField(
        widget=forms.NumberInput(
            attrs={'class': 'form-input w-full rounded-r-lg border border-slate-300 bg-transparent px-3 py-2 placeholder:text-slate-400/70 hover:z-10 hover:border-slate-400 focus:z-10 focus:border-primary dark:border-navy-450 dark:hover:border-navy-400 dark:focus:border-accent'}
        )
    )

    