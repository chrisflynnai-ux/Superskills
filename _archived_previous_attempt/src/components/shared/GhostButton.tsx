import { cn } from "../../lib/utils";
import { motion, type HTMLMotionProps } from "framer-motion";

interface GhostButtonProps extends HTMLMotionProps<"button"> {
  children: React.ReactNode;
}

export function GhostButton({ children, className, ...props }: GhostButtonProps) {
  return (
    <motion.button
      whileHover={{ scale: 1.02, backgroundColor: "rgba(26, 95, 122, 0.05)" }}
      whileTap={{ scale: 0.98 }}
      className={cn(
        "px-6 py-3 border border-[var(--accent-teal)] text-[var(--accent-teal)] rounded-[var(--radius-minimal)] font-medium transition-colors",
        className
      )}
      {...props}
    >
      {children}
    </motion.button>
  );
}
