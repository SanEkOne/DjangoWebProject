from django.shortcuts import render, redirect
import requests
from .models import ProductApplication
from .forms import ProductForm
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


@api_view(['GET'])
def products_list(request):
    products = ProductApplication.objects.all()     #/api/products/
    data = [{ 
        'id': a.id,
        'title': a.title,
        'price': a.price,
        'description': a.description,
        'image': a.image.url if a.image else None,
    } for a in products]
    return Response(data) 