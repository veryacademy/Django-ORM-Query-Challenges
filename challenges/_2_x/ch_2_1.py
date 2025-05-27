from drf_spectacular.utils import extend_schema
from inventory.models import Product
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

#################################
# Challenge serializer
#################################


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "price",
            "is_active",
        ]


#################################
# Challenge Viewset
#################################


@extend_schema(
    tags=["_2_x Challenge Endpoint"],
    responses={200: ProductSerializer(many=True)},
)
class challenge_2_1_ViewSet(ViewSet):
    #########################################
    # Task: Get the First and Last 5 Added Products
    # Filter: Active products only
    # Return: All fields
    #########################################

    # def list(self, request):
    #     products = list(
    #         Product.objects.filter(is_active=True).order_by("id")[:5]
    #     ) + list(Product.objects.filter(is_active=True).order_by("-id")[:5])
    #     products = list({p.id: p for p in products}.values())

    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)

    # def list(self, request):
    #     queryset = Product.objects.filter(is_active=True).order_by("id")
    #     total = queryset.count()

    #     first_five = list(queryset[:5])
    #     last_five = list(queryset[max(total - 5, 0) :])

    #     products = list({p.id: p for p in first_five + last_five}.values())

    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)

    def list(self, request):
        first_five = Product.objects.filter(is_active=True).order_by("id")[:5]
        last_five = Product.objects.filter(is_active=True).order_by("-id")[:5]

        # Combine and remove any duplicates by ID
        combined = list({p.id: p for p in list(first_five) + list(last_five)}.values())

        serializer = ProductSerializer(combined, many=True)
        return Response(serializer.data)
