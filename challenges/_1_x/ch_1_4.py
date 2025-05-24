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
    responses={200: ProductSerializer},
)
class challenge_1_4_ViewSet(ViewSet):
    #########################################
    # Task: Retrieve the most recently added product
    # Return: All fields
    #########################################

    def list(self, request):
        product = (
            #############
            # Replace ... with your solution.
            #############
            ...
        )

        serializer = ProductSerializer(product)
        return Response(serializer.data)
