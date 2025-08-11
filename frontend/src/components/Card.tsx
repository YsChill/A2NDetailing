interface CardProps {
  title: string;
  price: string;
  items: string[];
}

export default function Card({ title, price, items }: CardProps) {
  return (
    <div className="bg-charcoal border border-accent rounded p-4 shadow">
      <h3 className="text-xl mb-2 text-accent">{title}</h3>
      <p className="mb-2">{price}</p>
      <ul className="list-disc ml-4 text-sm">
        {items.map((it) => (
          <li key={it}>{it}</li>
        ))}
      </ul>
    </div>
  );
}
