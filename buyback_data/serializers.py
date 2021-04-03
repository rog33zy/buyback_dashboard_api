from rest_framework import serializers

from .models import BuybackData


class BuybackDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuybackData
        fields = "__all__"


class BuybackDataSerializerTwo(serializers.ModelSerializer):
    total_yield_estimate = serializers.DecimalField(decimal_places=2, max_digits=10)
    total_actual_yield = serializers.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        model = BuybackData
        fields = (
            "id",
            "category",
            "crop",
            "variety",
            "season",
            "camp",
            "field_supervisor",
            "yields_estimates_weight_mt",
            "actual_yields_weight_mt",
            "total_purchased_amount",
            "total_yield_estimate",
            "total_actual_yield",
            "last_updated",
        )
