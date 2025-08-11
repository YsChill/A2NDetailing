from rest_framework import viewsets
from rest_framework.response import Response
from .models import Service, Package, AddOn, SiteSettings
from .serializers import (
    ServiceSerializer,
    PackageSerializer,
    AddOnSerializer,
    SiteSettingsSerializer,
)


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer


class PackageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Package.objects.filter(is_active=True)
    serializer_class = PackageSerializer


class AddOnViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AddOn.objects.filter(is_active=True)
    serializer_class = AddOnSerializer


class SiteSettingsViewSet(viewsets.ViewSet):
    def list(self, request):
        settings = SiteSettings.load()
        serializer = SiteSettingsSerializer(settings)
        return Response(serializer.data)
