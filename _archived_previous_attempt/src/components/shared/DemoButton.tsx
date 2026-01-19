import { cn } from "../../lib/utils";
import { motion, type HTMLMotionProps } from "framer-motion";


interface DemoButtonProps extends HTMLMotionProps<"button"> {
  children: React.ReactNode;
}

export function DemoButton({ children, className, ...props }: DemoButtonProps) {
  return (
    <motion.button
      whileHover={{ scale: 1.02 }}
      whileTap={{ scale: 0.98 }}
      className={cn(
        "px-6 py-3 flex items-center gap-3 bg-[var(--bg-primary)] border border-[var(--text-secondary)] text-[var(--text-primary)] rounded-[var(--radius-minimal)] font-medium shadow-[var(--soft-shadow)] transition-all",
        className
      )}
      {...props}
    >
      <span className="flex items-center justify-center w-8 h-8 rounded-full bg-[var(--accent-teal)] bg-opacity-10 text-[var(--accent-teal)]">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="lucide lucide-play"><polygon points="6 3 20 12 6 21 6 3"/></svg>
      </span>
      {children}
    </motion.button>
  );
}
