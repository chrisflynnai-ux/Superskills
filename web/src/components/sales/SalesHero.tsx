import { MagneticButton } from "../ui/MagneticButton";

export function SalesHero() {
  return (
    <section className="min-h-screen relative pt-32 flex items-center justify-center overflow-hidden">
        {/* Background Image Parallax */}
        <div className="absolute inset-0 z-0">
             <img src="/assets/official/sales/image1.jpeg" className="w-full h-full object-cover opacity-10" />
             <div className="absolute inset-0 bg-gradient-to-b from-bg-primary via-bg-primary/50 to-bg-primary" />
        </div>

        <div className="relative z-10 max-w-5xl mx-auto px-6 text-center">
            <div className="mb-6 inline-block px-4 py-1.5 rounded-full border border-accent-gold/30 bg-accent-gold/5 backdrop-blur-sm">
                <span className="text-xs md:text-sm font-bold tracking-widest text-accent-gold uppercase">
                    Attention: Functional Care & Wellness Professionals
                </span>
            </div>

            <h1 
                className="text-5xl md:text-7xl font-bold mb-8 tracking-tight text-text-primary leading-[1.1]"
            >
                You Are Missing The Most <br/>
                <span className="text-accent-teal">Critical Piece</span> of The <br/>
                Clinical Puzzle.
            </h1>
            
            <p className="text-xl md:text-2xl text-text-secondary max-w-3xl mx-auto mb-12 leading-relaxed">
                While you wait weeks for lab results, your most complex patients are losing patience—and trust. Here is the "Third Lens" that allows you to see the invisible and turn your toughest cases into your strongest referral engine.
            </p>

            <div className="flex flex-col md:flex-row items-center justify-center gap-6">
                 <MagneticButton onClick={() => document.getElementById('demo')?.scrollIntoView({ behavior: 'smooth' })}>
                    Watch Clinical Demonstration
                 </MagneticButton>
                 <MagneticButton variant="ghost" onClick={() => window.open('https://cal.com/jim-qrx/audit', '_blank')}>
                    Book Peer Conversation
                 </MagneticButton>
            </div>
            
             {/* VSL #2: THE MEDIUM (2:30) - "THE BRIDGE" */}
             <div 
                id="demo"
                className="mt-24 rounded-2xl overflow-hidden shadow-2xl border border-text-secondary/10 group cursor-pointer relative"
                onClick={() => window.open('https://vimeo.com/qrx/medium-vsl', '_blank')}
             >
                <div className="w-full aspect-video bg-black/5 flex flex-col items-center justify-center relative">
                    <img 
                        src="/assets/official/sales/image5.jpeg" 
                        alt="Clinical Demonstration Preview" 
                        className="absolute inset-0 w-full h-full object-cover opacity-50 group-hover:scale-105 transition-transform duration-700"
                    />
                    <div className="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-colors duration-500" />
                    
                    <div className="w-20 h-20 rounded-full bg-white/10 backdrop-blur-md flex items-center justify-center border border-white/20 z-10 group-hover:scale-110 transition-transform duration-300">
                        <div className="w-0 h-0 border-t-[10px] border-t-transparent border-l-[18px] border-l-white border-b-[10px] border-b-transparent ml-1" />
                    </div>
                    
                    <div className="absolute bottom-6 left-6 text-left z-10">
                        <p className="text-white/90 text-sm font-medium tracking-wide mb-1 uppercase">Clinical Feature</p>
                        <h3 className="text-white text-xl font-bold">The Regulatory Layer (2:30)</h3>
                    </div>
                </div>
             </div>
        </div>
    </section>
  );
}
