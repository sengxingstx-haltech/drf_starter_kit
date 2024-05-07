from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include
from rest_framework import routers
from accounts.views import AccountViewSet, PermissionViewSet, RoleViewSet
from . import views


router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'employees', views.EmployeeViewSet)


urlpatterns = [
    path('', views.APIRootView.as_view(), name='api-root'),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
