from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.contrib import admin


class City(models.Model):
    """Model representing a city"""

    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postcode = models.CharField(max_length=20, help_text="Enter the postcode of the city")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular city."""
        return reverse('city-detail', args=[str(self.id)])


class Supplier(models.Model):
    """Model representing a supplier"""

    code = models.CharField(max_length=10, help_text='Enter the vendor`s or producer`s identifier')
    title = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    city = models.OneToOneField(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return f'{self.title} ({self.city})'

    def get_absolute_url(self):
        """Returns the url to access a particular supplier."""
        return reverse('supplier-detail', args=[str(self.id)])


class Product(models.Model):
    """Model representing a product"""

    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['product_name', 'price']

    def __str__(self):
        return f'{self.product_name}\n{self.description}'

    def get_absolute_url(self):
        """Returns the url to access a particular product."""
        return reverse('product-detail', args=[str(self.id)])


class Client(models.Model):
    """Model representing a client"""

    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return f'{self.name} {self.surname} {self.email}'

    def get_absolute_url(self):
        """Returns the url to access a particular client."""
        return reverse('client-detail', args=[str(self.id)])

    @admin.display(description='')
    def get_products(self):
        return ", ".join([p.product_name for p in self.products.all()])

