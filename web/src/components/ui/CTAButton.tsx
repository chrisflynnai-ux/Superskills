import { motion } from 'framer-motion';
import type { ButtonHTMLAttributes } from 'react';
import { ctaHover } from '../../lib/motion_variants.js';

interface CTAButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary';
  isLoading?: boolean;
}

export function CTAButton({ 
  children, 
  variant = 'primary', 
  isLoading = false,
  className = '',
  ...props 
}: CTAButtonProps) {
  const baseStyles = "relative px-8 py-3 rounded-button font-body font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-accent focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed";
  
  const variants = {
    primary: "bg-accent text-primary shadow-md hover:shadow-lg",
    secondary: "bg-transparent border-2 border-accent text-accent hover:bg-accent/10"
  };

  return (
    <motion.button
      className={`${baseStyles} ${variants[variant]} ${className}`}
      variants={ctaHover}
      whileHover="whileHover"
      whileTap="whileTap"
      disabled={isLoading || props.disabled}
      {...props as any}
    >
      {isLoading ? (
        <div className="flex items-center justify-center">
          <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-current" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          Loading...
        </div>
      ) : children}
    </motion.button>
  );
}
