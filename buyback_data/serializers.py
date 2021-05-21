from rest_framework import serializers

from .models import BuybackData


class BuybackDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuybackData
        fields = "__all__"


class BuybackDataSerializerTwo(serializers.ModelSerializer):
    total_yield_estimate = serializers.DecimalField(decimal_places=2, max_digits=10)
    total_actual_yield = serializers.DecimalField(decimal_places=2, max_digits=10)
    total_amount_purchased_zmw = serializers.DecimalField(decimal_places=2, max_digits=12)
    total_amount_purchased_usd = serializers.DecimalField(decimal_places=2, max_digits=12)

    total_amount_paid_zmw = serializers.DecimalField(decimal_places=2, max_digits=12)
    total_amount_paid_usd = serializers.DecimalField(decimal_places=2, max_digits=12)

    total_hectares_bought_from = serializers.DecimalField(decimal_places=2, max_digits=8)
    total_farmers_bought_from = serializers.IntegerField()
    all_farmers = serializers.IntegerField()

    class Meta:
        model = BuybackData
        fields = (
            "id",
            "category",
            "all_farmers",
            "total_farmers_bought_from",
            "total_hectares_bought_from",
            "total_amount_purchased_zmw",
            "total_amount_purchased_usd",
            "total_amount_paid_zmw",
            "total_amount_paid_usd",
            "total_yield_estimate",
            "total_actual_yield",
            "last_updated",
        )


class BuybackDataSerializerThree(serializers.ModelSerializer):
    total_yield_estimate = serializers.DecimalField(decimal_places=2, max_digits=10)
    total_actual_yield = serializers.DecimalField(decimal_places=2, max_digits=10)
    total_amount_purchased_zmw = serializers.DecimalField(decimal_places=2, max_digits=12)
    total_amount_purchased_usd = serializers.DecimalField(decimal_places=2, max_digits=12)

    total_amount_paid_zmw = serializers.DecimalField(decimal_places=2, max_digits=12)
    total_amount_paid_usd = serializers.DecimalField(decimal_places=2, max_digits=12)

    total_hectares_bought_from = serializers.DecimalField(decimal_places=2, max_digits=8)
    total_farmers_bought_from = serializers.IntegerField()
    all_farmers = serializers.IntegerField()

    class Meta:
        model = BuybackData
        fields = (
            "field_supervisor",
            "camp",
            "all_farmers",
            "total_farmers_bought_from",
            "total_hectares_bought_from",
            "total_amount_purchased_zmw",
            "total_amount_purchased_usd",
            "total_amount_paid_zmw",
            "total_amount_paid_usd",
            "total_yield_estimate",
            "total_actual_yield",
        )