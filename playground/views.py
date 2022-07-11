from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


def say_hello(request):
    query_set = Product.objects.all()
    list(query_set)
    list(query_set)

    return render(request, 'hello.html', {'name': 'Mosh', 'tags': list(query_set)})
