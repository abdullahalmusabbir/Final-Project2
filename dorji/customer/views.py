from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def customer_detail(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    return render(request, 'customer_detail.html', {'customer': customer})

def customer_create(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'customer_form.html')

def customer_update(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'customer_form.html', {'customer': customer})

def customer_delete(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.method == 'POST':
        customer.delete()
        return HttpResponse('Customer deleted')
    return render(request, 'customer_confirm_delete.html', {'customer': customer})