import { useEffect, useState } from 'react';
import { api, SiteSettings } from '../data/api';

export default function Contact() {
  const [settings, setSettings] = useState<SiteSettings | null>(null);
  useEffect(() => {
    document.title = 'Contact';
    api.settings().then(setSettings);
  }, []);
  return (
    <div className="p-4 space-y-4">
      <h1 className="text-3xl mb-4">Contact</h1>
      <p>{settings?.hours_text}</p>
      <div className="space-x-4">
        <a
          className="bg-accent text-white px-4 py-2 rounded"
          href="tel:+18106661417"
        >
          Call to Schedule
        </a>
        <a
          className="bg-gray-700 text-white px-4 py-2 rounded"
          href="mailto:test@gmail.com?subject=Detail%20Inquiry"
        >
          Email for a Quote
        </a>
      </div>
      {settings && (
        <div className="space-y-2 text-sm">
          <p>Service Area: {settings.service_area}</p>
          <p>Cancellation: {settings.cancellation_policy}</p>
          <p>Weather: {settings.weather_policy}</p>
          <p>Heavy Soiling/Pet Hair: {settings.heavy_policy}</p>
          <p>Guarantee: {settings.guarantee_policy}</p>
        </div>
      )}
    </div>
  );
}
