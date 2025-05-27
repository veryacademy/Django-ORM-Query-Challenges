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
class challenge_2_6_ViewSet(ViewSet):
    #########################################
    # Task: Find Users Named janedoe or johndoe
    # Filter: username IN ['janedoe', 'johndoe']
    # Return: All fields in serializer
    #########################################

    def list(self, request):
        users = User.objects.filter(username__in=["janedoe", "johndoe"])

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
