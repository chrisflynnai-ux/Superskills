

export function EditorialContent() {
  return (
    <section className="max-w-[1400px] mx-auto px-6 grid grid-cols-12 gap-12 pb-32">
        <div className="col-span-12 md:col-span-4 relative hidden md:block">
            <div className="sticky top-32">
              <img 
                src="/assets/official/advertorial/image2.png" 
                alt="System Detail" 
                className="w-full aspect-[3/4] object-cover rounded-[var(--radius-minimal)] shadow-soft grayscale hover:grayscale-0 transition-all duration-700" 
              />
              <p className="mt-4 text-xs font-medium text-text-secondary uppercase tracking-widest text-right">Fig 1.0 — Regulatory Scan</p>
            </div>
        </div>
        
        <div className="col-span-12 md:col-span-7 md:col-start-6">
            <div className="prose prose-lg prose-slate text-text-primary prose-headings:font-heading prose-headings:font-bold prose-p:text-lg prose-p:leading-relaxed max-w-none">
                <p>If you work with complex chronic illness, you know the pattern.</p>
                <p>A client walks in exhausted, brain-fogged, carrying a folder thick with lab results. Her numbers are "mostly fine." Her symptoms are anything but. You run more tests. Tweak the protocol. Weeks pass.</p>
                <p>She looks you in the eye and says: <em>"I don't think I feel any better."</em></p>
                
                <h3>The Blind Spot in Standard Testing</h3>
                <p>Here's what most practitioners don't talk about openly: Standard testing — even good functional testing — has significant blind spots.</p>
                <ul>
                    <li><strong>Parasites?</strong> False negative rates run 50-70%.</li>
                    <li><strong>Heavy metals?</strong> Blood work misses deep tissue storage.</li>
                    <li><strong>System-wide patterns?</strong> Most testing is single-focus snapshots.</li>
                </ul>
                
                <h3>Asking a Different Question</h3>
                <p>Instead of only asking, "What does the blood say?" — she started asking, <strong>"What does the biofield say?"</strong></p>
                <p>It's not fringe science anymore. It's measurable physics. And this "regulatory layer" often shows patterns of stress long before they appear on a lab panel.</p>
            </div>
        </div>
    </section>
  );
}
