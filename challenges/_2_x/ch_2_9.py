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
class challenge_1_8_ViewSet(ViewSet):
    #########################################
    # Task: Show the Top 10 Most Expensive Active Products
    # Logic: is_active=True, order_by('-price'), [:10]
    # Return: All fields
    #########################################

    def list(self, request):
        # Filter for products that are active, order them by price in descending order
        # (most expensive first), and then slice the queryset to get only the top 10.
        products = Product.objects.filter(is_active=True).order_by("-price")[:10]

        # Serialize the filtered and ordered queryset. 'many=True' indicates that we are serializing a list of objects.
        serializer = ProductSerializer(products, many=True)

        # Return the serialized data as a REST framework Response.
        return Response(serializer.data)
