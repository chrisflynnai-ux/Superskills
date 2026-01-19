import { motion } from "framer-motion";
import { PrimaryButton } from "../shared/PrimaryButton";
import { DemoButton } from "../shared/DemoButton";

export function SalesHero() {
  return (
    <section className="pt-32 pb-20 relative overflow-hidden">
      <div className="max-w-5xl mx-auto px-6 text-center relative z-10">
        <motion.h1 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="text-[var(--h1-size)] font-bold mb-8 leading-tight text-[var(--text-primary)]"
        >
          Finally See What You've Been Missing
        </motion.h1>
        
        <motion.p 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="text-xl md:text-2xl text-[var(--text-secondary)] mb-12 leading-relaxed max-w-3xl mx-auto"
        >
          How a growing number of holistic practitioners are turning their most complex cases into their strongest referral sources — using biofield technology that observes, supports, and resets in a single 90-minute session.
        </motion.p>

        {/* Video Placeholder */}
        <motion.div
           initial={{ opacity: 0, scale: 0.95 }}
           animate={{ opacity: 1, scale: 1 }}
           transition={{ duration: 0.6, delay: 0.4 }}
           className="aspect-video bg-black/5 rounded-[var(--radius-minimal)] shadow-[var(--soft-shadow)] mb-12 flex items-center justify-center border border-[var(--text-primary)]/5"
        >
            <div className="text-[var(--text-secondary)] font-medium flex flex-col items-center gap-4">
                <div className="w-16 h-16 rounded-full bg-[var(--accent-teal)]/10 flex items-center justify-center text-[var(--accent-teal)]">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polygon points="6 3 20 12 6 21 6 3"/></svg>
                </div>
                <span>VSL Medium-Form 2:30 Payload</span>
            </div>
        </motion.div>

        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.6 }}
            className="flex flex-col sm:flex-row items-center justify-center gap-6"
        >
            <DemoButton onClick={() => window.open('#demo', '_blank')}>
                Watch Clinical Demonstration
            </DemoButton>
            <PrimaryButton onClick={() => window.open('#book', '_blank')}>
                Book a Conversation
            </PrimaryButton>
        </motion.div>
      </div>
      
      {/* Background Gradient */}
      <div className="absolute top-0 left-0 right-0 h-[600px] bg-gradient-to-b from-[var(--bg-primary)] via-white to-[var(--bg-primary)] -z-10" />
    </section>
  );
}
