from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=15, verbose_name='Foydalnuvchining ismi ', unique=True)
    email = models.EmailField(max_length=255, verbose_name='Email ', null=True, blank=True)
    phone = models.CharField(max_length=13, verbose_name='Telefon raqam ', null=True, blank=True, validators=[
    RegexValidator(
        regex='^[\+]9{2}8{1}[0-9]{9}$',
        message='Invalid phone number',
        code='invalid_number'
    ),])
    password = models.CharField(max_length=8, unique=True)
    first_name = models.CharField(max_length=15, verbose_name='Ismingiz ', blank=True, null=True)
    last_name = models.CharField(max_length=15, verbose_name='Familiyangiz ', null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=55, verbose_name='Category :')

    class Meta(AbstractUser.Meta):
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=55, verbose_name='Maxsulot nomi :')
    price = models.IntegerField(verbose_name='Maxshulot narxi :', default=0)
    discount = models.IntegerField(verbose_name='Chegirma narxi :', null=True, blank=True, default=0)
    brand = models.ForeignKey(to='Brand', on_delete=models.CASCADE)
    photo = models.ManyToManyField(to='Product_image', verbose_name='Maxsulotning rasmi :')
    video = models.FileField(upload_to='product_video/', verbose_name='Maxsulot videosi :', null=True, blank=True)
    xit = models.BooleanField(default=False, verbose_name='Xit tovar :')
    sub_category = models.ForeignKey(to='Sub_category', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True, verbose_name='Yaratilgan sana :')
    like = models.IntegerField(default=0)
    characteristic = models.TextField()
    new = models.BooleanField(default=False)

    class Meta(AbstractUser.Meta):
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=25, verbose_name='Brandining nomi :')
    photo = models.ImageField(upload_to='brand_photo/', verbose_name='Brandining rasmi')

    class Meta(AbstractUser.Meta):
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name


class Sub_category(models.Model):
    name = models.CharField(max_length=55, verbose_name='Maxsulotning sub categoriyasi :')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)

    class Meta(AbstractUser.Meta):
        verbose_name = 'Sub_category'
        verbose_name_plural = 'Sub_categories'

    def __str__(self):
        return self.name

class Saved(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Maxsuloti')

    class Meta(AbstractUser.Meta):
        verbose_name = 'Saved'
        verbose_name_plural = 'Saveds'

    def __str__(self):
        return self.product.name


class Product_image(models.Model):
    photo = models.ImageField(upload_to='product_image/', verbose_name='Maxsulot rasmi :')

    class Meta(AbstractUser.Meta):
        verbose_name = 'Product_image'
        verbose_name_plural = 'Product_images'


class Order(models.Model):
    region = models.ForeignKey(to='Region', on_delete=models.CASCADE)
    email = models.EmailField(max_length=25)
    product = models.ManyToManyField(to=Product, verbose_name='Maxsulot :')
    phone = models.CharField(max_length=13, unique=True, blank=False, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    user = models.ForeignKey(to=User, blank=False, verbose_name="Mijoz", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, verbose_name='Soni :')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.IntegerField(default=12, null=True, blank=True)
    dostavka = models.IntegerField(blank=False, verbose_name='Kuryer turi :', choices=
    (
        (1, 'Take away'),
        (2, 'Delivery')
    ))
    comment = models.TextField(verbose_name='Comment :')

    class Meta(AbstractUser.Meta):
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.user.name

class Region(models.Model):
    name = models.CharField(max_length=30, verbose_name='Addressning nomi :')

    class Meta(AbstractUser.Meta):
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name


class Card(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(to=Product)
    created_at = models.DateTimeField(auto_now=True)

    class Meta(AbstractUser.Meta):
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    def __str__(self):
        return self.user.username


class Saved(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Maxsuloti')

    class Meta(AbstractUser.Meta):
        verbose_name = 'Saved'
        verbose_name_plural = 'Saveds'

    def __str__(self):
        return self.product.name