from django.urls import path

from . import views

urlpatterns = [
    path('search_product_by_name/', views.search_product_by_name, name='search_product_by_name'),
    path('get_subcategories_by_category/<int:pk>/', views.get_subcategories_by_category, name='get_subcategories_by_category'),
    path('filter_category/', views.filter_category, name='filter_category'),
    path('filter_price/', views.filter_price, name='filter_price'),
    path('add_product_card/<int:pk>/', views.add_product_card, name='add_product_card'),
    # path('saveproductview/<int:pk>/', views.SaveProductView.as_view(), name='SaveProductView'),
    # path('createsaved1/<int:pk>/', views.CreateSaved1.as_view(), name='CreateSaved1'),
    path('product_saved/<int:pk>/', views.product_saved, name='product_saved'),
]