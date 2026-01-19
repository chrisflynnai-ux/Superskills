import { cn } from "../../lib/utils";
import { motion, type HTMLMotionProps } from "framer-motion";

interface PrimaryButtonProps extends HTMLMotionProps<"button"> {
  children: React.ReactNode;
}

export function PrimaryButton({ children, className, ...props }: PrimaryButtonProps) {
  return (
    <motion.button
      whileHover={{ scale: 1.02, opacity: 0.9 }}
      whileTap={{ scale: 0.98 }}
      className={cn(
        "px-8 py-4 bg-[var(--accent-teal)] text-white rounded-[var(--radius-minimal)] font-bold shadow-[var(--soft-shadow)] transition-all",
        className
      )}
      {...props}
    >
      {children}
    </motion.button>
  );
}
