from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Max, Avg, Min, Sum, Count
from store.models import Product


def say_hello(request):
    result = Product.objects.aggregate(count=Count('id'))

    return render(request, 'hello.html', {'name': 'Mosh', 'result': result})
