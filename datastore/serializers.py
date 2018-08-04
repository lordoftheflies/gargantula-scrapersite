from rest_framework import serializers
from rest_framework.views import APIView
from mdm import models as mdm_models
from botapp import models as bot_models
from datastore import models as data_models


class BestOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.BestOfferModel
        fields = (
            'id', 'timestamp', 'duration',
            'supplier', 'supplier_name',
            'market', 'market_name',
            'departure', 'departure_name',
            'arrival', 'arrival_name',
            'lowest_price', 'bag_weight', 'bag_price',

            'bag_price_per_person',
            'hotel_only_price',
            'flight_only_price',
            'flight_price_with_bag',
            'package_price',
            'full_package_price'
        )


        # def create(self, validated_data):
        #     """
        #     Create and return a new `Snippet` instance, given the validated data.
        #     """
        #     return Snippet.objects.create(**validated_data)
        #
        # def update(self, instance, validated_data):
        #     """
        #     Update and return an existing `Snippet` instance, given the validated data.
        #     """
        #     instance.title = validated_data.get('title', instance.title)
        #     instance.code = validated_data.get('code', instance.code)
        #     instance.linenos = validated_data.get('linenos', instance.linenos)
        #     instance.language = validated_data.get('language', instance.language)
        #     instance.style = validated_data.get('style', instance.style)
        #     instance.save()
        #     return instance
