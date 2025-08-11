import { useEffect } from 'react';

export default function About() {
  useEffect(() => {
    document.title = 'About';
  }, []);
  return (
    <div className="p-4 space-y-4">
      <h1 className="text-3xl mb-4">About Us</h1>
      <p>
        Ashes to New Detailing is a mobile detailing service bringing back the
        shine across Genesee County. We come to you and treat every vehicle as
        if it were our own.
      </p>
      <ol className="list-decimal ml-6 space-y-1">
        <li>Book your appointment</li>
        <li>We arrive equipped and ready</li>
        <li>Your car is refreshed and shining</li>
      </ol>
    </div>
  );
}
