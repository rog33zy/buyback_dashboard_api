from functools import partial
from rest_framework import generics, status
from .serializers import BuybackDataSerializer, BuybackDataSerializerTwo, BuybackDataSerializerThree
from .models import BuybackData

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from django.http.response import JsonResponse
from django.db.models import Sum


class BuybackDataListView(generics.ListAPIView):

    filterset_fields = ["category", "season", "crop", "variety"]

    def get_serializer_class(self):
        category_param = self.request.query_params.get("category")
        crop_param = self.request.query_params.get("crop")
        season_param = self.request.query_params.get("season")
        variety_param = self.request.query_params.get("variety")

        if category_param is None:
            return BuybackDataSerializerTwo

        elif (category_param == "seed" or category_param == "source" or category_param == "commercial") and (
            crop_param is None or season_param is None or variety_param is None
        ):
            return BuybackDataSerializerThree

        else:
            return BuybackDataSerializer

    def get_queryset(self):
        category_param = self.request.query_params.get("category")
        crop_param = self.request.query_params.get("crop")
        season_param = self.request.query_params.get("season")
        variety_param = self.request.query_params.get("variety")
        if category_param is None:
            queryset = (
                BuybackData.objects.values(
                    "category",
                )
                .order_by("category")
                .annotate(
                    total_yield_estimate=Sum("yields_estimates_weight_mt"),
                    total_actual_yield=Sum("actual_yields_weight_mt"),
                )
            )

        elif (category_param == "seed") and (crop_param is None or season_param is None or variety_param is None):
            queryset = (
                BuybackData.objects.values(
                    "camp",
                )
                .order_by("camp")
                .annotate(
                    total_yield_estimate=Sum("yields_estimates_weight_mt"),
                    total_actual_yield=Sum("actual_yields_weight_mt"),
                    total_amount_purchased=Sum("total_purchased_amount"),
                )
            )

        elif (category_param == "commercial" or category_param == "source") and (
            crop_param is None or season_param is None or variety_param is None
        ):
            queryset = (
                BuybackData.objects.values(
                    "field_supervisor",
                )
                .order_by("field_supervisor")
                .annotate(
                    total_yield_estimate=Sum("yields_estimates_weight_mt"),
                    total_actual_yield=Sum("actual_yields_weight_mt"),
                    total_amount_purchased=Sum("total_purchased_amount"),
                )
            )

        else:
            queryset = BuybackData.objects.all().order_by("camp")
        return queryset


@api_view(["POST"])
def post_category_view(request):

    if request.method == "POST":
        buyback_entry_data = JSONParser().parse(request)
        buyback_entry_serializer = BuybackDataSerializer(data=buyback_entry_data)
        if buyback_entry_serializer.is_valid():
            buyback_entry_serializer.save()
            return JsonResponse(buyback_entry_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(buyback_entry_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH", "DELETE"])
def edit_category_view(request, pk):
    try:
        detailed_buyback_entry = BuybackData.objects.get(pk=pk)
    except BuybackData.DoesNotExist:
        return JsonResponse({"message": "The request does not exist"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PATCH":
        buyback_entry_data = JSONParser().parse(request)
        buyback_entry_serializer = BuybackDataSerializer(detailed_buyback_entry, data=buyback_entry_data, partial=True)

        if buyback_entry_serializer.is_valid():
            buyback_entry_serializer.save()
            return JsonResponse(buyback_entry_serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        detailed_buyback_entry.delete()
        return JsonResponse({"message": "Entry was deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    return JsonResponse(buyback_entry_serializer.errors, status=status.HTTP_400_BAD_REQUEST)