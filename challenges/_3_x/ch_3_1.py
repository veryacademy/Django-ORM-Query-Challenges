from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    OpenApiTypes,
    extend_schema,
)
from inventory.models import Category, Product
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
    tags=["_3_x Challenge Endpoint"],
    responses={200: ProductSerializer(many=True)},
    parameters=[
        OpenApiParameter(
            name="category_name",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description="The name of the category to filter products by. (e.g., 'Electronics')",
            required=True,
            examples=[
                OpenApiExample(  # <--- Use OpenApiExample here
                    name="Example: Electronics",
                    value="Electronics",
                    description="Products in the Electronics category.",
                ),
                OpenApiExample(  # <--- Use OpenApiExample here
                    name="Example: Books",
                    value="Books",
                    description="Products in the Books category.",
                ),
                OpenApiExample(  # <--- Use OpenApiExample here
                    name="Example: Clothing",
                    value="Clothing",
                    description="Products in the Clothing category.",
                ),
            ],
        ),
    ],
)
class challenge_3_1_ViewSet(ViewSet):
    #########################################
    # Task: Retrieve products by category name
    # Filter[1]: Active products only
    # Order By: id
    # Fields: All fields
    #########################################

    def list(self, request):
        category_name = request.query_params.get("category_name")

        products = Product.objects.filter(
            category__name=category_name,
            is_active=True,
        ).order_by("id")

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
