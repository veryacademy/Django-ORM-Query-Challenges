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
    responses={200: ProductSerializer(many=True)},
)
class challenge_2_7_ViewSet(ViewSet):
    #########################################
    # Task: Get Products Name Starting with the Letter 'W'
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
