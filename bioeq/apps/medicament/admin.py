from django.contrib import admin

from .models import Holder, MedicinalIngredient, Product, Treatment

class MedicantIngredientInline (admin.StackedInline):
	model = MedicinalIngredient

class TreatmentAdmin (admin.ModelAdmin):
	inlines = (MedicantIngredientInline, )

admin.site.register(Holder)
admin.site.register(Product)
admin.site.register(MedicinalIngredient)
admin.site.register(Treatment, TreatmentAdmin)
