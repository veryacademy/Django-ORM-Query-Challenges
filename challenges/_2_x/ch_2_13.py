from drf_spectacular.utils import extend_schema
from inventory.models import PromotionEvent  # Import the PromotionEvent model
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.utils import timezone # Import timezone for current time comparison

#################################
# Challenge serializer
#################################


class PromotionEventSerializer(serializers.ModelSerializer):
    """
    Serializer for the PromotionEvent model, exposing specific fields.
    """
    class Meta:
        model = PromotionEvent
        fields = [
            "id",
            "name",
            "start_date",
            "end_date",
            "price_reduction",
        ]


#################################
# Challenge Viewset
#################################


@extend_schema(
    tags=["_1_x Challenge Endpoint"],
    responses={200: PromotionEventSerializer(many=True)},
)
class challenge_1_12_ViewSet(ViewSet):
    #########################################
    # Task: List All Promotion Events That Have Ended
    # Logic: end_date__lte=timezone.now()
    # Return: All fields
    #########################################

    def list(self, request):
        # Get the current time using Django's timezone utility.
        current_time = timezone.now()

        # Filter PromotionEvent objects where the 'end_date' is less than or equal to the current time.
        # This effectively selects all promotion events that have already concluded.
        promotion_events = PromotionEvent.objects.filter(end_date__lte=current_time)

        # Serialize the filtered queryset. 'many=True' indicates that we are serializing a list of objects.
        serializer = PromotionEventSerializer(promotion_events, many=True)
        
        # Return the serialized data as a REST framework Response.
        return Response(serializer.data)
