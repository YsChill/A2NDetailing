import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav className="bg-charcoal text-white p-4 flex justify-between">
      <Link to="/" className="font-bold">Ashes to New Detailing</Link>
      <div className="space-x-4">
        <Link to="/services">Services</Link>
        <Link to="/packages">Packages</Link>
        <Link to="/gallery">Gallery</Link>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
      </div>
    </nav>
  );
}
