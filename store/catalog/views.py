from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Product, Category
from .forms import ReviewForm, RatingForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        return context


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


class AddStarRating(View):
    """Добавление рейтинга фильму"""
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                product_id=int(request.POST.get("product")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)