from django.shortcuts import render
from django.http import HttpResponse
from .models import Order

# Create your views here.
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order/order_detail.html', {'order': order})

def order_create(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    else:
        return render(request, 'order/order_form.html')

def order_update(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        # Handle form submission
        pass
    else:
        return render(request, 'order/order_form.html', {'order': order})

def order_delete(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return HttpResponse('Order deleted')
    else:
        return render(request, 'order/order_confirm_delete.html', {'order': order})