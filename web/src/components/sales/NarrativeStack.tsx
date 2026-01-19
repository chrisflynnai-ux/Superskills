import { motion } from 'framer-motion';
import { sectionReveal, quantumPulse } from '../../lib/motion_variants.js';
import { CTAButton } from '../ui/CTAButton.js';

interface NarrativeStackProps {
  slides: string[];
}

export function NarrativeStack({ slides }: NarrativeStackProps) {
  // We start from slide 2 (index 1 in the array if slide 1 is Hero)
  // But pass in the sliced array of "remaining slides" to this component.
  
  return (
    <div className="flex flex-col w-full bg-surface">
      {slides.map((slide, index) => {
        // Correct slide number context (assuming passed slides start from Slide 2)
        const slideNumber = index + 2; 
        const isQuantumScan = slideNumber === 6;
        
        // Strategic CTA placement (Second half of deck)
        // Placing regular reminders to convert
        const showCTA = [10, 15, 20, 24].includes(slideNumber);

        return (
          <motion.section
            key={slide}
            className="relative w-full overflow-hidden"
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: 0.2 }}
            variants={sectionReveal}
          >
            {/* Slide Image */}
            <motion.img
              src={`/assets/${slide}`}
              alt={`Presentation Slide ${slideNumber}`}
              className="w-full h-auto object-cover"
              // Apply Pulse effect specifically to Slide 6
              variants={isQuantumScan ? quantumPulse : undefined}
              animate={isQuantumScan ? "animate" : undefined}
            />

            {/* Injected CTA Overlay */}
            {showCTA && (
              <div className="absolute bottom-12 left-0 right-0 flex justify-center pb-8 z-10">
                <CTAButton 
                  onClick={() => window.open('https://calendly.com/placeholder', '_blank')}
                  className="shadow-2xl"
                >
                  Book a Call
                </CTAButton>
              </div>
            )}
          </motion.section>
        );
      })}
    </div>
  );
}
