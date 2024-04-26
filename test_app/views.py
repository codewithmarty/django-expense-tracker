from django.shortcuts import render, redirect
from .models import Expense

def index(request):
    expenses = Expense.objects.all()
    return render(request, 'index.html', { 'expenses': expenses })

def add_expense(request):
    Expense.objects.create(
        name=request.POST.get("expense_name"),
        amount=request.POST.get("expense_amount"),
        date=request.POST.get("expense_date"),
    )
    return redirect('/')