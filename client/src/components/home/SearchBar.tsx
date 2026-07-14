import { useState } from "react";
import { Loader2 } from "lucide-react";
import { analyzeRepository } from "../../services/api";

interface SearchBarProps {
  setRepository: (repo: any) => void;
}

export default function SearchBar({ setRepository }: SearchBarProps) {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!url.trim()) return;

    try {
      setLoading(true);
      setRepository(null);

      const data = await analyzeRepository(url);

      setRepository(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mx-auto flex max-w-3xl gap-4">

      <input
        type="text"
        placeholder="https://github.com/facebook/react"
        value={url}
        disabled={loading}
        onChange={(e) => setUrl(e.target.value)}
        className="flex-1 rounded-2xl border border-white/10 bg-white/5 px-6 py-4 text-white outline-none transition focus:border-blue-500 disabled:opacity-60"
      />

      <button
        onClick={handleAnalyze}
        disabled={loading}
        className="flex min-w-[170px] items-center justify-center gap-2 rounded-2xl bg-blue-600 px-8 py-4 font-semibold transition hover:bg-blue-500 disabled:cursor-not-allowed disabled:opacity-70"
      >
        {loading ? (
          <>
            <Loader2 size={18} className="animate-spin" />
            Analyzing...
          </>
        ) : (
          "Analyze"
        )}
      </button>

    </div>
  );
}