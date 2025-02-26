from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Product

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import Product

@csrf_exempt  # ❌ Disable CSRF (only for testing)
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        if name and price:
            Product.objects.create(name=name, price=price)
            return redirect('/')
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})



def about(request):
    return render(request, 'about.html')
