from .models import Order, Car
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def place_order(request, car_id):
    car = Car.objects.get(id=car_id)
    Order.objects.create(user=request.user, car=car)
    car.quantity -= 1  # Assuming each order reduces the quantity by 1
    car.save()
    return redirect('order_history')


def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})
