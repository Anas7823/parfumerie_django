from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import store

# Create your views here.

def store_list(request):
    context = {}
    products = store.objects.all()
    context['products'] = products
    return render(request, 'store_list.html', context)

def view_product(request):
    # Récupérer le produit correspondant à l'ID
    product_id = request.GET.get('id')
    product = get_object_or_404(store, id=product_id)

    # Vérifier le stock
    in_stock = product.stock > 0

    # Passer les informations au template
    context = {
        'product': product,
        'in_stock': in_stock,
    }
    return render(request, 'view_product.html', context)