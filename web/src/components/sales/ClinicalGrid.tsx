

export function ClinicalGrid() {
  return (
    <section className="py-32 bg-primary">
      <div className="max-w-[1400px] mx-auto px-6 mb-24">
         <h2 className="text-5xl font-bold mb-6">Three Clinical Advantages</h2>
         <p className="text-xl text-text-secondary max-w-2xl">Why practitioners who adopt the regulatory lens become the go-to experts in their community.</p>
      </div>

      <div className="max-w-[1400px] mx-auto px-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
         {/* Card 1 */}
         <div className="group relative bg-white p-8 rounded-[var(--radius-minimal)] shadow-soft overflow-hidden">
            <div className="h-64 mb-8 overflow-hidden rounded-lg">
                 <img src="/assets/official/sales/image6.png" className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" />
            </div>
            <h3 className="text-2xl font-bold mb-4">1. Handle "Unsolvable" Cases</h3>
            <p className="text-text-secondary leading-relaxed">
                The patients who've "tried everything" become your specialty. You see the stress patterns correlating with parasitic activity or toxic load that standard labs missed.
            </p>
         </div>

         {/* Card 2 */}
         <div className="group relative bg-white p-8 rounded-[var(--radius-minimal)] shadow-soft overflow-hidden mt-12">
            <div className="h-64 mb-8 overflow-hidden rounded-lg">
                 <img src="/assets/official/sales/image10.png" className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" />
            </div>
             <h3 className="text-2xl font-bold mb-4">2. Faster Results</h3>
            <p className="text-text-secondary leading-relaxed">
                Momentum builds immediately because you support on visit one. Compliance increases because they <em>felt</em> it working before they left the office.
            </p>
         </div>

         {/* Card 3 */}
         <div className="group relative bg-white p-8 rounded-[var(--radius-minimal)] shadow-soft overflow-hidden">
            <div className="h-64 mb-8 overflow-hidden rounded-lg">
                 <img src="/assets/official/sales/image11.jpeg" className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" />
            </div>
             <h3 className="text-2xl font-bold mb-4">3. True Differentiation</h3>
            <p className="text-text-secondary leading-relaxed">
                Stand out not with better SEO, but through results clients can see. When clients show their "before and after" scans to skeptical family members, it’s game over.
            </p>
         </div>
      </div>
    </section>
  );
}
