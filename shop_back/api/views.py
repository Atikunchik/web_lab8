from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .models import Product, Category


def list_products(request):
    products = Product.objects.all()
    #products = dict(products)
    return HttpResponse(products)


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product = dict()
    return {'data': product}


def list_categories(request):
    categories = Category.objects.all()
    return {'data': categories}


def get_category(request, category_id):
    category = Category.objects.get(id=category_id)
    return {'data': category}