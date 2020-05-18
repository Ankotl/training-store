

from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.ProductView.as_view()),
    path('filter/', views.FilterProductView.as_view(), name='filter'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('review/<slug:slug>/', views.AddReview.as_view(), name='add_review'),
    path('accounts/', include('django.contrib.auth.urls')),
    ]
