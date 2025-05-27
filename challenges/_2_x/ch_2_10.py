from drf_spectacular.utils import extend_schema
from inventory.models import User  # Import the User model
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

#################################
# Challenge serializer
#################################


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model, exposing specific fields.
    """
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
        ]


#################################
# Challenge Viewset
#################################


@extend_schema(
    tags=["_1_x Challenge Endpoint"],
    responses={200: UserSerializer(many=True)},
)
class challenge_1_9_ViewSet(ViewSet):
    #########################################
    # Task: Find Users with Emails Ending in 'example.com'
    # Logic: email__endswith='example.com'
    # Return: id, username, email
    #########################################

    def list(self, request):
        # Filter User objects where the 'email' field ends with 'example.com'.
        users = User.objects.filter(email__endswith='example.com')

        # Serialize the filtered queryset. 'many=True' indicates that we are serializing a list of objects.
        serializer = UserSerializer(users, many=True)
        
        # Return the serialized data as a REST framework Response.
        return Response(serializer.data)
