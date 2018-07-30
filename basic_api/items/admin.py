from django import forms

from django.contrib import admin

from items import models
# Register your models here.


class ItemAdminForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = "__all__"

    def clean_code(self):
        code = self.cleaned_data['code'].upper()
        if models.Item.objects.filter(code=code).exists():
            raise forms.ValidationError("This code already exist.")
        return code

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        if models.Item.objects.filter(name=name).exists():
            raise forms.ValidationError("This name already exist.")
        return name


class ItemAdmin(admin.ModelAdmin):
    search_fields = ['code', 'name']
    list_filter = ('active',)
    list_display = ('code', 'name', 'active')
    readonly_fields = ('created',)
    form = ItemAdminForm


admin.site.register(models.Item, ItemAdmin)
