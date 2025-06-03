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
    responses={
        200: ProductSerializer(many=True)
    },  # It returns a list, even if it's just one item
)
class challenge_2_11_ViewSet(ViewSet):
    #########################################
    # Task: Return the 20th most expensive product
    # Return: All fields
    #########################################

    def list(self, request):
        #############
        # Replace ... with your solution.
        # Note: Prepare data in variable products
        #############
        ...

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
