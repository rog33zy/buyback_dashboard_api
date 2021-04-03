from functools import partial
from rest_framework import generics, status
from .serializers import BuybackDataSerializer, BuybackDataSerializerTwo
from .models import BuybackData

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from django.http.response import JsonResponse
from django.db.models import Sum


class BuybackDataListView(generics.ListAPIView):

    filterset_fields = ["category", "season", "crop", "variety"]

    def get_serializer_class(self):
        category_param = self.request.query_params.get("category")

        if category_param is None:
            return BuybackDataSerializerTwo
        return BuybackDataSerializer

    def get_queryset(self):
        category_param = self.request.query_params.get("category")
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


@api_view(["PATCH"])
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
    return JsonResponse(buyback_entry_serializer.errors, status=status.HTTP_400_BAD_REQUEST)