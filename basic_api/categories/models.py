from django.db import models
from django.dispatch import receiver

# from items.models import Item


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('active',)

    def __str__(self):
        """Magic func for print in the admin page."""
        return self.name

    # def get_items(self, **kwargs):
    #     return ItemsCategory.get_by_cat_id(self.id, **kwargs)

    @classmethod
    def get(cls, **kwargs):
        """Get all Items."""
        return cls.objects.filter(**kwargs)

    @classmethod
    def get_active(cls, **kwargs):
        """Get All Active items."""
        return cls.get(active=True, **kwargs)


# class ItemsCategory(models.Model):
#     item = models.ForeignKey(Item, related_name='items', blank=False, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, related_name='categories', blank=False, on_delete=models.CASCADE)

#     def __str__(self):
#         """Magic func for print in the admin page."""
#         return self.category.name + " - " + self.item.code

#     @classmethod
#     def get(cls, **kwargs):
#         """Get all Items."""
#         return cls.objects.filter(**kwargs)

#     @classmethod
#     def get_by_cat_id(cls, id, **kwargs):
#         """Get All Active items."""
#         return cls.get(category_id=id, **kwargs).only('item')


@receiver(models.signals.pre_save, sender=Category)
def convert_to(sender, instance, *args, **kwargs):
    instance.name = instance.name.lower()
