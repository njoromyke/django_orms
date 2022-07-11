from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Product
from tags.models import TaggedItem


def say_hello(request):
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(pk=1)
    collection.save()
    

    return render(request, 'hello.html', {'name': 'Mosh', 'tags': list(query_set)})
