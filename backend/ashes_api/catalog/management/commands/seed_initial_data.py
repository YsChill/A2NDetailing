from django.core.management.base import BaseCommand
from catalog.models import Service, Package, AddOn, SiteSettings


class Command(BaseCommand):
    help = "Seed initial data for services, packages, add-ons, and site settings"

    def handle(self, *args, **options):
        Service.objects.all().delete()
        Package.objects.all().delete()
        AddOn.objects.all().delete()

        services = [
            {
                "name": "Basic Exterior",
                "starting_price": 75,
                "features": ["Body & wheels wash"],
            },
            {
                "name": "Basic Interior",
                "starting_price": 75,
                "features": ["Seats & carpets vacuumed", "Surfaces wiped down"],
            },
            {
                "name": "Standard Exterior",
                "starting_price": 125,
                "features": [
                    "Body hand washed",
                    "Waxed",
                    "Tires/Wheels washed & shined",
                    "Windows",
                    "Gas cap area cleaned",
                    "Door jambs cleaned",
                ],
            },
            {
                "name": "Standard Interior",
                "starting_price": 125,
                "features": [
                    "All carpets & seats vacuumed",
                    "All surfaces cleaned (restorative where applicable)",
                    "Windows",
                ],
            },
            {
                "name": "Deluxe Exterior",
                "starting_price": 175,
                "features": [
                    "Windows",
                    "Door jambs cleaned",
                    "Clean gas cap area",
                    "Clay bar treatment",
                    "Wax",
                    "Body hand washed",
                    "Tires/Wheels washed & shined",
                ],
            },
            {
                "name": "Deluxe Interior",
                "starting_price": 175,
                "features": [
                    "All carpets & seats vacuumed",
                    "Shampoo carpets & mats",
                    "Shampoo seats / recondition leather seats",
                    "Windows",
                    "All surfaces deep cleaned",
                ],
            },
        ]

        for data in services:
            Service.objects.create(**data)

        packages = [
            {
                "name": "Basic Package",
                "starting_price": 100,
                "includes": [
                    "Body hand washed",
                    "Tires/Wheels washed",
                    "All carpets & seats vacuumed",
                    "Solid surfaces wiped down",
                ],
            },
            {
                "name": "Standard Package",
                "starting_price": 200,
                "includes": [
                    "Body hand washed & waxed",
                    "Tires/Wheels washed & shined",
                    "Windows inside & out",
                    "All carpets & seats vacuumed",
                    "All surfaces cleaned (restorative where applicable)",
                    "Gas cap area cleaned",
                    "Door jambs cleaned",
                ],
            },
            {
                "name": "Deluxe Package",
                "starting_price": 300,
                "includes": [
                    "Windows in & out",
                    "Door jambs & gas cap cleaned",
                    "Clay bar treatment",
                    "Wax",
                    "Shampoo carpets & mats",
                    "Shampoo seats / recondition leather seats",
                    "Body hand washed",
                    "Tires/Wheels washed & shined",
                    "All carpets & seats vacuumed",
                ],
            },
        ]
        for data in packages:
            Package.objects.create(**data)

        addons = [
            {"name": "Engine Cleaning", "price_range": "$100–$150"},
            {"name": "Tire Rotation", "price_range": "$15"},
            {"name": "Headlight Restoration", "price_range": "$50"},
            {"name": "Headliner Cleaning", "price_range": "$30–$60"},
            {"name": "Clay Bar Treatment", "price_range": "$100–$200"},
            {"name": "Waxing", "price_range": "$100–$200"},
            {"name": "Carpet Deep Cleaning", "price_range": "$50–$100"},
        ]
        for data in addons:
            AddOn.objects.create(**data)

        SiteSettings.objects.update_or_create(
            pk=1,
            defaults={
                "company_name": "Ashes to New Detailing LLC",
                "tagline": "Bringing Back the Shine",
                "phone": "(810) 666-1417",
                "email": "test@gmail.com",
                "service_area": "Genesee County, MI",
                "hours_text": "By Appointment Only",
                "cancellation_policy": "Please give at least 24 hours’ notice to cancel or reschedule. Same-day cancellations may incur a fee up to 50% of the scheduled service; no-shows up to 75%.",
                "weather_policy": "Because we’re mobile, severe weather may require rescheduling. A garage/covered area may be requested for certain services.",
                "heavy_policy": "Heavy soil, excess pet hair, or biohazards may add a surcharge ($25–$75+, based on condition). We’ll confirm any additional charges on-site before work begins.",
                "guarantee_policy": "48-hour satisfaction guarantee. If we miss something, contact us within 48 hours and we’ll make it right.",
                "theme_bg": "#1a1a1a",
                "theme_accent": "#7B2A2A",
            },
        )

        self.stdout.write(self.style.SUCCESS("Initial data seeded."))
