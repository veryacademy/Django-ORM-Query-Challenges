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
class challenge_1_1_ViewSet(ViewSet):
    #########################################
    # Task: Retrieve all active products only
    # Return: All fields
    # Order-By: Name (Decending)
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
