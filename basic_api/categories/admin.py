from django import forms

from django.contrib import admin

from . import models
# Register your models here.


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        if models.Category.objects.filter(name=name).exists():
            raise forms.ValidationError("This name already exist.")
        return name


# class ItemsCategoryInline(admin.TabularInline):
#     model = models.ItemsCategory
#     extra = 0

#     def has_delete_permission(self, request, obj=None):
#         return True


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ('active',)
    list_display = ('name', 'active')
    form = CategoryAdminForm
    # inlines = [ItemsCategoryInline]


# class ItemsCategoryAdmin(admin.ModelAdmin):
#     search_fields = ['category__name', 'item__name', 'item__code']
#     list_filter = ('category',)
#     # list_display = ('name', 'active')


admin.site.register(models.Category, CategoryAdmin)
# admin.site.register(models.ItemsCategory, ItemsCategoryAdmin)
