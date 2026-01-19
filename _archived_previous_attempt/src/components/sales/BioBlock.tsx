import { motion } from "framer-motion";
import { cn } from "../../lib/utils";

interface BioBlockProps {
  title: string;
  content: React.ReactNode;
  className?: string;
  imageSrc?: string;
}

export function BioBlock({ title, content, className, imageSrc }: BioBlockProps) {
  return (
    <section className={cn("py-20 border-t border-[var(--text-secondary)]/10", className)}>
      <div className="max-w-[var(--container-width)] mx-auto grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          whileInView={{ opacity: 1, x: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <h2 className="text-3xl font-bold mb-8 text-[var(--text-primary)]">{title}</h2>
          <div className="leading-relaxed">
            {content}
          </div>
        </motion.div>

        {imageSrc && (
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="rounded-[var(--radius-minimal)] overflow-hidden shadow-[var(--soft-shadow)]"
          >
             <img src={imageSrc} alt="" className="w-full h-auto object-cover" />
          </motion.div>
        )}
      </div>
    </section>
  );
}
