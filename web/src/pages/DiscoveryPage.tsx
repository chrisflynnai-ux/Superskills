import { Layout } from "../components/shared/Layout";
import { MagneticButton } from "../components/ui/MagneticButton";

export default function DiscoveryPage() {
  return (
    <Layout>
      <div className="bg-primary min-h-screen text-primary">
        
        {/* Header / Nav Area */}
        <div className="fixed top-0 left-0 right-0 z-50 px-6 py-6 flex justify-between items-center pointer-events-none">
             <div className="pointer-events-auto">
                 <span className="text-xl font-bold tracking-tight text-primary">QRX</span>
             </div>
             <div className="pointer-events-auto">
                 <MagneticButton variant="ghost" onClick={() => window.location.href='/sales'}>
                    Skip to Sales Page
                 </MagneticButton>
             </div>
        </div>

        {/* Main Cinema Container */}
        <div className="max-w-6xl mx-auto px-6 pt-32 pb-24">
            
            <div className="text-center mb-12">
                <div className="inline-block px-3 py-1 mb-4 rounded-full border border-text-secondary/20 text-xs font-bold tracking-widest text-text-secondary uppercase">
                    Documentary Feature
                </div>
                <h1 className="text-4xl md:text-6xl font-bold mb-6 tracking-tight">The Complete Discovery</h1>
                <p className="text-xl text-text-secondary max-w-2xl mx-auto">
                    From the frustration of "normal labs" to the breakthrough of the Regulatory Layer. Watch the full story.
                </p>
            </div>

            {/* Video Player Shell */}
            <div className="aspect-video bg-black rounded-2xl shadow-2xl overflow-hidden relative group border border-white/10">
                <div className="absolute inset-0 flex items-center justify-center">
                    <img 
                        src="/assets/official/sales/image1.jpeg" 
                        className="absolute inset-0 w-full h-full object-cover opacity-40"
                        alt="Documentary Cover"
                    />
                    <div className="relative z-10 w-24 h-24 rounded-full bg-white/10 backdrop-blur-md border border-white/20 flex items-center justify-center cursor-pointer hover:scale-110 transition-transform duration-500">
                         <div className="ml-2 w-0 h-0 border-t-[12px] border-t-transparent border-l-[20px] border-l-white border-b-[12px] border-b-transparent" />
                    </div>
                </div>
                
                {/* Duration Badge */}
                <div className="absolute bottom-6 right-6 px-4 py-2 bg-black/60 backdrop-blur-md rounded-lg text-white font-mono text-sm border border-white/10">
                    14:15
                </div>
            </div>

        </div>

        {/* Post-Watch CTA */}
        <div className="bg-bg-secondary py-24 text-center">
            <div className="max-w-2xl mx-auto px-6">
                <h2 className="text-3xl font-bold mb-6">Ready to see your practice differently?</h2>
                <div className="flex flex-col md:flex-row justify-center gap-6">
                     <MagneticButton onClick={() => window.location.href='/sales'}>
                        Explore The System
                     </MagneticButton>
                     <MagneticButton variant="ghost" onClick={() => window.open('#book', '_blank')}>
                        Book Peer Conversation
                     </MagneticButton>
                </div>
            </div>
        </div>

      </div>
    </Layout>
  );
}
