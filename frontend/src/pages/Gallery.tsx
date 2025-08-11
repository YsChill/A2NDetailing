import { useState } from 'react';

const images = [
  'https://placehold.co/1200x800?text=Before',
  'https://placehold.co/1200x800?text=After',
];

export default function Gallery() {
  const [active, setActive] = useState<string | null>(null);
  return (
    <div className="p-4">
      <h1 className="text-3xl mb-4">Gallery</h1>
      <div className="columns-2 md:columns-3 gap-2">
        {images.map((src) => (
          <img
            key={src}
            src={src}
            className="mb-2 cursor-pointer rounded"
            onClick={() => setActive(src)}
          />
        ))}
      </div>
      {active && (
        <div
          className="fixed inset-0 bg-black/80 flex items-center justify-center"
          onClick={() => setActive(null)}
        >
          <img src={active} className="max-h-full max-w-full" />
        </div>
      )}
    </div>
  );
}
