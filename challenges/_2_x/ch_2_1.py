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
class challenge_2_1_ViewSet(ViewSet):
    #########################################
    # Task: Retrieve the First and Last Five Product Entries
    # Filter[1]: Active products only
    # Order By: id
    # Fields: All fields
    # Extra[1]: Should not return duplicate records.
    #########################################

    def list(self, request):
        #############
        # Replace ... with your solution.
        # Note: Prepare data in variable products
        #############
        ...

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
