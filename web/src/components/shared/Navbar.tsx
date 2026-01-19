import { motion, useScroll, useMotionValueEvent } from "framer-motion";
import { useState } from "react";
import { MagneticButton } from "../ui/MagneticButton";

export function Navbar() {
  const { scrollY } = useScroll();
  const [hidden, setHidden] = useState(false);

  useMotionValueEvent(scrollY, "change", (latest) => {
    const previous = scrollY.getPrevious() || 0;
    if (latest > previous && latest > 150) {
      setHidden(true);
    } else {
      setHidden(false);
    }
  });

  return (
    <motion.nav
      variants={{
        visible: { y: 0 },
        hidden: { y: "-100%" },
      }}
      animate={hidden ? "hidden" : "visible"}
      transition={{ duration: 0.35, ease: "easeInOut" }}
      className="fixed top-0 inset-x-0 z-40 bg-primary/80 backdrop-blur-md border-b border-text-secondary/5 h-24 flex items-center"
    >
      <div className="w-full max-w-[1400px] mx-auto px-8 flex items-center justify-between">
        <div className="text-3xl font-heading font-bold tracking-tighter text-text-primary">
          QRX<span className="text-accent-teal">.</span>
        </div>

        <div className="flex items-center gap-4">
            <a href="/" className="text-sm font-medium text-text-secondary hover:text-accent-teal transition-colors">Journal</a>
            <a href="/sales" className="text-sm font-medium text-text-secondary hover:text-accent-teal transition-colors">System</a>
            <MagneticButton className="px-6 py-2 text-sm" onClick={() => window.open('#book', '_blank')}>
                Book Conversation
            </MagneticButton>
        </div>
      </div>
    </motion.nav>
  );
}
