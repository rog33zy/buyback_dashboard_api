from functools import partial
from rest_framework import generics, status
from .serializers import (
    ProcessingDataSerializer,
    ProcessingDataSerializerTwo,
    ProcessingDataSerializerThree,
)
from .models import ProcessingData

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from django.http.response import JsonResponse
from django.db.models import Sum


class ProcessingDataListView(generics.ListAPIView):
    filterset_fields = ["category", "season", "crop", "variety"]

    def get_serializer_class(self):
        category_param = self.request.query_params.get("category")
        crop_param = self.request.query_params.get("crop")
        season_param = self.request.query_params.get("season")
        variety_param = self.request.query_params.get("variety")

        if category_param is None:
            return ProcessingDataSerializerTwo

        elif (
            category_param == "seed"
            or category_param == "source"
            or category_param == "commercial"
            or category_param == "malawi"
        ) and (crop_param is None or season_param is None or variety_param is None):
            return ProcessingDataSerializerThree

        else:
            return ProcessingDataSerializer

    def get_queryset(self):
        category_param = self.request.query_params.get("category")
        crop_param = self.request.query_params.get("crop")
        season_param = self.request.query_params.get("season")
        variety_param = self.request.query_params.get("variety")
        if category_param is None:
            queryset = (
                ProcessingData.objects.values(
                    "category",
                )
                .order_by("category")
                .annotate(
                    total_purchased=Sum("purchased_weight_mt"),
                    total_received=Sum("received_weight_mt"),
                    total_processed=Sum("processed_weight_mt"),
                    total_cleaned=Sum("cleaned_weight_mt"),
                    total_sorts=Sum("sorts_weight_mt"),
                    total_waste=Sum("waste_weight_mt"),
                    total_hq_to_lsk=Sum("hq_to_lsk"),
                )
            )

        elif (category_param == "seed") and (
            crop_param is None or season_param is None or variety_param is None
        ):
            queryset = (
                ProcessingData.objects.values(
                    "camp",
                )
                .order_by("camp")
                .annotate(
                    total_purchased=Sum("purchased_weight_mt"),
                    total_received=Sum("received_weight_mt"),
                    total_processed=Sum("processed_weight_mt"),
                    total_cleaned=Sum("cleaned_weight_mt"),
                    total_sorts=Sum("sorts_weight_mt"),
                    total_waste=Sum("waste_weight_mt"),
                    total_hq_to_lsk=Sum("hq_to_lsk"),
                )
            )

        elif (
            category_param == "commercial"
            or category_param == "source"
            or category_param == "malawi"
        ) and (crop_param is None or season_param is None or variety_param is None):
            queryset = (
                ProcessingData.objects.values(
                    "field_supervisor",
                )
                .order_by("field_supervisor")
                .annotate(
                    total_purchased=Sum("purchased_weight_mt"),
                    total_received=Sum("received_weight_mt"),
                    total_processed=Sum("processed_weight_mt"),
                    total_cleaned=Sum("cleaned_weight_mt"),
                    total_sorts=Sum("sorts_weight_mt"),
                    total_waste=Sum("waste_weight_mt"),
                    total_hq_to_lsk=Sum("hq_to_lsk"),
                )
            )

        else:
            queryset = ProcessingData.objects.all().order_by("camp")
        return queryset


@api_view(["POST"])
def post_category_view(request):
    if request.method == "POST":
        processing_entry_data = JSONParser().parse(request)
        processing_entry_serializer = ProcessingDataSerializer(
            data=processing_entry_data
        )
        if processing_entry_serializer.is_valid():
            processing_entry_serializer.save()
            return JsonResponse(
                processing_entry_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            processing_entry_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["PATCH", "DELETE"])
def edit_category_view(request, pk):
    try:
        detailed_processing_entry = ProcessingData.objects.get(pk=pk)
    except ProcessingData.DoesNotExist:
        return JsonResponse(
            {"message": "The request does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "PATCH":
        processing_entry_data = JSONParser().parse(request)
        processing_entry_serializer = ProcessingDataSerializer(
            detailed_processing_entry, data=processing_entry_data, partial=True
        )

        if processing_entry_serializer.is_valid():
            processing_entry_serializer.save()
            return JsonResponse(
                processing_entry_serializer.data, status=status.HTTP_200_OK
            )

    elif request.method == "DELETE":
        detailed_processing_entry.delete()
        return JsonResponse(
            {"message": "Entry was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )
    return JsonResponse(
        processing_entry_serializer.errors, status=status.HTTP_400_BAD_REQUEST
    )
