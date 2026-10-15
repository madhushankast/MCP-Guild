# Phase 4: Creating a Streamable HTTP MCP Server

- **Video Reference**: [MCP Full Course For Beginners (With Deployment)](https://www.youtube.com/watch?v=io02ZM0ADqM) — Timestamp: `1:34:04`
- **File**: [`2_HTTP_MCP/1_http_mcp.py`](file:///d:/Projects/MCP%20Guild/2_HTTP_MCP/1_http_mcp.py)

---

## 🎯 What This Part Does

In Chapter 1, we built an MCP server using **STDIO** (Standard Input/Output). STDIO is great for local, single-client desktop apps (like Claude Desktop running locally on your laptop), but it cannot be accessed across a network.

In **Chapter 2**, we switch to **HTTP Transport**.

### STDIO vs. HTTP Transport:

| Feature | STDIO Transport (Chapter 1) | HTTP Transport (Chapter 2) |
| :--- | :--- | :--- |
| **Connection** | Process pipe (`stdin` / `stdout`) | TCP / Network Socket (`http://`) |
| **Scope** | Local machine only | Network / Internet / Cloud accessible |
| **Clients** | Exactly 1 client (parent process) | Multiple concurrent clients |
| **Web & Microservices** | Difficult to connect | Native support via standard HTTP / SSE |
| **Default Port** | None (subprocesses) | Port `8050` (endpoint `/mcp`) |

---

## 📝 Complete Code Breakdown

```python
from fastmcp import FastMCP

# 1. Create an instance of FastMCP configured for HTTP
mcp = FastMCP("1_http_mcp")


# 2. Define Tool 1: fetch_http()
@mcp.tool()
async def fetch_http():
    """Use this tool to fetch data from an HTTP MCP server."""
    # Simulate fetching data from an external API or database source
    return {"data": "Hello, HTTP MCP!"}


# 3. Define Tool 2: process_http(path: str)
@mcp.tool()
async def process_http(path: str):
    """Use this tool to process data over HTTP."""
    # Simulate processing or transforming data received from path
    return {
        "status": "success",
        "processed_path": path,
        "message": f"Processed HTTP data from {path}",
    }


# 4. Start the Uvicorn web server running HTTP transport on port 8050
if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8050)
```

### Explanation of Code Sections:
- **`mcp = FastMCP("1_http_mcp")`**: Instantiates the server with the name `"1_http_mcp"`.
- **`@mcp.tool()`**: Exposes `fetch_http()` and `process_http(path: str)` as tools over HTTP.
- **`mcp.run(transport="http", host="127.0.0.1", port=8050)`**: Instead of stdio pipes, FastMCP starts an internal **Uvicorn** ASGI server listening on `http://127.0.0.1:8050/mcp`.

---

## 🚀 How to Run

Execute the script using `uv`:

```bash
uv run python 2_HTTP_MCP/1_http_mcp.py
```

---

## 🖥️ Expected Terminal Output

```text
+-----------------------------------------------------------------------------+
|                                FastMCP 3.4.8                                |
|                 Server:      1_http_mcp, 3.4.8                              |
+-----------------------------------------------------------------------------+

INFO: Starting MCP server '1_http_mcp' with transport 'http' on http://127.0.0.1:8050/mcp
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8050 (Press CTRL+C to quit)
```

The server is now live and waiting for remote MCP clients to connect to `http://127.0.0.1:8050/mcp`!

---

## 🔌 Connecting Remote Clients

Clients can connect using HTTP / SSE endpoint:
- **URL**: `http://127.0.0.1:8050/mcp`
- In next stages, we will connect to this server via **MCP Inspector** and a **LangChain HTTP Client**.
