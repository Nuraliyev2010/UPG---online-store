from rest_framework import serializers
from . import models

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = "__all__"


class Sub_categorySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Sub_category
        fields = "__all__"


class SevedSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Saved
        fields = "__all__"


class Product_imageSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Product_image
        fields = "__all__"


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'


class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Card
        fields = '__all__'