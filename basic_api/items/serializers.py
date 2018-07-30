from items.models import Item

from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'code', 'active')

    # def validate_name(self):
    #     name = self.cleaned_data['name'].lower()
    #     if Item.objects.filter(name=name).exists():
    #         raise serializers.ValidationError("This name already exist.")
    #     return name

    # def validate_code(self):
    #     code = self.cleaned_data['code'].upper()
    #     if Item.objects.filter(code=code).exists():
    #         raise serializers.ValidationError("This code already exist.")
    #     return code
