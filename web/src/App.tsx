import { Routes, Route } from "react-router-dom";
import Advertorial from "./pages/Advertorial";
import SalesPage from "./pages/SalesPage";
import DiscoveryPage from "./pages/DiscoveryPage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Advertorial />} />
      <Route path="/sales" element={<SalesPage />} />
      <Route path="/discovery" element={<DiscoveryPage />} />
    </Routes>
  );
}

export default App;
