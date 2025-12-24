"use client";
import { useState } from "react";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");

  const sendPrompt = async () => {
    const res = await fetch("http://127.0.0.1:8000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt }),
    });

    const data = await res.json();
    setResponse(JSON.stringify(data, null, 2));
  };

  return (
    <main className="p-10 max-w-2xl mx-auto text-white">
      <h1 className="text-2xl font-bold mb-4">Agency AI Tool</h1>

      <textarea
        className="border text-black p-2 w-full mb-4"
        rows={4}
        placeholder="Enter your prompt..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <button
        onClick={sendPrompt}
        className="bg-black text-white px-4 py-2 rounded"
      >
        Send Prompt
      </button>

      {response && (
        <pre className="mt-4 bg-white text-black p-4 rounded whitespace-pre-wrap">
          {response}
        </pre>
      )}
    </main>
  );
}

