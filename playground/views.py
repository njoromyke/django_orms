from django.shortcuts import render
from django.db import transaction
from store.models import Collection, Order, OrderItem, Product


def say_hello(request):
    query_set = Product.objects.raw('SELECT id,title FROM store_product')
    return render(request, 'hello.html', {'name': 'Mosh', 'result': list(query_set)})
