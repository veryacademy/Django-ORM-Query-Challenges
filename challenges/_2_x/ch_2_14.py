from drf_spectacular.utils import extend_schema
from inventory.models import (  # Import both Product and Category models
    Category,
    Product,
)
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

#################################
# Challenge serializer
#################################


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model, exposing specific fields.
    """

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
        ]


#################################
# Challenge Viewset
#################################


@extend_schema(
    tags=["_1_x Challenge Endpoint"],
    responses={200: CategorySerializer(many=True)},
)
class challenge_1_13_ViewSet(ViewSet):
    #########################################
    # Task: List all Unique Categories Related to a Product
    # Logic: Product.objects.values_list('category', flat=True).distinct() then get Category objects
    # Return: id, name, slug for unique categories
    #########################################

    def list(self, request):
        # Get the IDs of all unique categories associated with any product.
        # values_list('category', flat=True) returns a flat list of category IDs.
        # .distinct() ensures only unique category IDs are returned.
        unique_category_ids = Product.objects.values_list(
            "category", flat=True
        ).distinct()

        # Fetch the actual Category objects using the unique IDs.
        # in=unique_category_ids will select all Category objects whose IDs are in the list.
        unique_categories = Category.objects.filter(id__in=unique_category_ids)

        # Serialize the unique Category objects. 'many=True' indicates that we are serializing a list of objects.
        serializer = CategorySerializer(unique_categories, many=True)

        # Return the serialized data as a REST framework Response.
        return Response(serializer.data)
