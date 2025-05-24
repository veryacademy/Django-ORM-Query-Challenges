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
    # Task: Retrieve all products - excluding active products.
    # Return: All fields
    # Instruction: Do not use a filter()
    #########################################

    def list(self, request):
        products = (
            #############
            # Replace ... with your solution.
            #############
            ...
        )

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
