import { motion } from "framer-motion";
import { PrimaryButton } from "../shared/PrimaryButton";
import { DemoButton } from "../shared/DemoButton";

export function CTASection() {
  return (
    <section className="py-24 bg-[var(--bg-primary)] border-t border-[var(--text-secondary)]/10">
      <div className="max-w-4xl mx-auto text-center">
        <motion.h2
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-4xl font-bold mb-8"
        >
          See the "Third Lens" in Action
        </motion.h2>
        <p className="text-xl text-[var(--text-secondary)] mb-12 max-w-2xl mx-auto">
          Watch the 20-minute clinical demonstration or speak with our AI agent to see if this matches your practice goals.
        </p>
        
        <div className="flex flex-col sm:flex-row items-center justify-center gap-6">
           <DemoButton onClick={() => window.open('#demo', '_blank')}>
                Watch Clinical Demo
            </DemoButton>
            <PrimaryButton onClick={() => window.open('#book', '_blank')}>
                Book a Strategy Call
            </PrimaryButton>
        </div>
      </div>
    </section>
  );
}
