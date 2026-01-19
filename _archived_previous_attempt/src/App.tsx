import { Routes, Route } from 'react-router-dom';
import { Layout } from "./components/shared/Layout";
import { EditorialHero } from "./components/advertorial/EditorialHero";
import { LeadContent } from "./components/advertorial/LeadContent";
import { CTASection } from "./components/sales/CTASection";
import { SalesPage } from "./components/sales/SalesPage";

function Advertorial() {
  return (
    <>
      <EditorialHero />
      <LeadContent />
      <CTASection />
    </>
  );
}

function App() {
  return (
    <RouterLayout>
       <Routes>
        <Route path="/" element={<Advertorial />} />
        <Route path="/sales" element={<SalesPage />} />
      </Routes>
    </RouterLayout>
  );
}

// Wrapper to pass children to Layout but keep Router context happy if needed, 
// though Layout itself doesn't depend on Router context unless using Links.
// actually Layout uses Navbar which might use useNavigate.
// Let's ensure Layout is outside Routes if it persists, or inside if page specific.
// Plan: Using Layout as a wrapper in each page or global.
// Simpler: Just put Layout in App and Routes inside Main.

function RouterLayout({ children }: { children: React.ReactNode }) {
  return (
    <Layout>
      {children}
    </Layout>
  );
}

export default App;
