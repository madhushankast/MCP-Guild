# Phase 6: Testing & Debugging with MCP Inspector

- **Video Reference**: [MCP Full Course For Beginners (With Deployment)](https://www.youtube.com/watch?v=io02ZM0ADqM) — Timestamp: `1:42:44`
- **Tool**: `@modelcontextprotocol/inspector`

---

## 🎯 What This Part Does

The **MCP Inspector** is the official visual developer tool built by Anthropic for testing, debugging, and inspecting Model Context Protocol servers.

### Why Use the Inspector?
- **Interactive UI**: View all exposed tools, resources, and prompts in a web interface.
- **Form Inputs**: Fill in tool parameters via web forms without writing test client code.
- **Protocol Inspection**: See real-time JSON-RPC 2.0 requests, responses, and notification streams.
- **Multi-Transport Support**: Works seamlessly with both **STDIO** (child subprocess) and **HTTP / SSE** (network endpoints).

---

## 🚀 How to Run the MCP Inspector

Because you have `npx` installed, you **do not need to manually download or build anything**. `npx` fetches and runs the latest version on demand:

```bash
npx @modelcontextprotocol/inspector
```

When you run this command, your terminal will display a local URL:
```text
Starting MCP inspector...
Proxy server listening on port 3000
Inspector web UI available at: http://localhost:5173
```

Open **`http://localhost:5173`** in your browser.

---

## 🔌 Connecting to Your MCP Servers

### Scenario A: Connecting to Chapter 2 HTTP MCP Server
1. Make sure your HTTP server is running:
   ```bash
   uv run python 2_HTTP_MCP/1_http_mcp.py
   ```
2. In the Inspector UI top bar:
   - **Transport Type**: Select `Streamable HTTP` (or `SSE`)
   - **URL**: `http://127.0.0.1:8050/mcp`
3. Click **Connect**.
4. Click on the **Tools** tab:
   - You will see `fetch_http` and `process_http`.
   - Click `Run Tool` to test them live!

---

### Scenario B: Connecting directly to Chapter 1 STDIO MCP Server
You can also inspect STDIO servers directly without running a separate terminal:
1. In the Inspector UI top bar:
   - **Transport Type**: Select `STDIO`
   - **Command**: `uv`
   - **Arguments**: `run python 1_CreateMCP/1_MCPServer_stdio.py`
2. Click **Connect**.
3. The Inspector starts your python script in the background and displays `fetch` and `process`.

---

## 💡 Troubleshooting
- If port `5173` or `3000` is already in use, pass a custom port:
  ```bash
  npx @modelcontextprotocol/inspector --port 8080
  ```
