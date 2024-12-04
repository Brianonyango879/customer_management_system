from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Order
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customers' : customers})
@login_required(login_url='login')
def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, 'customer/customer_detail.html', {'customer': customer})
@login_required(login_url='login')
def customer_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        Customer.objects.create(name=name, email=email, phone=phone, address=address)
        return redirect('customer_list')
    return render(request, 'customer/customer_form.html')
@login_required(login_url='login')
def customer_edit(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.email = request.POST.get('email')
        customer.phone = request.POST.get('phone')
        customer.address = request.POST.get('address')
        customer.save()
        return redirect('customer_list')
    return render(request, 'customer/customer_form.html', {'customer':customer})
@login_required(login_url='login')
def customer_delete(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.delete()
    return redirect('customer_list')
@login_required(login_url='login')
def order_list(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    orders = customer.orders.all()
    return render(request, 'customer/order_list.html', {'customer': customer, 'orders': orders})
@login_required(login_url='login')
def order_form(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        product = request.POST['product']
        quantity = request.POST['quantity']
        price = request.POST['price']
        Order.objects.create(customer=customer, product=product, quantity=quantity, price=price)
        return redirect('order_list', customer_id=customer.id)
    return render(request, 'customer/order_form.html', {'customer': customer})

@login_required(login_url='login')
def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        order.product = request.POST['product']
        order.quantity = request.POST['quantity']
        order.price = request.POST['price']
        order.order_status = request.POST['order_status']
        order.save()
        return redirect('order_list', customer_id=order.customer.id)  # Redirect to the customer's order list

    return render(request, 'customer/edit_order.html', {'order': order})

@login_required(login_url='login')
def dashboard(request):
    # Query all customers and orders
    customers = Customer.objects.all()
    total_orders = Order.objects.count()
    orders_completed = Order.objects.filter(order_status="Completed").count()
    orders_pending = Order.objects.filter(order_status="Pending").count()

    # Slice only AFTER filtering/sorting
    recent_orders = Order.objects.all().order_by('-id')[:5]  # Last 5 orders

    # Pass the context to the template
    context = {
        'total_orders': total_orders,
        'orders_completed': orders_completed,
        'orders_pending': orders_pending,
        'customer_count': customers.count(),
        'customers': customers,
        'orders': recent_orders,
    }
    return render(request, 'customer/dashboard.html', context)
