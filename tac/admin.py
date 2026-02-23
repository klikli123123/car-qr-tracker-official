from django.contrib import admin
from .models import Adres, ProductVariant, Bestelling, Levering

admin.site.register(Adres)
admin.site.register(ProductVariant)
admin.site.register(Bestelling)
admin.site.register(Levering)
from .models import Werknemer, Klant, Product

admin.site.register(Werknemer)
admin.site.register(Klant)
admin.site.register(Product)
from django.contrib import admin

# Register your models here.
