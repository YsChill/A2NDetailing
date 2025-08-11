import { useEffect, useState } from 'react';
import { api, Package } from '../data/api';
import Card from '../components/Card';

export default function Packages() {
  const [packages, setPackages] = useState<Package[]>([]);
  useEffect(() => {
    document.title = 'Packages';
    api.packages().then(setPackages);
  }, []);
  return (
    <div className="p-4 space-y-4">
      <h1 className="text-3xl mb-4">Packages</h1>
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
  );
}
