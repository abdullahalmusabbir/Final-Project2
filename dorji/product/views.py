from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'product_form.html')

def product_update(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'product_form.html', {'product': product})

def product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return HttpResponse('Product deleted')
    return render(request, 'product_confirm_delete.html', {'product': product})