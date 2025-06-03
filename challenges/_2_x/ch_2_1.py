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
        # Query for the first five active products ordered by ID ascending
        first_five_queryset = Product.objects.filter(is_active=True).order_by("id")[:5]

        # Query for the last five active products ordered by ID descending
        last_five_queryset = Product.objects.filter(is_active=True).order_by("-id")[:5]

        # Combine the two querysets using .union()
        # By default, union() performs a UNION DISTINCT, removing duplicates.
        # If you needed UNION ALL, you'd use .union(..., all=True)
        combined_products = first_five_queryset.union(last_five_queryset)

        # The combined_products is now a QuerySet, which can be directly serialized.
        serializer = ProductSerializer(combined_products, many=True)
        return Response(serializer.data)
