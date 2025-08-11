import { useEffect, useState } from 'react';
import { api, Service } from '../data/api';
import Card from '../components/Card';

export default function Services() {
  const [services, setServices] = useState<Service[]>([]);
  useEffect(() => {
    document.title = 'Services';
    api.services().then(setServices);
  }, []);
  return (
    <div className="p-4 space-y-4">
      <h1 className="text-3xl mb-4">Services</h1>
      <div className="grid md:grid-cols-3 gap-4">
        {services.map((s) => (
          <Card
            key={s.id}
            title={s.name}
            price={`$${s.starting_price}`}
            items={s.features}
          />
        ))}
      </div>
    </div>
  );
}
