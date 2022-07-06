from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Value,F
from store.models import Customer, Product


def say_hello(request):
    query_set = Customer.objects.annotate(new_id=F('id'))

    return render(request, 'hello.html', {'name': 'Mosh', 'result': query_set})
