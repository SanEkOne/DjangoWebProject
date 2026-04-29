from django.shortcuts import render 
import requests


def main_page(request):
    return render(request, 'main.html')


def news_page(request):
    return render(request, 'news.html')


def management_page(request):
    return render(request, 'management.html')

def about_page(request):
    return render(request, 'about.html')    

def contacts_page(request):
    return render(request, 'contacts.html')