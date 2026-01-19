

export function MagazineHeader() {
  return (
    <header className="relative pt-48 pb-24 px-6 overflow-hidden bg-primary">
      <div className="max-w-[1000px] mx-auto relative z-10 text-center md:text-left">
        <div className="flex items-center justify-center md:justify-start gap-4 mb-8 text-sm font-bold tracking-[0.2em] text-accent-gold uppercase">
          <span className="w-12 h-[2px] bg-accent-gold"></span>
          Special Report: Modern Clinical Practice
        </div>
        
        <h1 
          className="text-5xl md:text-7xl leading-[1.05] font-bold text-text-primary mb-12 tracking-tight"
        >
          How Elite Practitioners Are Solving The Cases Everyone Else Refers Out.
        </h1>

        <div
            className="flex flex-col md:flex-row gap-12 items-start border-t border-text-primary/10 pt-12"
        >
             <p className="text-xl md:text-2xl text-text-secondary w-full md:w-3/4 leading-relaxed font-medium">
                A frank conversation about the "invisible layer" of health that is costing you referrals, revenue, and your reputation as the practitioner who gets results.
             </p>
             <div className="text-sm font-bold text-text-primary/60 border-l-2 border-accent-gold pl-6 py-1 w-full md:w-1/4">
                BY JIM BERNARDINO<br/>
                FOUNDER, QRX<br/>
                <span className="opacity-50 font-normal">READ TIME: 8 MIN</span>
             </div>
        </div>
      </div>
      
      {/* Editorial Watermark */}
      <div className="absolute top-10 right-10 md:right-[-5%] text-[15vw] font-bold text-text-primary/[0.03] leading-none pointer-events-none select-none">
        GAP
      </div>
    </header>
  );
}
