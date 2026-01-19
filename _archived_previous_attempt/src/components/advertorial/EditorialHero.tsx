
import { motion } from "framer-motion";
import { SoftImage } from "../shared/SoftImage";
import { PrimaryButton } from "../shared/PrimaryButton";
import { DemoButton } from "../shared/DemoButton";

export function EditorialHero() {
  return (
    <section className="pt-32 pb-16">
      <div className="max-w-4xl mx-auto text-center mb-12">
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="text-[var(--accent-teal)] font-bold tracking-widest text-sm uppercase mb-6"
        >
          Health Insights | Discovery Series
        </motion.div>
        
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.1 }}
          className="text-[var(--h1-size)] leading-[1.1] font-bold text-[var(--text-primary)] mb-8"
        >
          The "Third Lens" That's Helping Holistic Practitioners See What Labs Miss
        </motion.h1>

        <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="flex flex-col sm:flex-row items-center justify-center gap-4 mt-8"
        >
            <DemoButton onClick={() => console.log('Watch Demo')}>
                Watch Demo Video
            </DemoButton>
            <PrimaryButton onClick={() => console.log('Book Call')}>
                Book a Call
            </PrimaryButton>
        </motion.div>
      </div>

      <div className="max-w-[var(--container-width)] mx-auto relative">
        <SoftImage 
          src="/assets/WEB IMAGES/Picture2.png" 
          alt="Practitioner analyzing biofield data"
          className="w-full aspect-[21/9] object-cover"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-[var(--bg-primary)] via-transparent to-transparent opacity-20 pointer-events-none rounded-[var(--radius-minimal)]" />
      </div>
    </section>
  );
}
