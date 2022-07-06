from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Max, Avg, Min, Sum, Count
from store.models import Product


def say_hello(request):
    result = Product.objects.filter('collection__id').aggregate(count=Count('id'),min_price =Min('unit_price'))

    return render(request, 'hello.html', {'name': 'Mosh', 'result': result})
