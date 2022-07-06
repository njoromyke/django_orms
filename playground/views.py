from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Value, F, Func
from django.db.models.functions import Concat
from store.models import Customer, Product


def say_hello(request):
    query_set = Customer.objects.annotate(
        full_name=Func(F('first_name'), Value(" "), F('last_name'), function='CONCAT'))

    query_set = Customer.objects.annotate(
        full_name=Concat('first_name', Value(' '), 'last_name'))

    return render(request, 'hello.html', {'name': 'Mosh', 'result': query_set})
