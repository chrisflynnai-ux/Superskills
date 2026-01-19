
import { motion } from "framer-motion";
import { PrimaryButton } from "./PrimaryButton";

export function Navbar() {


  return (
    <motion.nav 
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      transition={{ duration: 0.6 }}
      className="fixed top-0 left-0 right-0 z-50 bg-[var(--bg-primary)]/80 backdrop-blur-md border-b border-[var(--text-secondary)]/10"
    >
      <div className="max-w-[var(--container-width)] mx-auto px-8 h-20 flex items-center justify-between">
        <div className="text-2xl font-bold text-[var(--text-primary)] tracking-tight">
          QRX<span className="text-[var(--accent-teal)]">.</span>
        </div>
        
        <div className="hidden md:flex items-center gap-8">
          <button onClick={() => window.location.href='/'} className="text-[var(--text-secondary)] hover:text-[var(--accent-teal)] transition-colors text-sm font-medium">Advertorial</button>
          <button onClick={() => window.location.href='/sales'} className="text-[var(--text-secondary)] hover:text-[var(--accent-teal)] transition-colors text-sm font-medium">Sales Page</button>
          <button onClick={() => document.getElementById('discovery')?.scrollIntoView({ behavior: 'smooth' })} className="text-[var(--text-secondary)] hover:text-[var(--accent-teal)] transition-colors text-sm font-medium">Discovery</button>
        </div>

        <div className="flex items-center gap-4">
          <PrimaryButton onClick={() => window.open('#book', '_blank')} className="px-5 py-2 text-sm">
            Book a Call
          </PrimaryButton>
        </div>
      </div>
    </motion.nav>
  );
}
