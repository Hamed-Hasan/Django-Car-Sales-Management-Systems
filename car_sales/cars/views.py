from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Brand
from .forms import CommentForm

def home(request):
    brand_query = request.GET.get('brand')
    if brand_query:
        cars = Car.objects.filter(brand__name=brand_query)
    else:
        cars = Car.objects.all()
    brands = Brand.objects.all()
    return render(request, 'cars/home.html', {'cars': cars, 'brands': brands})

def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    comments = car.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
            return redirect('car_detail', car_id=car_id)
    else:
        comment_form = CommentForm()

    return render(request, 'cars/car_detail.html', {
        'car': car,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })