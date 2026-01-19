import { motion, useMotionTemplate, useMotionValue } from "framer-motion";
import type { MouseEvent } from "react";
import { cn } from "@/lib/utils";

interface ButtonProps {
  children: React.ReactNode;
  className?: string;
  onClick?: () => void;
  variant?: 'primary' | 'ghost';
}

export function MagneticButton({ children, className, onClick, variant = 'primary' }: ButtonProps) {
  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);

  function handleMouseMove({ currentTarget, clientX, clientY }: MouseEvent) {
    const { left, top, width, height } = currentTarget.getBoundingClientRect();
    mouseX.set(clientX - left - width / 2);
    mouseY.set(clientY - top - height / 2);
  }

  return (
    <motion.button
      className={cn(
        "relative px-8 py-4 rounded-[var(--radius-minimal)] font-medium transition-colors overflow-hidden group",
        variant === 'primary' 
          ? "bg-accent-teal text-white shadow-soft hover:bg-opacity-90" 
          : "border border-accent-teal text-accent-teal hover:bg-accent-teal/5",
        className
      )}
      onMouseMove={handleMouseMove}
      onMouseLeave={() => {
        mouseX.set(0);
        mouseY.set(0);
      }}
      onClick={onClick}
      whileHover={{ scale: 1.02 }}
      whileTap={{ scale: 0.98 }}
    >
      <motion.div
        className="pointer-events-none absolute -inset-px rounded-xl opacity-0 transition duration-300 group-hover:opacity-100"
        style={{
          background: useMotionTemplate`
            radial-gradient(
              150px circle at ${mouseX}px ${mouseY}px,
              rgba(255,255,255,0.15),
              transparent 80%
            )
          `,
        }}
      />
      {children}
    </motion.button>
  );
}
