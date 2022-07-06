from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Value, F, Func
from store.models import Customer, Product


def say_hello(request):
    query_set = Customer.objects.annotate(
        full_name=Func(F('first_name'), Value(" "), F('last_name'),function='CONCAT'))

    return render(request, 'hello.html', {'name': 'Mosh', 'result': query_set})
 