from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from quickstart.models import Employee, Profile

from .serializers import EmployeeSerializer, ProfileSerializer


class APIRootView(APIView):

    def get(self, request, format=None):
        return Response(
            {
                'auth': {
                    "login": reverse("token_obtain_pair", request=request, format=format),
                    "refresh_token": reverse("token_refresh", request=request, format=format),
                },
                "accounts": reverse("account-list", request=request, format=format),
                "roles": reverse("role-list", request=request, format=format),
                "permissions": reverse("permission-list", request=request, format=format),
                "employees": reverse("employee-list", request=request, format=format),
            }
        )


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [permissions.IsAuthenticated]
