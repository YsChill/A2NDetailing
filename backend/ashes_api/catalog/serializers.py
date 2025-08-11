from rest_framework import serializers
from .models import Service, Package, AddOn, SiteSettings


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "name", "slug", "starting_price", "duration_text", "features"]


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ["id", "name", "slug", "starting_price", "duration_text", "includes", "perfect_for"]


class AddOnSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddOn
        fields = ["id", "name", "price_range"]


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = [
            "company_name",
            "tagline",
            "phone",
            "email",
            "service_area",
            "hours_text",
            "cancellation_policy",
            "weather_policy",
            "heavy_policy",
            "guarantee_policy",
            "theme_bg",
            "theme_accent",
        ]
