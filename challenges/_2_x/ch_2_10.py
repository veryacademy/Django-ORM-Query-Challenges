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
    tags=["_2_x Challenge Endpoint"],
    responses={200: UserSerializer(many=True)},
)
class challenge_2_10_ViewSet(ViewSet):
    #########################################
    # Task: Find Users with Emails Ending in 'example.com'
    # Return: id, username, email
    #########################################

    def list(self, request):
        #############
        # Replace ... with your solution.
        # Note: Prepare data in variable users
        #############
        ...

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
