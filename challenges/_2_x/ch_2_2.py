from datetime import timedelta

from django.utils.timezone import now
from drf_spectacular.utils import extend_schema
from inventory.models import Order
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

#################################
# Challenge serializer
#################################


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "created_at",
            "updated_at",
        ]


#################################
# Challenge Viewset
#################################


@extend_schema(
    tags=["_2_x Challenge Endpoint"],
    responses={200: OrderSerializer(many=True)},
)
class challenge_2_2_ViewSet(ViewSet):
    #########################################
    # Task: Retrieve Orders from the Last 30 Days
    # Return: All fields
    #########################################

    def list(self, request):
        #############
        # Replace ... with your solution.
        # Note: Prepare data in variable orders
        #############
        ...

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
