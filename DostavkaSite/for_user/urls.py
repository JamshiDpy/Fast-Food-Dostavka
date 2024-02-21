from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# router.register('users', views.BotUsersViewSet, basename='users')
# router.register('basket', views.BasketView, basename='basket')

urlpatterns = [
    path("users/", views.BotUserAPIView.as_view(), name="create"),
    path("users/<int:pk>/", views.BotUserAPIView.as_view(), name="update"),
    path("category-main-image/", views.CategoryImageView.as_view(), name="category-main-image"),
    path("category/<int:pk>/", views.CategoryView.as_view(), name="category"),
    path("categories/", views.CategoryView.as_view(), name="categories"),
    path("products/<int:pk>/", views.ProductView.as_view(), name="products"),
    path("product-detail/<int:pk>/", views.ProductDetailView.as_view(), name="product-detail"),
    path('add-basket/<int:user_id>/<int:product_id>/<int:qty>/', views.BasketView.as_view(), name='add-basket'),
    path('basket/<int:user_id>/', views.BasketView.as_view(), name='basket'),
    path("orders/<int:order_id>/", views.OrderView.as_view(), name='get-orders'),
    path("create-orders/<int:user_id>/<str:lat>/<str:long>/", views.OrderView.as_view(), name='create-orders'),
    path("create-orders/<int:user_id>/", views.OrderView2.as_view(), name='create-order-2',)
]
