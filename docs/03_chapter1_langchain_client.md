# Phase 3: Integrating MCP with LangChain

- **Video Reference**: [MCP Full Course For Beginners (With Deployment)](https://www.youtube.com/watch?v=io02ZM0ADqM) — Timestamp: `1:21:38`
- **File**: [`CreateMCP/3_langchain_client.py`](file:///d:/Projects/MCP%20Guild/CreateMCP/3_langchain_client.py)

---

## 🎯 What This Part Does

In this stage, you bridge your MCP server with the **LangChain** ecosystem using `langchain-mcp-adapters`. 

### Key Concepts:
1. **`MultiServerMCPClient`**: A LangChain-native adapter that connects to one or more MCP servers (via `stdio` or `http/sse`), fetches their tool schemas, and converts them into standard LangChain `BaseTool` instances.
2. **Zero-Code Tool Wrapping**: You do not need to rewrite your tools using `@tool` in LangChain. The MCP protocol handles tool metadata, type validation, and execution transparently.
3. **Agent Integration**: Once MCP tools are loaded into LangChain tools, they can be directly passed to models (like OpenAI, Claude, Groq, or Ollama) using ReAct agents (`create_react_agent`).

---

## 📝 Complete Code Breakdown

```python
import asyncio
import os
import sys
from langchain_mcp_adapters.client import MultiServerMCPClient

# 1. Path to the MCP server script
mcp_server_script = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "1_MCPServer_stdio.py"
)


async def main():
    print(f"Connecting to MCP server via LangChain adapter...")
    print(f"Server script: {mcp_server_script}\n")

    # 2. Configure MultiServerMCPClient with stdio transport dictionary
    client = MultiServerMCPClient(
        {
            "my_stdio_server": {
                "transport": "stdio",
                "command": sys.executable,
                "args": [mcp_server_script],
            }
        }
    )

    # 3. Retrieve LangChain-compatible tools from the MCP server
    tools = await client.get_tools()

    print(f"Successfully converted {len(tools)} MCP tool(s) to LangChain tools:")
    for tool in tools:
        print(f" - Name: {tool.name}")
        print(f"   Description: {tool.description}")
        print(f"   Args: {tool.args}\n")

    # 4. Invoke tool 'fetch' using LangChain's standard .ainvoke() interface
    print("--- Invoking 'fetch' tool via LangChain ---")
    fetch_tool = next(t for t in tools if t.name == "fetch")
    fetch_result = await fetch_tool.ainvoke({})
    print(f"Result: {fetch_result}\n")

    # 5. Invoke tool 'process' with required parameter
    print("--- Invoking 'process' tool via LangChain ---")
    process_tool = next(t for t in tools if t.name == "process")
    process_result = await process_tool.ainvoke({"path": "analytics.csv"})
    print(f"Result: {process_result}\n")

    print("LangChain MCP tool integration complete!")


if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🚀 How to Run

```bash
uv run python CreateMCP/3_langchain_client.py
```

---

## 🖥️ Expected Output

```text
Connecting to MCP server via LangChain adapter...
Server script: D:\Projects\MCP Guild\CreateMCP\1_MCPServer_stdio.py

Successfully converted 2 MCP tool(s) to LangChain tools:
 - Name: fetch
   Description: Use this tool to fetch data from a source.
   Args: {}

 - Name: process
   Description: Use this tool to process the fetched data.
   Args: {'path': {'type': 'string'}}

--- Invoking 'fetch' tool via LangChain ---
Result: [{'type': 'text', 'text': '{"data":"Hello, MCP!"}', 'id': 'lc_...'}]

--- Invoking 'process' tool via LangChain ---
Result: [{'type': 'text', 'text': '{"status":"success","processed_path":"analytics.csv","message":"Processed data from analytics.csv"}', 'id': 'lc_...'}]

LangChain MCP tool integration complete!
```

---

## 🧠 Optional: Powering an AI Agent

To let an LLM autonomously decide when to call these tools:

```python
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

# Initialize model
model = ChatOpenAI(model="gpt-4o")

# Pass MCP tools into ReAct Agent
agent = create_react_agent(model, tools)

# Agent will decide which MCP tool to run:
response = await agent.ainvoke(
    {"messages": [("user", "Fetch the latest data and process it from path 'data.csv'")]}
)
print(response["messages"][-1].content)
```
