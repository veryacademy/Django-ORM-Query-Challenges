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
class challenge_1_11_ViewSet(ViewSet):
    #########################################
    # Task: Fetch Products with No Description
    # Logic: description__isnull=True
    # Return: All fields
    #########################################

    def list(self, request):
        # Filter Product objects where the 'description' field is null (i.e., has no description).
        products = Product.objects.filter(description__isnull=True)

        # Serialize the filtered queryset. 'many=True' indicates that we are serializing a list of objects.
        serializer = ProductSerializer(products, many=True)

        # Return the serialized data as a REST framework Response.
        return Response(serializer.data)
