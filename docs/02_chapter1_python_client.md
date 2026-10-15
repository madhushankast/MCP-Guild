# Phase 2: Creating a Python MCP Client

- **Video Reference**: [MCP Full Course For Beginners (With Deployment)](https://www.youtube.com/watch?v=io02ZM0ADqM) — Timestamp: `1:01:00`
- **File**: [`CreateMCP/2_python_client.py`](file:///d:/Projects/MCP%20Guild/CreateMCP/2_python_client.py)

---

## 🎯 What This Part Does

In this stage, you build a custom Python client using the official `mcp` SDK to interact directly with your STDIO server without needing a third-party app like Claude Desktop.

### Key Concepts:
1. **`StdioServerParameters`**: Configures how the client launches the MCP server process (`python CreateMCP/1_MCPServer_stdio.py`).
2. **`stdio_client` Context Manager**: Spawns the subprocess, attaches to its standard input/output pipes, and manages stream lifecycles.
3. **`ClientSession`**: Handles the MCP JSON-RPC protocol negotiation.
4. **Lifecycle**:
   - Handshake: `await session.initialize()`
   - Tool Discovery: `await session.list_tools()`
   - Tool Execution: `await session.call_tool(name, arguments)`

---

## 📝 Complete Code Breakdown

```python
import asyncio
import os
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# 1. Dynamically resolve the absolute path to the server script
mcp_server_script = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "1_MCPServer_stdio.py"
)

# 2. Configure the subprocess execution parameters
server_params = StdioServerParameters(
    command=sys.executable,        # Current python executable from virtual environment
    args=[str(mcp_server_script)], # Server script to launch
    env=dict(os.environ),          # Inherit existing environment variables
)


async def main():
    print(f"Connecting to MCP server at: {mcp_server_script} ...")

    # 3. Establish stdio streams to the child process
    async with stdio_client(server_params) as (read_stream, write_stream):
        # 4. Open ClientSession over the streams
        async with ClientSession(read_stream, write_stream) as session:
            # Step A: Handshake initialization
            await session.initialize()
            print("Connected to MCP server successfully!\n")

            # Step B: Discover tools registered on the server
            tools_response = await session.list_tools()
            print("--- Available Tools ---")
            for tool in tools_response.tools:
                print(f"Tool Name: {tool.name}")
                print(f"Description: {tool.description}")
                print(f"Schema: {getattr(tool, 'input_schema', getattr(tool, 'inputSchema', None))}\n")

            # Step C: Call 'fetch' tool
            print("--- Calling tool 'fetch' ---")
            fetch_result = await session.call_tool("fetch", arguments={})
            for content in fetch_result.content:
                print(f"Fetch Output: {content.text}")

            # Step D: Call 'process' tool with arguments
            print("\n--- Calling tool 'process' ---")
            process_result = await session.call_tool(
                "process", arguments={"path": "sample_data.csv"}
            )
            for content in process_result.content:
                print(f"Process Output: {content.text}")


if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🚀 How to Run

```bash
uv run python CreateMCP/2_python_client.py
```

---

## 🖥️ Expected Output

```text
Connecting to MCP server at: D:\Projects\MCP Guild\CreateMCP\1_MCPServer_stdio.py ...
Connected to MCP server successfully!

--- Available Tools ---
Tool Name: fetch
Description: Use this tool to fetch data from a source.
Schema: {'additionalProperties': False, 'properties': {}, 'type': 'object'}

Tool Name: process
Description: Use this tool to process the fetched data.
Schema: {'additionalProperties': False, 'properties': {'path': {'type': 'string'}}, 'required': ['path'], 'type': 'object'}

--- Calling tool 'fetch' ---
Fetch Output: {"data":"Hello, MCP!"}

--- Calling tool 'process' ---
Process Output: {"status":"success","processed_path":"sample_data.csv","message":"Processed data from sample_data.csv"}
```

---

## 💡 Key Learnings & Gotchas
- **Subprocess Management**: The client handles starting and terminating the server cleanly when exiting the `async with` blocks.
- **Pydantic Model Compatibility**: In modern MCP Python packages, tool schema is accessed via `tool.input_schema` (snake_case) rather than `tool.inputSchema` (camelCase).
