import { Layout } from "../shared/Layout";
import { BioBlock } from "./BioBlock";
import { SalesHero } from "./SalesHero";
import { CTASection } from "./CTASection";

export function SalesPage() {
  return (
    <Layout>
      <SalesHero />

      <BioBlock 
        title="The Pattern You've Probably Seen Too Many Times"
        content={
          <div className="space-y-6 text-lg text-[var(--text-primary)]">
            <p>She's been to four practitioners before you. Spent thousands on specialty labs. Tried elimination diets, supplement protocols, hormone support. Nothing quite worked.</p>
            <p>She's frustrated. You're determined to help. So you do what you were trained to do: order comprehensive testing, review results, build protocol.</p>
            <p>It's thorough. It's evidence-based. It's professional. <strong>But it's slow.</strong></p>
            <p className="font-medium text-[var(--accent-teal)]">But here's what matters: She wants answers now. And whoever gives them to her — with credibility — earns her loyalty.</p>
          </div>
        }
        imageSrc="/assets/WEB IMAGES/Picture3.png"
      />

      <BioBlock 
        title="The Shift That's Already Happening"
        className="bg-white"
        content={
          <div className="space-y-6 text-lg text-[var(--text-primary)]">
            <p>A growing number of functional medicine practitioners, naturopaths, and integrative clinics have adopted a different approach entirely. They've added one thing that's changing everything:</p>
            <p className="text-xl font-bold bg-[var(--bg-primary)] p-6 rounded-[var(--radius-minimal)] border-l-4 border-[var(--accent-teal)]">
                The ability to observe, support, and begin a reset — in the first visit.
            </p>
            <p>With <strong>biofield observation</strong> — technology that reads electromagnetic patterns from hundreds of organs, tissues, and systems — and delivers actionable insights before the client leaves your office.</p>
          </div>
        }
        imageSrc="/assets/WEB IMAGES/Picture4.png"
      />

      <BioBlock 
        title="The Mechanism: Resonance Medicine"
        content={
            <div className="space-y-6 text-lg text-[var(--text-primary)]">
                <p>Most holistic practitioners already work with two clinical lenses: Client story & symptoms, and Labs & imaging.</p>
                <p><strong>Resonance Medicine adds a third: Field-level stress and regulation patterns.</strong></p>
                <p>We know now that the body has an electromagnetic field. An information field. A biofield. It's not woo-woo anymore. It's measurable. It's physics. It's real science.</p>
                <p>These fields often show patterns of stress and disruption <em>long before</em> they show up as a clear diagnosis on a lab panel. This is the <strong>regulatory layer</strong>.</p>
                <p><strong>We've been treating downstream. The upstream pattern is still running.</strong></p>
            </div>
        }
        imageSrc="/assets/WEB IMAGES/Picture5.png"
      />

      <section className="py-24 bg-[var(--text-primary)] text-white">
        <div className="max-w-[var(--container-width)] mx-auto px-8">
            <h2 className="text-3xl font-bold mb-12 text-center">The System: Scan • Support • Reset</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-12 text-center">
                <div className="p-8 bg-white/5 rounded-[var(--radius-minimal)] border border-white/10">
                    <h3 className="text-xl font-bold mb-4 text-[var(--accent-teal)]">SCAN</h3>
                    <p className="opacity-90">In 20 minutes, observe stress patterns across hundreds of organs. Identify regulatory disruption correlating with imbalance.</p>
                </div>
                <div className="p-8 bg-white/5 rounded-[var(--radius-minimal)] border border-white/10">
                    <h3 className="text-xl font-bold mb-4 text-[var(--accent-teal)]">SUPPORT</h3>
                    <p className="opacity-90">Deliver supportive scalar frequencies directly into the biofield. Support natural self-regulation in the same session.</p>
                </div>
                <div className="p-8 bg-white/5 rounded-[var(--radius-minimal)] border border-white/10">
                    <h3 className="text-xl font-bold mb-4 text-[var(--accent-teal)]">RESET</h3>
                    <p className="opacity-90">Plug insights into a structured wellness program focusing on detox, mitochondrial resilience, and nervous system regulation.</p>
                </div>
            </div>
        </div>
      </section>

      <BioBlock 
        title="Hybrid Intelligence: Labs + Field"
        content={
            <div className="space-y-6 text-lg text-[var(--text-primary)]">
                <p>QRX wasn't created to replace functional testing. <strong>It was created to guide it.</strong></p>
                <p>Step 1: Observe the field to find stress patterns.<br/>Step 2: Start supportive frequency programs immediately.<br/>Step 3: Use functional testing strategically to confirm.</p>
                <p>We're not interested in throwing out good science. We're interested in giving practitioners a smarter way to use it.</p>
            </div>
        }
        className="bg-white"
        imageSrc="/assets/WEB IMAGES/Picture6.png"
      />

      <BioBlock 
        title="The Referral Engine"
        content={
            <div className="space-y-6 text-lg text-[var(--text-primary)]">
                <p>"Seeing is believing." When clients can see their patterns, watch you address them, and feel tangible progress — they become your most powerful referral engine.</p>
                <ul className="space-y-2 font-medium">
                    <li className="flex items-center gap-3"><span className="text-[var(--accent-teal)]">✓</span> 70-85% new clients from referrals</li>
                    <li className="flex items-center gap-3"><span className="text-[var(--accent-teal)]">✓</span> Calendars booked 4-6 weeks out</li>
                    <li className="flex items-center gap-3"><span className="text-[var(--accent-teal)]">✓</span> 40-60% conversion to programs</li>
                </ul>
            </div>
        }
         imageSrc="/assets/WEB IMAGES/Picture7.png"
      />

      <BioBlock 
        title="Three Clinical Advantages"
        content={
            <div className="space-y-6 text-lg text-[var(--text-primary)]">
                <p><strong>1. Handle the "Unsolvable" Cases:</strong> The patients who've "tried everything" become your specialty because you can see what others missed.</p>
                <p><strong>2. Faster Results:</strong> Because you support on visit one, momentum builds immediately. Compliance increases because they <em>felt</em> it working.</p>
                <p><strong>3. True Differentiation:</strong> In a crowded market, you stand out not with better SEO, but through results clients can see and feel.</p>
            </div>
        }
        className="bg-white"
        imageSrc="/assets/WEB IMAGES/Picture8.png"
      />

      <section className="py-24 bg-[var(--bg-primary)]">
        <div className="max-w-4xl mx-auto px-6 text-center">
            <h2 className="text-3xl font-bold mb-12 text-[var(--text-primary)]">What Practitioners Are Saying</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div className="p-8 bg-white rounded-[var(--radius-minimal)] shadow-[var(--soft-shadow)] text-left">
                    <p className="italic text-[var(--text-secondary)] mb-6">"My waiting list is three months long now. And 85% of my new patients come from word-of-mouth. Not because of marketing. Because they see what's happening."</p>
                    <div className="font-bold text-[var(--text-primary)]">— Dr. Sarah Chen, Functional Medicine</div>
                </div>
                 <div className="p-8 bg-white rounded-[var(--radius-minimal)] shadow-[var(--soft-shadow)] text-left">
                    <p className="italic text-[var(--text-secondary)] mb-6">"Before QRX, I was spending $3,000 a month on ads. Now I spend $200 and I'm booked six weeks out. My patients have become my best marketing team."</p>
                    <div className="font-bold text-[var(--text-primary)]">— Michael Torres, DC</div>
                </div>
            </div>
        </div>
      </section>

      <CTASection />
      
    </Layout>
  );
}
