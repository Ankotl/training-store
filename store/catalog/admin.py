from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Category, Reviews, RatingStar, Rating
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("id", "name")
    list_display_links = ("name",)


class ReviewInline(admin.TabularInline):
    """Отзывы на странице фильма"""
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("name", "email", "parent", "product", "id")
    readonly_fields = ("name", "email")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("product", "ip")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Товары"""
    list_display = ("name", "category", "article", "get_image")
    list_filter = ("category",)
    search_fields = ("name", "category__name")
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="75" height="75"')

    get_image.short_description = "Фото"


admin.site.register(RatingStar)

admin.site.site_title = "Web Store"
admin.site.site_header = "Web Store"