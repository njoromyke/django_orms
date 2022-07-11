from django.shortcuts import render
from django.db import connection
from store.models import Collection, Order, OrderItem, Product


def say_hello(request):
    with connection.cursor() as cursor:
        cursor.callproc('get-customers', 1, 2, 3, 'a')

    return render(request, 'hello.html', {'name': 'Mosh', 'result': list(query_set)})
