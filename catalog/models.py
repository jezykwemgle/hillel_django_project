from django.db import models
from django.core.validators import RegexValidator

class City(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postcode = models.IntegerField()

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    vendor_code = models.CharField(max_length=255)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_name}\n{self.description}'

class Client(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.name} {self.surname} {self.email}'

class Supplier(models.Model):
    title = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    city = models.OneToOneField(City, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title} ({self.city})'

