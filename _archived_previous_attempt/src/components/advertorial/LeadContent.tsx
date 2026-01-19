import { motion } from "framer-motion";

export function LeadContent() {
  return (
    <section className="pt-8 pb-16 max-w-3xl mx-auto">
      <div className="space-y-6 text-xl text-[var(--text-primary)] leading-relaxed">
        <p>
          If you work with complex chronic illness, you know the pattern.
        </p>
        <p>
          A client walks in exhausted, brain-fogged, carrying a folder thick with lab results from four other practitioners. Her numbers are "mostly fine." Her symptoms are anything but.
        </p>
        <p>
          You run more tests. Tweak the protocol. Add another supplement. Weeks pass.
        </p>
        <p>
          She looks you in the eye and says what you've heard too many times:
          <span className="italic block mt-2">"I don't think I feel any better."</span>
        </p>
      </div>

      <motion.div
        initial={{ opacity: 0, x: -20 }}
        whileInView={{ opacity: 1, x: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.8 }}
        className="my-16 pl-8 border-l-4 border-[var(--accent-teal)] py-4"
      >
        <blockquote className="text-2xl font-bold text-[var(--accent-teal)] leading-snug">
          "It's not that you're doing anything wrong. It's not that functional medicine doesn't work. It's that something is being missed."
        </blockquote>
      </motion.div>

      <div className="space-y-6 text-xl text-[var(--text-primary)] leading-relaxed">
        <h2 className="text-3xl font-bold text-[var(--text-primary)] mt-12 mb-6">WHY LABS AREN'T ENOUGH</h2>
        <p>
          Here's what most practitioners don't talk about openly: Standard testing — even good functional testing — has significant blind spots.
        </p>
        <ul className="space-y-4 ml-4">
            <li><strong>Parasites?</strong> False negative rates run 50-70%.</li>
            <li><strong>Heavy metals?</strong> Blood work misses deep tissue storage.</li>
            <li><strong>Chronic infections?</strong> Dormant viruses often fly under the radar.</li>
        </ul>
        <p className="mt-6">
            This is why complex cases feel so difficult. You're making decisions with incomplete information.
        </p>
      </div>
    </section>
  );
}
