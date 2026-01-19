import { cn } from "../../lib/utils";
import { Navbar } from "./Navbar";

interface LayoutProps {
  children: React.ReactNode;
  className?: string;
}

export function Layout({ children, className }: LayoutProps) {
  return (
    <div className="min-h-screen bg-[var(--bg-primary)] text-[var(--text-primary)] font-sans antialiased overflow-x-hidden selection:bg-[var(--accent-teal)] selection:text-white">
      <Navbar />
      <main className={cn("pt-24", className)}>
        {children}
      </main>
      <footer className="py-12 border-t border-[var(--text-secondary)]/10 mt-20">
        <div className="max-w-[var(--container-width)] mx-auto px-8 text-center text-[var(--text-secondary)] text-sm">
          © 2026 QRX. All rights reserved.
        </div>
      </footer>
    </div>
  );
}
