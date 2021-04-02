from rest_framework import serializers

from .models import BuybackData


class BuybackDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuybackData
        fields = "__all__"