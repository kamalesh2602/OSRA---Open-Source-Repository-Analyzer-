import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="sticky top-0 z-50 border-b border-white/10 bg-[#030712]/80 backdrop-blur-xl">

      <div className="mx-auto flex max-w-7xl items-center justify-between px-8 py-5">

        <Link
          to="/"
          className="text-2xl font-black tracking-wide"
        >
          OSRA
        </Link>

        <div className="flex items-center gap-8">

          <Link
            to="/"
            className="text-slate-300 hover:text-white"
          >
            Home
          </Link>

          <Link
            to="/analyzer"
            className="text-slate-300 hover:text-white"
          >
            Analyzer
          </Link>

          <Link
            to="/analytics"
            className="text-slate-300 hover:text-white"
          >
            Analytics
          </Link>

          <a
            href="https://github.com/"
            target="_blank"
            rel="noreferrer"
            className="rounded-xl border border-white/10 bg-white/5 px-4 py-2 transition hover:bg-white/10"
          >
            GitHub
          </a>

        </div>

      </div>

    </nav>
  );
}