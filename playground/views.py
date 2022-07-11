from django.shortcuts import render
from django.db import transaction
from store.models import Collection, Order, OrderItem, Product


def say_hello(request):

    # ...
    with transaction.atomic():

        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = -1
        item.quantity = 200
        item.unit_price = 1000

    return render(request, 'hello.html', {'name': 'Mosh'})
