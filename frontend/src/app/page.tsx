// src/app/page.tsx
"use client";

import { useState } from "react";
import UploadForm from "@/components/UploadForm";
import ResultsList from "@/components/ResultsList";

export default function Home() {
  const [results, setResults] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  const handleFormSubmit = (newResults: any[]) => {
    setResults(newResults);
  };

  const handleExport = () => {
    const headers = ["Name", "Score", "Explanation"];
    const rows = results.map((r) => [r.name, r.score, r.explanation]);
    const csvContent = [headers, ...rows]
      .map((e) => e.map((s) => `"${String(s).replace(/"/g, '""')}"`).join(","))
      .join("\n");

    const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.setAttribute("href", url);
    link.setAttribute("download", "resume_results.csv");
    link.click();
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8 px-4">
      <div className="max-w-2xl mx-auto bg-white p-8 rounded shadow">
        <h1 className="text-2xl font-bold mb-4">AI Resume Screener</h1>
        <UploadForm onResults={handleFormSubmit} setLoading={setLoading} />
        {loading && <p className="text-blue-500 mt-4">Processing resumes...</p>}
        {results.length > 0 && (
          <div className="mt-6">
            <div className="flex justify-between items-center">
              <h2 className="text-xl font-semibold">Results</h2>
              <button
                onClick={handleExport}
                className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
              >
                Export CSV
              </button>
            </div>
            <ResultsList results={results} />
          </div>
        )}
      </div>
    </div>
  );
}
