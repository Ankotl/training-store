from django.contrib import admin
from .models import Product, Category, Reviews, RatingStar, Rating
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Reviews)
admin.site.register(RatingStar)
admin.site.register(Rating)
