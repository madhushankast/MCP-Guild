# Phase 5: LangChain Client for HTTP MCP Server

- **Video Reference**: [MCP Full Course For Beginners (With Deployment)](https://www.youtube.com/watch?v=io02ZM0ADqM) — Timestamp: `1:55:07`
- **File**: [`2_HTTP_MCP/2_langchain_client.py`](file:///d:/Projects/MCP%20Guild/2_HTTP_MCP/2_langchain_client.py)

---

## 🎯 What This Part Does

In Chapter 1, our LangChain client connected to a **local STDIO** script by starting it as a child subprocess. 

In this stage, our LangChain client connects to a **remote/networked HTTP MCP server** that is already running on a port (`http://127.0.0.1:8050/mcp`).

### Key Differences from STDIO Client:
1. **No Subprocess**: The client does not launch Python or manage pipes. It simply opens an HTTP/SSE streaming connection to the server URL.
2. **`streamable_http` Transport**: Uses HTTP POST/GET and Server-Sent Events to exchange JSON-RPC messages.
3. **Decoupled Architecture**: The server can run anywhere (on a remote VM, inside Docker, Kubernetes, or the cloud), while the client runs locally or in another service.

---

## 📝 Complete Code Breakdown

```python
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

# Target URL of the running HTTP MCP Server
HTTP_MCP_SERVER_URL = "http://127.0.0.1:8050/mcp"


async def main():
    print(f"Connecting to HTTP MCP Server at: {HTTP_MCP_SERVER_URL} ...\n")

    # 1. Initialize MultiServerMCPClient using streamable_http transport
    client = MultiServerMCPClient(
        {
            "my_http_server": {
                "transport": "streamable_http",
                "url": HTTP_MCP_SERVER_URL,
            }
        }
    )

    # 2. Automatically retrieve and convert remote MCP tools into LangChain tools
    tools = await client.get_tools()

    print(f"Connected! Discovered {len(tools)} LangChain tool(s) over HTTP:")
    for tool in tools:
        print(f" - Tool Name: {tool.name}")
        print(f"   Description: {tool.description}")
        print(f"   Arguments: {tool.args}\n")

    # 3. Invoke tool 'fetch_http' via LangChain .ainvoke()
    print("--- Invoking 'fetch_http' tool over HTTP ---")
    fetch_tool = next(t for t in tools if t.name == "fetch_http")
    fetch_response = await fetch_tool.ainvoke({})
    print(f"Response: {fetch_response}\n")

    # 4. Invoke tool 'process_http' with input arguments
    print("--- Invoking 'process_http' tool over HTTP ---")
    process_tool = next(t for t in tools if t.name == "process_http")
    process_response = await process_tool.ainvoke({"path": "remote_dataset.json"})
    print(f"Response: {process_response}\n")

    print("HTTP MCP LangChain Client integration successful!")


if __name__ == "__main__":
    asyncio.run(main())
```

### Explanation of Code Sections:
- **`MultiServerMCPClient` with `transport: "streamable_http"`**: Configures the client to connect to `http://127.0.0.1:8050/mcp` using the HTTP streaming protocol.
- **`await client.get_tools()`**: Sends an HTTP request to the MCP server, downloads the registered tool schemas, and builds native LangChain `StructuredTool` objects.
- **`await tool.ainvoke(...)`**: Executes the tool by sending an HTTP POST JSON-RPC request to the server, receiving the response stream, and unpacking the data.

---

## 🚀 How to Run

### Step 1: Ensure the HTTP server is running (Terminal 1)
```bash
uv run python 2_HTTP_MCP/1_http_mcp.py
```

### Step 2: Run the LangChain HTTP client (Terminal 2)
```bash
uv run python 2_HTTP_MCP/2_langchain_client.py
```

---

## 🖥️ Expected Terminal Output

```text
Connecting to HTTP MCP Server at: http://127.0.0.1:8050/mcp ...

Connected! Discovered 2 LangChain tool(s) over HTTP:
 - Tool Name: fetch_http
   Description: Use this tool to fetch data from an HTTP MCP server.
   Arguments: {}

 - Tool Name: process_http
   Description: Use this tool to process data over HTTP.
   Arguments: {'path': {'type': 'string'}}

--- Invoking 'fetch_http' tool over HTTP ---
Response: [{'type': 'text', 'text': '{"data":"Hello, HTTP MCP!"}', 'id': 'lc_...'}]

--- Invoking 'process_http' tool over HTTP ---
Response: [{'type': 'text', 'text': '{"status":"success","processed_path":"remote_dataset.json","message":"Processed HTTP data from remote_dataset.json"}', 'id': 'lc_...'}]

HTTP MCP LangChain Client integration successful!
```
