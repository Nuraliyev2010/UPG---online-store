from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView


@api_view(["GET"])
def get_subcategories_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    subcategories = Sub_category.objects.filter(category=category)
    ser = Sub_categorySerializers(subcategories, many=True)
    return Response(ser.data)

@api_view(['GET'])
def search_product_by_name(request):
    name = request.GET.get('name')
    product = Product.objects.filter(name__icontains=name)
    ser = ProductSerializers(product, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_category(request):
    name = request.GET.get('name')
    category = Category.objects.filter(name=name)
    ser = CategorySerializers(category, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_price(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price is not None and max_price is not None:
        queryset = Product.objects.filter(price__gte=min_price, price__lte=max_price)
        serializer = CategorySerializers(queryset, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': '"min_price" va "max_price" barchasi ham berilishi shart'}, status=400)


@api_view(['POST'])
def add_product_card(request, pk):
    product = Product.objects.get(pk=pk)
    users = request.user
    card = Card.objects.create(
        products = product,
    )
    cards = []
    cards.append(user)
    for u in users:
        card.emails_for_help.set(u)
    cards.append(card)
    ser = CardSerializer(card)
    return Response(ser.data)


@api_view(['POST'])
def product_saved(request, pk):
    product = Product.objects.get(pk=pk)

    save = Saved.objects.create(
        user=request.user,
        product=product
    )
    ser = SevedSerializers(save, many=True)
    return Response(ser.data)


@api_view(['PUT'])
def update_products_like(request, pk):
    product = Product.objects.get(pk=pk)
    product.like_number += 1
    product.save()
    ser = ProductSerializers(product)
    return Response(ser.data)