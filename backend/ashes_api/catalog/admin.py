from django.contrib import admin
from .models import Service, Package, AddOn, SiteSettings


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "starting_price", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("name", "starting_price", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(AddOn)
class AddOnAdmin(admin.ModelAdmin):
    list_display = ("name", "price_range", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
