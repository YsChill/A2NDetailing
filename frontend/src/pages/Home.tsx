import { useEffect, useState } from 'react';
import { api, Package, SiteSettings } from '../data/api';
import Card from '../components/Card';

export default function Home() {
  const [settings, setSettings] = useState<SiteSettings | null>(null);
  const [packages, setPackages] = useState<Package[]>([]);

  useEffect(() => {
    api.settings().then(setSettings);
    api.packages().then(setPackages);
  }, []);

  useEffect(() => {
    if (settings) {
      document.title = settings.tagline;
    }
  }, [settings]);

  return (
    <div className="space-y-8 p-4">
      <div className="text-center space-y-4">
        <img
          src="https://placehold.co/128x128?text=Logo"
          alt="logo"
          className="w-32 mx-auto"
        />
        <h1 className="text-3xl">{settings?.tagline}</h1>
        <div className="flex justify-center space-x-4 text-sm text-gray-400">
          <span>Mobile Only</span>
          <span>Genesee County, MI</span>
          <span>By Appointment</span>
        </div>
      </div>

      <div>
        <h2 className="text-2xl mb-4">Featured Packages</h2>
        <div className="grid md:grid-cols-3 gap-4">
          {packages.map((p) => (
            <Card
              key={p.id}
              title={p.name}
              price={`$${p.starting_price}`}
              items={p.includes}
            />
          ))}
        </div>
      </div>

      <div className="text-center bg-accent text-white p-4 rounded">
        <p>Ready to bring back the shine?</p>
        <a href="tel:+18106661417" className="underline">
          Call (810) 666-1417
        </a>
      </div>

      {settings && (
        <script type="application/ld+json">
          {JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'Service',
            serviceType: 'Mobile Auto Detailing',
            areaServed: settings.service_area,
            telephone: settings.phone,
          })}
        </script>
      )}
    </div>
  );
}
