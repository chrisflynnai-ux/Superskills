import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { cn } from "@/lib/utils";

const tabs = [
    { id: 'scan', label: '01. SCAN', title: 'Quantum Resonance Mapping', content: 'In 20 minutes, observe stress patterns across hundreds of organs. Identify regulatory disruption correlating with imbalance.' },
    { id: 'support', label: '02. SUPPORT', title: 'Deep Biofield Scalar', content: 'Deliver supportive scalar frequencies directly into the biofield. Support natural self-regulation in the same session.' },
    { id: 'reset', label: '03. RESET', title: 'Cellular Reset', content: 'Plug insights into a structured wellness program focusing on detox, mitochondrial resilience, and nervous system regulation.' },
];

export function MechanismInteractable() {
    const [activeTab, setActiveTab] = useState('scan');

  return (
    <section className="py-32 bg-text-primary text-white overflow-hidden relative">
       <div className="max-w-[1400px] mx-auto px-6 grid grid-cols-1 lg:grid-cols-2 gap-24 items-center relative z-10">
          <div>
             <h2 className="text-4xl md:text-5xl font-bold mb-16">The System.</h2>
             <div className="flex flex-col gap-6">
                {tabs.map((tab) => (
                    <button 
                        key={tab.id}
                        onClick={() => setActiveTab(tab.id)}
                        className={cn(
                            "text-left p-8 rounded-[var(--radius-minimal)] border transition-all duration-300",
                            activeTab === tab.id 
                                ? "bg-white text-text-primary border-white" 
                                : "bg-transparent border-white/10 text-white/40 hover:border-white/30"
                        )}
                    >
                        <div className="text-sm font-bold tracking-widest mb-2 uppercase">{tab.label}</div>
                        <div className="text-2xl font-bold">{tab.title}</div>
                    </button>
                ))}
             </div>
          </div>

          <div className="relative h-[600px] bg-white/5 rounded-2xl overflow-hidden border border-white/10">
              <AnimatePresence mode="wait">
                <motion.div
                    key={activeTab}
                    initial={{ opacity: 0, scale: 1.1 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0 }}
                    transition={{ duration: 0.5 }}
                    className="absolute inset-0"
                >
                    <img 
                        src={activeTab === 'scan' ? "/assets/official/sales/image5.jpeg" : activeTab === 'support' ? "/assets/official/sales/image3.jpeg" : "/assets/official/sales/image9.png"} 
                        className="w-full h-full object-cover opacity-60" 
                    />
                    <div className="absolute bottom-0 left-0 right-0 p-12 bg-gradient-to-t from-black/90 to-transparent">
                        <p className="text-xl leading-relaxed">{tabs.find(t => t.id === activeTab)?.content}</p>
                    </div>
                </motion.div>
              </AnimatePresence>
          </div>
       </div>
    </section>
  );
}
