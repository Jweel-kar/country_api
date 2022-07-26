from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    country_lang = serializers.CharField(required=True, allow_blank=False, max_length=100)
    country_currency = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Country` instance, given the validated data.
        """
        return Country.objects.create(
            country_name=validated_data.get('country_name'),
            country_lang=validated_data.get('country_lang'),
            country_currency=validated_data.get('country_currency'),
            )

    def update(self, instance, validated_data):
        """
        Update and return an existing `Country` instance, given the validated data.
        """
        instance.country_name = validated_data.get('country_name', instance.country_name)
        instance.country_lang = validated_data.get('country_lang', instance.country_lang)
        instance.country_currency = validated_data.get('country_currency', instance.country_currency)
        instance.save()
        return instance

    class Meta:
        model = Country
        fields = ['id', 'country_name', 'country_lang', 'country_currency']
