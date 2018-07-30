from rest_framework import serializers

from items.serializers import ItemSerializer

from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')

    def validate_name(self):
        name = self.cleaned_data['name'].lower()
        if models.Category.objects.filter(name=name).exists():
            raise serializers.ValidationError("This name already exist.")
        return name


class ItemsCategorySerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()
    item = ItemSerializer(many=True)

    class Meta:
        model = models.ItemsCategory
        fields = ('item',)
