// import { ReactLenis } from '@studio-freight/react-lenis';
import { Navbar } from './Navbar';
import { ScrollProgress } from '../ui/ScrollProgress';

interface LayoutProps {
  children: React.ReactNode;
}

export function Layout({ children }: LayoutProps) {
  return (
    // <ReactLenis root>
      <div className="min-h-screen bg-primary text-primary selection:bg-accent-teal selection:text-white">
        <ScrollProgress />
        <Navbar />
        <main className="w-full relative z-10">
          {children}
        </main>
        <footer className="py-24 bg-text-primary text-white border-t border-white/10 mt-32">
            <div className="max-w-7xl mx-auto px-6 text-center opacity-60">
                <p>&copy; 2026 QRX Quantum Resonance™. Editorial Discovery Suite.</p>
            </div>
        </footer>
      </div>
    // </ReactLenis>
  );
}
