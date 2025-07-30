"use client";

import { useRef, useState } from "react";

interface Props {
  onResults: (results: any[]) => void;
  setLoading: (isLoading: boolean) => void;
}

export default function UploadForm({ onResults, setLoading }: Props) {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const jdInputRef = useRef<HTMLTextAreaElement>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const files = fileInputRef.current?.files;
    const jd = jdInputRef.current?.value;

    if (!files || files.length === 0 || !jd) return;

    const formData = new FormData();
    for (const file of Array.from(files)) {
      formData.append("files", file);
    }
    formData.append("job_description", jd);

    setLoading(true);
    try {
      const res = await fetch("http://127.0.0.1:8000/api/rank", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      onResults(data.results);

      // Clear form inputs after success ✅
      if (fileInputRef.current) fileInputRef.current.value = "";
      if (jdInputRef.current) jdInputRef.current.value = "";
    } catch (err) {
      console.error("Upload failed:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <input
        ref={fileInputRef}
        type="file"
        multiple
        accept=".pdf"
        className="w-full border p-2 rounded"
      />
      <textarea
        ref={jdInputRef}
        rows={6}
        placeholder="Paste job description here..."
        className="w-full border p-2 rounded"
      ></textarea>
      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Submit
      </button>
    </form>
  );
}
