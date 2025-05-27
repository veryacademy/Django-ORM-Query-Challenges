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
class challenge_1_4_ViewSet(ViewSet):
    #########################################
    # Task: List Products Priced Between 50 and 1000
    # Filter: price >= 50 and price <= 1000
    # Return: All fields
    #########################################

    def list(self, request):
        products = Product.objects.filter(price__gte=50, price__lte=1000)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
