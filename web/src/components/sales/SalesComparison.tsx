import { AlertTriangle } from "lucide-react";

export function SalesComparison() {
  return (
    <section className="py-24 bg-primary">
      <div className="max-w-[1200px] mx-auto px-6">
        
        <div className="text-center mb-16 max-w-3xl mx-auto">
            <h2 className="text-4xl font-bold mb-6">Not Just Another "Scanner." <br/>A Complete Clinical Ecosystem.</h2>
            <p className="text-xl text-text-secondary">
                You may have seen "frequency devices" before. Here is the difference: <br/>Those are consumer gadgets. QRX is a Clinical Weapon.
            </p>
        </div>

        <div className="overflow-x-auto">
            <table className="w-full border-collapse bg-white rounded-[var(--radius-minimal)] shadow-soft overflow-hidden">
                <thead>
                    <tr className="bg-text-primary text-white">
                        <th className="p-6 text-left w-1/4">Feature</th>
                        <th className="p-6 text-center w-1/4 opacity-70 font-medium">Consumer Gadgets<br/><span className="text-xs uppercase tracking-widest">(Healy / AO)</span></th>
                        <th className="p-6 text-center w-1/4 opacity-70 font-medium">Legacy Systems<br/><span className="text-xs uppercase tracking-widest">(QUEX / TimeWaver)</span></th>
                        <th className="p-6 text-center w-1/4 bg-accent-teal font-bold relative">
                            QRX QUANTUM RESONANCE™
                            <div className="absolute top-0 left-0 w-full h-1 bg-accent-gold"></div>
                        </th>
                    </tr>
                </thead>
                <tbody className="text-text-secondary">
                    {/* Row 1 */}
                    <tr className="border-b border-gray-100 hover:bg-gray-50">
                        <td className="p-6 font-bold text-text-primary">Grade</td>
                        <td className="p-6 text-center">MLM / Consumer Toy</td>
                        <td className="p-6 text-center">Aging Tech / Over-Complex</td>
                        <td className="p-6 text-center font-bold text-accent-teal bg-accent-teal/5">Professional Clinical System</td>
                    </tr>
                    {/* Row 2 */}
                    <tr className="border-b border-gray-100 hover:bg-gray-50">
                        <td className="p-6 font-bold text-text-primary">Depth</td>
                        <td className="p-6 text-center">Surface Level</td>
                        <td className="p-6 text-center">High Learning Curve</td>
                        <td className="p-6 text-center font-bold text-accent-teal bg-accent-teal/5">Deep Scalar Penetration</td>
                    </tr>
                    {/* Row 3 */}
                    <tr className="border-b border-gray-100 hover:bg-gray-50">
                        <td className="p-6 font-bold text-text-primary">Outcome</td>
                        <td className="p-6 text-center">"Data Dump"</td>
                        <td className="p-6 text-center">"Confusion"</td>
                        <td className="p-6 text-center font-bold text-accent-teal bg-accent-teal/5">Actionable Roadmap</td>
                    </tr>
                    {/* Row 4 */}
                    <tr>
                        <td className="p-6 font-bold text-text-primary">Business Model</td>
                        <td className="p-6 text-center text-red-500 flex items-center justify-center gap-2">
                            <AlertTriangle size={16} /> Recruit Friends
                        </td>
                        <td className="p-6 text-center">$30k+ Investment</td>
                        <td className="p-6 text-center font-bold text-accent-teal bg-accent-teal/5">Practice Growth Engine</td>
                    </tr>
                </tbody>
            </table>
        </div>

      </div>
    </section>
  );
}
