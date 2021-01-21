from django.shortcuts import render, redirect
from .forms import AccountForm, TransactionForm

# Create your views here.
def home(request):
    return render(request, 'checkbook/index.html')

def create_account(request):
    form = AccountForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    content = {'form': form}
    return render(request, 'checkbook/CreateNewAccount.html', content)

def balance(request):
    return render(request, 'checkbook/BalanceSheet.html')

def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
