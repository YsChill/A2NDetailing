from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from catalog.models import SiteSettings


class SettingsAPITest(TestCase):
    def test_settings_endpoint_returns_company_name(self):
        SiteSettings.objects.create(
            company_name="Ashes to New Detailing LLC",
            tagline="Bringing Back the Shine",
            phone="(810) 666-1417",
            email="test@gmail.com",
            service_area="Genesee County, MI",
            hours_text="By Appointment Only",
            cancellation_policy="c",
            weather_policy="w",
            heavy_policy="h",
            guarantee_policy="g",
        )
        client = APIClient()
        response = client.get(reverse("settings-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["company_name"], "Ashes to New Detailing LLC"
        )
