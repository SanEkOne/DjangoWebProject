from django.shortcuts import render, redirect
import requests
from .models import ProductApplication
from .forms import ProductForm
from django.contrib import messages

def index(request):
    products = ProductApplication.objects.all()

    return render(request, 'Store/index.html', {'products': products})

def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save()
            messages.success(request, 'Продукт успешно добавлен!')
            return redirect('store:index')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')

    else:
        form = ProductForm()

    return render(request, 'Store/product_form.html', {'form': form})