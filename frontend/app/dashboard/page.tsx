"use client"

import { useEffect, useState } from "react"

export default function Dashboard() {

  const [logs, setLogs] = useState<any[]>([])
  const [memory, setMemory] = useState<any[]>([])

  const fetchData = async () => {
    try {
      const logsRes = await fetch("http://127.0.0.1:8001/logs")
      const memRes = await fetch("http://127.0.0.1:8001/memory")

      const logsData = await logsRes.json()
      const memData = await memRes.json()

      setLogs(logsData)
      setMemory(memData)
    } catch (err) {
      console.error(err)
    }
  }

  const clearMemory = async () => {
    await fetch("http://127.0.0.1:8001/memory/clear", {
      method: "POST"
    })
    fetchData()
  }

  useEffect(() => {
    fetchData()

    const interval = setInterval(() => {
      fetchData()
    }, 2000)

    return () => clearInterval(interval)
  }, [])

  return (
    <div style={{
      background: "#0f172a",
      color: "white",
      minHeight: "100vh",
      padding: "30px",
      fontFamily: "Arial"
    }}>

      <h1 style={{
        fontSize: "32px",
        marginBottom: "20px",
        color: "#38bdf8"
      }}>
        🤖 AI Control Panel
      </h1>

      <button onClick={clearMemory} style={{
        padding: "10px 20px",
        marginBottom: "30px",
        background: "#ef4444",
        color: "white",
        border: "none",
        borderRadius: "8px",
        cursor: "pointer"
      }}>
        🧹 Clear Memory
      </button>

      <div style={{
        display: "grid",
        gridTemplateColumns: "1fr 1fr",
        gap: "20px"
      }}>

        {/* Logs Card */}
        <div style={{
          background: "#1e293b",
          padding: "20px",
          borderRadius: "12px",
          boxShadow: "0 0 10px rgba(0,0,0,0.3)"
        }}>
          <h2 style={{ marginBottom: "15px", color: "#22c55e" }}>
            📊 System Logs
          </h2>

          <div style={{
            maxHeight: "300px",
            overflowY: "auto"
          }}>
            {logs.map((log, i) => (
              <div key={i} style={{
                marginBottom: "10px",
                fontSize: "14px"
              }}>
                <span style={{ color: "#94a3b8" }}>{log.time}</span><br />
                <span>{log.message}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Memory Card */}
        <div style={{
          background: "#1e293b",
          padding: "20px",
          borderRadius: "12px",
          boxShadow: "0 0 10px rgba(0,0,0,0.3)"
        }}>
          <h2 style={{ marginBottom: "15px", color: "#facc15" }}>
            🧠 Memory
          </h2>

          <div style={{
            maxHeight: "300px",
            overflowY: "auto"
          }}>
            {memory.map((m, i) => (
              <div key={i} style={{
                marginBottom: "10px",
                fontSize: "14px"
              }}>
                <b style={{ color: "#38bdf8" }}>{m.role}</b>: {m.content}
              </div>
            ))}
          </div>
        </div>

      </div>

    </div>
  )
}