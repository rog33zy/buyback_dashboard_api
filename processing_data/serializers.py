from rest_framework import serializers

from .models import ProcessingData


class ProcessingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessingData
        fields = "__all__"


class ProcessingDataSerializerTwo(serializers.ModelSerializer):
    total_purchased = serializers.DecimalField(decimal_places=2, max_digits=10)
    total_received = serializers.DecimalField(decimal_places=2, max_digits=10)
    total_processed = serializers.DecimalField(decimal_places=2, max_digits=12)
    total_cleaned = serializers.DecimalField(decimal_places=2, max_digits=12)
    total_sorts = serializers.DecimalField(decimal_places=2, max_digits=8)
    total_waste = serializers.DecimalField(decimal_places=2, max_digits=8)
    total_hq_to_lsk = serializers.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        model = ProcessingData
        fields = (
            "id",
            "category",
            "total_waste",
            "total_sorts",
            "total_processed",
            "total_cleaned",
            "total_purchased",
            "total_received",
            "total_hq_to_lsk",
            "last_updated",
        )


class ProcessingDataSerializerThree(serializers.ModelSerializer):
    total_purchased = serializers.DecimalField(decimal_places=2, max_digits=10)
    total_received = serializers.DecimalField(decimal_places=2, max_digits=10)
    total_processed = serializers.DecimalField(decimal_places=2, max_digits=12)
    total_cleaned = serializers.DecimalField(decimal_places=2, max_digits=12)
    total_sorts = serializers.DecimalField(decimal_places=2, max_digits=8)
    total_waste = serializers.DecimalField(decimal_places=2, max_digits=8)
    total_hq_to_lsk = serializers.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        model = ProcessingData
        fields = (
            "field_supervisor",
            "camp",
            "total_waste",
            "total_sorts",
            "total_processed",
            "total_cleaned",
            "total_purchased",
            "total_received",
            "total_hq_to_lsk",
        )