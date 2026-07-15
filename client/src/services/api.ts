const API_URL = import.meta.env.VITE_API_URL;

export async function analyzeRepository(url: string) {
  const response = await fetch(`${API_URL}/repository/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      url,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to analyze repository");
  }

  return response.json();
}