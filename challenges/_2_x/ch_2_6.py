from drf_spectacular.utils import extend_schema
from inventory.models import User
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

#################################
# Challenge serializer
#################################


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
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
class challenge_2_6_ViewSet(ViewSet):
    #########################################
    # Task: Return Users Named janedoe or johndoe
    # Return: All fields in serializer
    #########################################

    def list(self, request):
        #############
        # Replace ... with your solution.
        # Note: Prepare data in variable users
        #############
        ...

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
