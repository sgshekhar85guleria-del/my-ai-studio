"use client"

import { useState } from "react"

export default function Home() {

  const [input, setInput] = useState("")
  const [response, setResponse] = useState("")

  const sendMessage = async () => {

    try {

      const res = await fetch("http://localhost:8002/generate/stream", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt: input })
      })

      // 👉 अगर backend response नहीं देता
      if (!res.ok) {
        throw new Error("Backend not responding")
      }

      const text = await res.text()
      setResponse(text)

    } catch (error) {

      console.error("ERROR:", error)

      setResponse("❌ Backend not running OR connection failed")

    }
  }

  return (
    <div style={{
      padding: "30px",
      background: "#0f172a",
      color: "white",
      minHeight: "100vh"
    }}>

      <h1>🤖 AI Studio (Stable)</h1>

      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type your message..."
        style={{
          padding: "10px",
          width: "300px",
          marginRight: "10px",
          borderRadius: "8px",
          border: "none"
        }}
      />

      <button
        onClick={sendMessage}
        style={{
          padding: "10px 15px",
          background: "#22c55e",
          border: "none",
          borderRadius: "8px",
          cursor: "pointer"
        }}
      >
        Send
      </button>

      <div style={{ marginTop: "20px" }}>
        <b>Response:</b>
        <p>{response}</p>
      </div>

    </div>
  )
}