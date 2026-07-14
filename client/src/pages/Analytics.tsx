import Footer from "../components/layout/Footer";
import Navbar from "../components/layout/Navbar";

const artifacts = [
  {
    title: "Elbow Method",
    description:
      "Used to determine the optimal number of clusters for K-Means training.",
    file: "/eda/elbow_plot.png",
  },
  {
    title: "Cluster Summary",
    description:
      "Average repository statistics calculated for every discovered cluster.",
    file: "/eda/clusters_pca.png",
  },
];

export default function Analytics() {
  return (
    <div className="min-h-screen bg-[#030712] text-white">
      <Navbar />

      <section className="mx-auto max-w-7xl px-8 py-20">

        <h1 className="mb-4 text-6xl font-black">
          Machine Learning Analytics
        </h1>

        <p className="mb-16 max-w-4xl text-lg leading-8 text-slate-400">
          Visualizations and artifacts generated during feature engineering,
          dimensionality reduction and K-Means clustering.
        </p>

        <div className="grid gap-8 lg:grid-cols-2">

          {artifacts.map((item) => (
            <div
              key={item.title}
              className="rounded-3xl border border-white/10 bg-white/5 p-6"
            >
              <h2 className="mb-2 text-2xl font-bold">
                {item.title}
              </h2>

              <p className="mb-6 text-slate-400">
                {item.description}
              </p>

              <img
                src={item.file}
                alt={item.title}
                className="w-full rounded-xl bg-white"
              />
            </div>
          ))}

        </div>

        <div className="mt-12 rounded-3xl border border-white/10 bg-white/5 p-8">

          <h2 className="mb-6 text-3xl font-bold">
            Model Summary
          </h2>

          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">

            <div>
              <h3 className="text-slate-400">Algorithm</h3>
              <p className="text-2xl font-bold">K-Means</p>
            </div>

            <div>
              <h3 className="text-slate-400">Preprocessing</h3>
              <p className="text-2xl font-bold">StandardScaler</p>
            </div>

            <div>
              <h3 className="text-slate-400">Dimensionality Reduction</h3>
              <p className="text-2xl font-bold">PCA (95%)</p>
            </div>

            <div>
              <h3 className="text-slate-400">Dataset</h3>
              <p className="text-2xl font-bold">250 Repositories</p>
            </div>

          </div>

        </div>

      </section>
      <Footer />
    </div>
  );
}