from django.shortcuts import render
from django.views.generic.base import View

from .models import Product
# Create your views here.


class ProductView(View):
    def get(self,request):
        products = Product.objects.all()
        return render(request, 'products/products_list.html', {'product_list': products})


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        return render(request, 'products/product_detail.html', {"product": product})
