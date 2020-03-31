from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Product
# Create your views here.


class ProductView(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'products/products_list.html'


class ProductDetailView(DetailView):
    model = Product
    slug_field = "article"
    template_name = 'products/product_detail.html'

