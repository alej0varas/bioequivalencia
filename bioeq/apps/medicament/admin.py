from django.contrib import admin

from .models import Holder, MedicinalIngredient, Product, Treatment

admin.site.register(Holder)
admin.site.register(Product)
admin.site.register(MedicinalIngredient)
admin.site.register(Treatment)
