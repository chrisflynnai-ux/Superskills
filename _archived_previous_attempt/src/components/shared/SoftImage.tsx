import { cn } from "../../lib/utils";
import { motion, type HTMLMotionProps } from "framer-motion";

interface SoftImageProps extends HTMLMotionProps<"img"> {
  src: string;
  alt: string;
}

export function SoftImage({ src, alt, className, ...props }: SoftImageProps) {
  return (
    <motion.img
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
      transition={{ duration: 0.8, ease: "easeOut" }}
      src={src}
      alt={alt}
      className={cn(
        "editorial-img object-cover",
        className
      )}
      {...props}
    />
  );
}
