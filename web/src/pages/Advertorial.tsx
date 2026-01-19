import { Layout } from "../components/shared/Layout";
import { MagazineHeader } from "../components/advertorial/MagazineHeader";
import { AdvertorialBody } from "../components/advertorial/AdvertorialBody";
import { MagneticButton } from "../components/ui/MagneticButton";

function Advertorial() {
  return (
    <Layout>
      <MagazineHeader />
      
      <div className="max-w-[1200px] mx-auto px-6 mb-16">
        <img 
            src="/assets/official/advertorial/image4.jpeg"
            className="w-full h-[50vh] md:h-[70vh] object-cover rounded-[var(--radius-minimal)] shadow-2xl"
            alt="The Third Lens Feature"
        />
        <div className="text-sm text-text-secondary mt-4 text-center italic opacity-60">
            The "Third Lens": Seeing the invisible regulatory layer of health.
        </div>
      </div>

      <AdvertorialBody />
      
      {/* Sticky Bottom Assessment Logic could go here, but for now just the footer CTA */}
      
      <div className="bg-text-primary text-white py-32 text-center relative overflow-hidden">
        <div className="absolute inset-0 bg-accent-teal/10"></div>
        <div className="relative z-10 max-w-4xl mx-auto px-6">
            <h2 className="text-4xl md:text-5xl font-bold mb-8">Are You Ready To Upgrade Your Lens?</h2>
            <p className="text-lg text-white/80 mb-12 max-w-2xl mx-auto leading-relaxed">
                The future of functional medicine belongs to those who can see the invisible. Watch the 2-minute clinical breakdown to see how it works.
            </p>
            <div className="flex flex-col md:flex-row items-center justify-center gap-6 mb-16">
                <MagneticButton className="bg-white text-text-primary hover:bg-gray-100" onClick={() => window.location.href='/sales#demo'}>
                    Watch Clinical Demo
                </MagneticButton>
                <MagneticButton variant="ghost" className="text-white border-white/20" onClick={() => window.location.href='/sales#book'}>
                    Book Practice Audit
                </MagneticButton>
            </div>
            
            <p className="text-xs text-gray-500 max-w-2xl mx-auto leading-relaxed border-t border-white/10 pt-8">
                The QRX Quantum Resonance™ System is intended for wellness, stress-reduction, and energetic support only. It is an educational wellness tool, not a medical device. It does not diagnose, treat, cure, or prevent any disease.
            </p>
        </div>
      </div>
    </Layout>
  );
}

export default Advertorial;
