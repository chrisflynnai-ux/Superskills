import { useState } from 'react';
import { motion } from 'framer-motion';
import { CTAButton } from '../ui/CTAButton.js';
import { Play } from 'lucide-react';

interface HeroSectionProps {
  slideImage: string;
}

export function HeroSection({ slideImage }: HeroSectionProps) {
  const [isPlaying, setIsPlaying] = useState(false);

  return (
    <section className="relative w-full min-h-screen flex flex-col items-center justify-center overflow-hidden bg-primary">
      {/* Background Slide */}
      <div className="absolute inset-0 z-0">
        <img 
          src={`/assets/${slideImage}`} 
          alt="Hero Background" 
          className="w-full h-full object-cover opacity-90"
        />
        {/* Clinical Overlay to ensure text/video pops */}
        <div className="absolute inset-0 bg-primary/20 backdrop-blur-[2px]" />
      </div>

      {/* VSL Container */}
      <motion.div 
        className="relative z-10 w-full max-w-5xl aspect-video bg-black rounded-card shadow-2xl border border-white/10 overflow-hidden group cursor-pointer"
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.8, delay: 0.2 }}
        onClick={() => setIsPlaying(true)}
      >
        {!isPlaying ? (
          <div className="absolute inset-0 flex flex-col items-center justify-center bg-black/40 group-hover:bg-black/30 transition-all">
            <motion.div
              whileHover={{ scale: 1.1 }}
              className="w-20 h-20 bg-white/10 backdrop-blur-md rounded-full flex items-center justify-center border border-white/20 shadow-glow"
            >
              <Play className="w-8 h-8 text-white ml-1" fill="currentColor" />
            </motion.div>
            <span className="mt-4 text-white font-heading font-semibold tracking-wider uppercase text-sm">
              Watch 20 Min Clinical Demonstration
            </span>
          </div>
        ) : (
          <div className="w-full h-full flex items-center justify-center bg-black text-white">
            {/* Placeholder for iframe / video player */}
            <p>VSL Internal Video Player Loading...</p>
          </div>
        )}
      </motion.div>

      {/* Primary CTAs */}
      <motion.div 
        className="relative z-10 mt-12 flex flex-col md:flex-row gap-6"
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.8, delay: 0.4 }}
      >
        <CTAButton 
          onClick={() => setIsPlaying(true)}
        >
          Watch 20 Minute Demo
        </CTAButton>
        <CTAButton 
          variant="secondary"
          onClick={() => window.open('https://calendly.com/placeholder', '_blank')}
          className="bg-white/5 border-white/20 text-white hover:bg-white/10 backdrop-blur-sm"
        >
          Book a Call
        </CTAButton>
      </motion.div>
    </section>
  );
}
