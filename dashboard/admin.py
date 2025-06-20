from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group

admin.site.site_header = 'Timeless Dashboard'
list_display = ('name', 'Quantity')
# Register your models here.
admin.site.register(Product)

# admin.site.unregister(Group)