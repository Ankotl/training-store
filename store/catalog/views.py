from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Product, Category
from .forms import ReviewForm
# Create your views here.


class ArticleFilter:
    def get_article(self):
        return Product.objects.all().values('article')


class ProductView(ArticleFilter, ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'products/products_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        return context


class ProductDetailView(ArticleFilter, DetailView):
    model = Product
    slug_field = "article"
    template_name = 'products/product_detail.html'


class AddReview(View):
    def post(self, request, slug):
        form = ReviewForm(request.POST)
        product = Product.objects.get(article=slug)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())


class FilterProductView(ArticleFilter, ListView):
    template_name = 'products/products_list.html'

    def get_queryset(self):
        queryset = Product.objects.filter(article__in=self.request.GET.getlist('article'))
        return queryset
