from django.shortcuts import render
from pages.models import MainScrollModel, ProductModel


def home_page_view(request):
    scrolls = MainScrollModel.objects.all().order_by('-pk')
    burgers = ProductModel.objects.filter(category__title__icontains="Burgers").order_by('-pk')
    pizzas = ProductModel.objects.filter(category__title__icontains="pizza").order_by('-pk')
    drinks = ProductModel.objects.filter(category__title__icontains="Drinks").order_by('-pk')
    fries = ProductModel.objects.filter(category__title__icontains="fr").order_by('-pk')
    salads = ProductModel.objects.filter(category__title__icontains="Salads").order_by('-pk')
    context = {
        'scrolls': scrolls,
        'burgers': burgers,
        'pizzas': pizzas,
        'drinks': drinks,
        'fries': fries,
        'salads': salads,
    }
    return render(request, 'index.html', context)