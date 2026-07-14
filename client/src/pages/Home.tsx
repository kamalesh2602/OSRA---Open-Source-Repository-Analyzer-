import Footer from "../components/layout/Footer";
import Navbar from "../components/layout/Navbar";
import { Link } from "react-router-dom";

const features = [
  {
    title: "Machine Learning",
    desc: "K-Means clustering classifies repositories based on activity, popularity and maintenance.",
  },
  {
    title: "GitHub Analytics",
    desc: "Analyze stars, forks, issues, language and repository metadata.",
  },
  {
    title: "Visual Dashboard",
    desc: "Interactive charts and repository insights powered by Chart.js.",
  },
  {
    title: "Fast Analysis",
    desc: "Analyze any public GitHub repository in seconds.",
  },
];

const pipeline = [
  "GitHub API",
  "Dataset Collection",
  "Preprocessing",
  "Feature Engineering",
  "StandardScaler",
  "PCA",
  "K-Means",
  "Prediction",
];

const tech = [
  "React",
  "TypeScript",
  "Tailwind CSS",
  "FastAPI",
  "Python",
  "Scikit-Learn",
  "Chart.js",
  "GitHub API",
];

export default function Home() {
  return (
    <div className="min-h-screen bg-[#030712] text-white">
      <Navbar />

      <section className="mx-auto flex min-h-[85vh] max-w-7xl flex-col items-center justify-center px-8 text-center">
        <h1 className="mb-8 text-7xl font-black">
          Open Source Repository Analyzer
        </h1>

        <p className="mb-10 max-w-4xl text-xl leading-9 text-slate-400">
          Analyze GitHub repositories using Machine Learning. OSRA combines
          GitHub analytics with K-Means clustering to classify repositories
          based on popularity, activity and maintenance.
        </p>

        <Link
          to="/analyzer"
          className="rounded-2xl bg-blue-600 px-10 py-5 text-lg font-semibold transition hover:bg-blue-500"
        >
          Analyze Repository →
        </Link>
      </section>

      <section className="mx-auto max-w-7xl px-8 py-20">
        <h2 className="mb-6 text-4xl font-bold">Problem Statement</h2>

        <p className="leading-8 text-slate-400">
          GitHub hosts millions of repositories, making it difficult to quickly
          identify projects that are actively maintained and suitable for
          learning or production use. Traditional metrics such as stars and
          forks alone are often insufficient for evaluating repository quality.
        </p>
      </section>

      <section className="mx-auto max-w-7xl px-8 py-20">
        <h2 className="mb-6 text-4xl font-bold">Proposed Solution</h2>

        <p className="leading-8 text-slate-400">
          OSRA automatically collects repository metadata from GitHub, engineers
          meaningful features, applies PCA for dimensionality reduction and uses
          K-Means clustering to group repositories with similar development and
          maintenance characteristics.
        </p>
      </section>

      <section className="mx-auto max-w-7xl px-8 py-20">
        <h2 className="mb-10 text-4xl font-bold">Features</h2>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
          {features.map((feature) => (
            <div
              key={feature.title}
              className="rounded-3xl border border-white/10 bg-white/5 p-6"
            >
              <h3 className="mb-3 text-xl font-semibold">
                {feature.title}
              </h3>

              <p className="leading-7 text-slate-400">
                {feature.desc}
              </p>
            </div>
          ))}
        </div>
      </section>

      <section className="mx-auto max-w-7xl px-8 py-20">
        <h2 className="mb-10 text-4xl font-bold">Machine Learning Pipeline</h2>

        <div className="grid gap-4 md:grid-cols-4">
          {pipeline.map((step, index) => (
            <div
              key={step}
              className="rounded-2xl border border-blue-500/20 bg-blue-500/5 p-5 text-center"
            >
              <div className="mb-2 text-sm text-blue-400">
                Step {index + 1}
              </div>

              <div className="font-semibold">
                {step}
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="mx-auto max-w-7xl px-8 py-20">
        <h2 className="mb-10 text-4xl font-bold">Technology Stack</h2>

        <div className="flex flex-wrap gap-4">
          {tech.map((item) => (
            <div
              key={item}
              className="rounded-full border border-white/10 bg-white/5 px-6 py-3"
            >
              {item}
            </div>
          ))}
        </div>
      </section>

      <section className="mx-auto max-w-7xl px-8 py-24 text-center">
        <h2 className="mb-6 text-5xl font-bold">
          Ready to Analyze a Repository?
        </h2>

        <Link
          to="/analyzer"
          className="rounded-2xl bg-blue-600 px-10 py-5 text-lg font-semibold transition hover:bg-blue-500"
        >
          Start Analysis
        </Link>
      </section>
      <Footer />
    </div>
  );
}