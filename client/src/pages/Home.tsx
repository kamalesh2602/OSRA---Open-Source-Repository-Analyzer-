import { useState } from "react";
import Navbar from "../components/layout/Navbar";
import Hero from "../components/home/Hero";
import OverviewCards from "../components/dashboard/OverviewCards";

export default function Home() {
  const [repository, setRepository] = useState<any>(null);
  
  return (
    <div className="min-h-screen bg-[#030712] text-white">
      <Navbar />

      <Hero setRepository={setRepository} />

      {repository && (
        <OverviewCards repository={repository} />
      )}
    </div>
  );
}