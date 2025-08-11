const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

async function fetchJSON(path: string) {
  const res = await fetch(`${BASE_URL}${path}`);
  return res.json();
}

export const api = {
  settings: () => fetchJSON('/api/settings/'),
  services: () => fetchJSON('/api/services/'),
  packages: () => fetchJSON('/api/packages/'),
  addons: () => fetchJSON('/api/addons/'),
};

export type Service = {
  id: number;
  name: string;
  slug: string;
  starting_price: number;
  duration_text: string;
  features: string[];
};

export type Package = {
  id: number;
  name: string;
  slug: string;
  starting_price: number;
  duration_text: string;
  includes: string[];
  perfect_for?: string;
};

export type AddOn = {
  id: number;
  name: string;
  price_range: string;
};

export type SiteSettings = {
  company_name: string;
  tagline: string;
  phone: string;
  email: string;
  service_area: string;
  hours_text: string;
  cancellation_policy: string;
  weather_policy: string;
  heavy_policy: string;
  guarantee_policy: string;
  theme_bg: string;
  theme_accent: string;
};
