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
    tags=["_1_x Challenge Endpoint"],
    responses={200: ProductSerializer(many=True)},
)
class challenge_1_5_ViewSet(ViewSet):
    #########################################
    # Task: Exclude Products Priced 19.99 and Under 100
    # Logic: price != 19.99 AND price >= 100
    # Return: All fields
    #########################################

    def list(self, request):
        products = Product.objects.exclude(price=19.99).filter(price__gte=100)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
