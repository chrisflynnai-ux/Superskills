// Import removed as it was unused

export function SalesPattern() {
  return (
    <section className="py-24 bg-white relative overflow-hidden">
      <div className="max-w-[1000px] mx-auto px-6 relative z-10">
        
        {/* Section Header */}
        <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold mb-6 text-text-primary">
                We Know The Pattern. <br/>
                <span className="text-text-secondary opacity-60">We See It Every Day.</span>
            </h2>
        </div>

        <div className="grid md:grid-cols-2 gap-16 items-center">
            {/* The Story */}
            <div className="space-y-6 text-lg text-text-secondary leading-relaxed">
                <p>
                    She's been to four practitioners before you. She’s "tried everything."
                    She has the supplements. She’s done the elimination diets. She’s spent thousands on functional panels.
                </p>
                <p className="font-medium text-text-primary text-xl">
                    And yet, she is still suffering.
                </p>
                <p>
                    So you do what you were trained to do: You order <em>more</em> comprehensive testing. You dig deeper biochemically. You schedule a follow-up for 3 weeks out.
                </p>
            </div>

            {/* The Gap */}
            <div className="bg-primary p-8 rounded-[var(--radius-minimal)] border border-text-primary/5 shadow-soft">
                <h3 className="text-2xl font-bold mb-4 text-accent-teal">The Brutal Truth About The "Gap"</h3>
                <p className="mb-6 text-text-secondary">
                    In that 3-week silence between labs and results, trust erodes. Anxiety builds. And deep down, you worry the labs might come back "normal" again.
                </p>
                
                <div className="p-4 bg-accent-gold/10 rounded-lg border-l-4 border-accent-gold">
                    <p className="font-bold text-text-primary">It isn't your fault. But it IS a blind spot.</p>
                    <p className="text-sm mt-2 opacity-80">You are missing the Regulatory Layer.</p>
                </div>
            </div>
        </div>
      </div>
    </section>
  );
}
