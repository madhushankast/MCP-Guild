# Phase 1: Creating Your First STDIO MCP Server

- **Video Reference**: [MCP Full Course For Beginners (With Deployment)](https://www.youtube.com/watch?v=io02ZM0ADqM) — Timestamp: `49:13`
- **File**: [`CreateMCP/1_MCPServer_stdio.py`](file:///d:/Projects/MCP%20Guild/CreateMCP/1_MCPServer_stdio.py)

---

## 🎯 What This Part Does

In this stage, you build your very first **Model Context Protocol (MCP)** server using the **FastMCP** framework.

### Key Concepts:
1. **STDIO Transport**: Communication happens over standard input (`stdin`) and standard output (`stdout`). The host application (like Claude Desktop, Cursor, or a Python script) spawns the MCP server as a child process and sends JSON-RPC 2.0 messages over pipe.
2. **Tools**: Functions decorated with `@mcp.tool()` that an AI model can discover, inspect the schema of, and invoke.
3. **Type Annotations & Docstrings**: FastMCP reads your Python type hints (`path: str`) and docstrings (`"""..."""`) to automatically generate the JSON Schema that tells the LLM what the tool does and what parameters it accepts.

---

## 📝 Complete Code Breakdown

```python
from fastmcp import FastMCP

# 1. Initialize FastMCP with the server name
mcp = FastMCP("1_MCPServer_stdio")


# 2. Define Tool 1: fetch()
@mcp.tool()
async def fetch():
    """Use this tool to fetch data from a source."""
    # Simulate fetching data from a database or external API
    return {"data": "Hello, MCP!"}


# 3. Define Tool 2: process(path: str)
@mcp.tool()
async def process(path: str):
    """Use this tool to process the fetched data."""
    # Simulate processing or parsing a file from the provided path
    return {
        "status": "success",
        "processed_path": path,
        "message": f"Processed data from {path}",
    }


# 4. Entrypoint: Run using STDIO transport
if __name__ == "__main__":
    mcp.run(transport="stdio")
```

### Explanation of Code Sections:
- **`FastMCP("1_MCPServer_stdio")`**: Creates the server instance. The name is announced to clients during handshake.
- **`@mcp.tool()`**: Registers the function as a callable tool in the MCP registry.
- **`async def fetch()`**: A parameterless tool. FastMCP generates a schema with `"properties": {}`.
- **`async def process(path: str)`**: Accepts a required string parameter. FastMCP generates `"properties": {"path": {"type": "string"}}` and `"required": ["path"]`.
- **`mcp.run(transport="stdio")`**: Starts listening on `sys.stdin` for JSON-RPC messages and writing responses to `sys.stdout`.

---

## 🚀 How to Run

### Direct Command Line:
```bash
uv run python CreateMCP/1_MCPServer_stdio.py
```

### What to Expect:
FastMCP will launch and print its banner and status to `stderr`:
```text
+-----------------------------------------------------------------------------+
|                                FastMCP 3.4.8                                |
|                 Server:      1_MCPServer_stdio, 3.4.8                       |
+-----------------------------------------------------------------------------+
INFO: Starting MCP server '1_MCPServer_stdio' with transport 'stdio'
```
*Note: The server will remain running waiting for input on `stdin`. To exit, press `Ctrl + C`.*

---

## 🤖 Connecting to an MCP Client (e.g., Claude Desktop, Antigravity)

Add the following to your MCP settings file (e.g. `claude_desktop_config.json` or Antigravity config):

```json
{
  "mcpServers": {
    "first_mcpserver_stdio": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "d:/Projects/MCP Guild",
        "python",
        "CreateMCP/1_MCPServer_stdio.py"
      ]
    }
  }
}
```
