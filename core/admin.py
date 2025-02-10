from django.contrib import admin
from .models import Product, Customer
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')

admin.site.register(Product,ProductAdmin)
admin.site.register(Customer,CustomerAdmin)  # Registering the Customer model
