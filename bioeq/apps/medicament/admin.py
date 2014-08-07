from django.contrib import admin
from django import forms

from .models import Holder, MedicinalIngredient, Product, Treatment

class TreatmentForm(forms.ModelForm):

    class Meta:
        model = Treatment

    medicinal_ingredients = forms.ModelMultipleChoiceField(queryset=MedicinalIngredient.objects.all())

    def __init__(self, *args, **kwargs):
        super(TreatmentForm, self).__init__(*args, **kwargs)

        if self.instance:
            self.fields['medicinal_ingredients'].initial = MedicinalIngredient.objects.filter(treatment=self.instance)

    def save(self, *args, **kwargs):
        # FIXME: 'commit' argument is not handled
        # TODO: Wrap reassignments into transaction
        instance = super(TreatmentForm, self).save(commit=False)
        self.fields['medicinal_ingredients'].initial.update(treatment=None)
        self.cleaned_data['medicinal_ingredients'].update(treatment=instance)
        return instance

class TreatmentAdmin (admin.ModelAdmin):
    form = TreatmentForm

admin.site.register(Holder)
admin.site.register(Product)
admin.site.register(MedicinalIngredient)
admin.site.register(Treatment, TreatmentAdmin)
