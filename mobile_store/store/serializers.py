from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from core.models import Brand, Mobile


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'nationality']


class MobileSerializers(serializers.ModelSerializer):
    brand = BrandSerializers(many=False, required=True)
    model_name = serializers.CharField(validators=[UniqueValidator(queryset=Mobile.objects.all(),
                                                                   message="model name already exist")])


    class Meta:
        model = Mobile
        fields = "__all__"

    def create(self, validated_data):
        brand = validated_data.pop("brand")
        brand_obj, created = Brand.objects.get_or_create(**brand)
        validated_data['brand'] = brand_obj

        return Mobile.objects.create(**validated_data)
