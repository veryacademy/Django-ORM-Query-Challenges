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
    responses={
        200: ProductSerializer(many=True)
    },  # It returns a list, even if it's just one item
)
class challenge_1_10_ViewSet(ViewSet):
    #########################################
    # Task: Return the 20th most expensive product
    # Logic: order_by('-price')[19:20]
    # Return: All fields
    #########################################

    def list(self, request):
        # Order products by price in descending order (most expensive first).
        # Then, use slicing [19:20] to get the 20th product (0-indexed, so index 19).
        # This slice will return a queryset containing at most one product.
        products = Product.objects.order_by("-price")[19:20]

        # Serialize the queryset. 'many=True' is used because even a single item
        # extracted via slicing still results in a queryset (a list-like object).
        serializer = ProductSerializer(products, many=True)

        # Return the serialized data as a REST framework Response.
        return Response(serializer.data)
