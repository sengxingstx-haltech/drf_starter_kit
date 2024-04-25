from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from quickstart.models import Employee, Profile

from .serializers import EmployeeSerializer, GroupSerializer, ProfileSerializer, UserSerializer


class APIRootView(APIView):

    def get(self, request, format=None):
        return Response(
            {
                'auth': {
                    "login": reverse("token_obtain_pair", request=request, format=format),
                    "refresh_token": reverse("token_refresh", request=request, format=format),
                },
                "users": reverse("user-list", request=request, format=format),
                "groups": reverse("group-list", request=request, format=format),
                "employees": reverse("employee-list", request=request, format=format),
            }
        )


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [permissions.IsAuthenticated]
