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
class challenge_1_6_ViewSet(ViewSet):
    #########################################
    # Task: Get Products Starting with the Letter 'W'
    # Logic: name__startswith='W'
    # Return: All fields
    #########################################

    def list(self, request):
        # Filter products where the 'name' field starts with the letter 'W'.
        products = Product.objects.filter(name__startswith="W")

        # Serialize the filtered queryset. 'many=True' indicates that we are serializing a list of objects.
        serializer = ProductSerializer(products, many=True)

        # Return the serialized data as a REST framework Response.
        return Response(serializer.data)
