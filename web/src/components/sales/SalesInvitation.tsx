import { MagneticButton } from "../ui/MagneticButton";

export function SalesInvitation() {
  return (
    <section className="py-32 relative bg-text-primary text-white overflow-hidden" id="book">
      {/* Background Ambience */}
      <div className="absolute inset-0 bg-gradient-to-tr from-text-primary via-text-primary to-accent-teal/20" />
      
      <div className="max-w-4xl mx-auto px-6 relative z-10 text-center">
        <h2 className="text-5xl md:text-6xl font-bold mb-8">Are You Ready To Upgrade Your Lens?</h2>
        
        <p className="text-xl md:text-2xl text-gray-300 mb-12 leading-relaxed">
            The era of "guessing and waiting" is over. We are looking for the top 1% of functional wellness professionals who are ready to define the future of care.
        </p>

        <div className="p-8 border border-white/10 rounded-2xl bg-white/5 backdrop-blur-sm mb-12 text-left md:text-center">
            <p className="text-lg text-gray-200 mb-6 font-medium">
                This is not a sales pitch. It is a peer-to-peer look at your clinical model.
            </p>
            <div className="flex flex-col md:flex-row items-center justify-center gap-6">
                 <MagneticButton variant="primary" className="bg-white text-text-primary hover:bg-gray-100">
                    Watch The Demo (20 Min)
                 </MagneticButton>
                 <MagneticButton variant="ghost" className="text-white border-white/20 hover:bg-white/10">
                    Book Your Practice Audit
                 </MagneticButton>
            </div>
        </div>

        <p className="text-xs text-gray-500 max-w-2xl mx-auto">
            The QRX Quantum Resonance™ System is intended for wellness, stress-reduction, and energetic support only. It is an educational wellness tool, not a medical device. It does not diagnose, treat, cure, or prevent any disease.
        </p>
      </div>
    </section>
  );
}
