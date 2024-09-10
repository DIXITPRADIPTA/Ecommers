# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomerLoginForm, SellerLoginForm

def customer_login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('customer_dashboard')  # Replace with the customer dashboard URL
        else:
            messages.error(request, "Invalid login credentials")
    else:
        form = CustomerLoginForm()
    return render(request, 'SnapTrad/customer_login.html', {'form': form})

def seller_login(request):
    if request.method == 'POST':
        form = SellerLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('seller_dashboard')  # Replace with the seller dashboard URL
        else:
            messages.error(request, "Invalid login credentials")
    else:
        form = SellerLoginForm()
    return render(request, 'SnapTrad/seller_login.html', {'form': form})


def home(request):
    return render(request, 'SnapTrad/home.html')

