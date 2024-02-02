from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Anjali'})

def new(request):
    return HttpResponse('New Products')

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})