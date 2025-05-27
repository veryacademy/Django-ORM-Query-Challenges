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
class challenge_1_3_ViewSet(ViewSet):
    #########################################
    # Task: Find Products in Multiple Categories
    # Filter: Category IDs: 1, 4, 8, 11
    # Return: All fields
    #########################################

    def list(self, request):
        category_ids = [1, 4, 8, 11]
        products = Product.objects.filter(category_id__in=category_ids)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
