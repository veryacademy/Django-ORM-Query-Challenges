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
class challenge_1_7_ViewSet(ViewSet):
    #########################################
    # Task: Find Products Ending with the Letter 'E'
    # Logic: name__endswith='E'
    # Return: All fields
    #########################################

    def list(self, request):
        # Filter products where the 'name' field ends with the letter 'E'.
        products = Product.objects.filter(name__endswith="E")

        # Serialize the filtered queryset. 'many=True' indicates that we are serializing a list of objects.
        serializer = ProductSerializer(products, many=True)

        # Return the serialized data as a REST framework Response.
        return Response(serializer.data)
