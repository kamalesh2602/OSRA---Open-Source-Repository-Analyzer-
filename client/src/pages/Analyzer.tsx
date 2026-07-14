import { useState } from "react";

import Navbar from "../components/layout/Navbar";
import Hero from "../components/home/Hero";
import OverviewCards from "../components/dashboard/OverviewCards";
import Footer from "../components/layout/Footer";

export default function Analyzer() {
  const [repository, setRepository] = useState<any>(null);

  return (
    <div className="min-h-screen bg-[#030712] text-white">

      <Navbar />

      <Hero setRepository={setRepository} />

      {repository && (
        <OverviewCards repository={repository} />
      )}
    <Footer />
    </div>
  );
}