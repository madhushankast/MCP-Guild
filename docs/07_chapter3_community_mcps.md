# Phase 7: Community & 3rd-Party Hosted MCP Servers

- **Video Reference**: [MCP Full Course For Beginners (With Deployment)](https://www.youtube.com/watch?v=io02ZM0ADqM)
  - Part 1: **Using Community MCPs** — Timestamp: `2:08:17`
  - Part 2: **Using 3rd-Party Hosted MCPs** — Timestamp: `2:23:08`
- **Files**:
  - [`3_3rdParty_MCPs/1_community_mcp.py`](file:///d:/Projects/MCP%20Guild/3_3rdParty_MCPs/1_community_mcp.py)
  - [`3_3rdParty_MCPs/2_tavily_mcp.py`](file:///d:/Projects/MCP%20Guild/3_3rdParty_MCPs/2_tavily_mcp.py)

---

## 🎯 What This Part Does

Up until now, we built and hosted our own MCP servers from scratch. In **Chapter 3**, we learn how to consume MCP servers created and hosted by others:

### 1. Community MCPs via `uvx` / `npx`
Instead of writing a custom server or cloning code, you can use pre-packaged community MCP servers published to PyPI or npm.
- **How it works**: `MultiServerMCPClient` launches the tool on demand using `uvx` (for Python packages) or `npx` (for Node.js packages) over STDIO.
- **Example**: `duckduckgo-mcp-server` provides instant web search without requiring any API keys or server code.

### 2. 3rd-Party Hosted MCP Servers
Companies and services host remote MCP endpoints in the cloud accessible over Streamable HTTP or SSE.
- **How it works**: You connect directly to their HTTPS endpoint by supplying an API key in the URL query string or authentication headers.
- **Example**: Tavily AI Search (`https://mcp.tavily.com/mcp/?tavilyApiKey=...`).

---

## 📝 Part 1: Community MCP Code Breakdown

File: [`3_3rdParty_MCPs/1_community_mcp.py`](file:///d:/Projects/MCP%20Guild/3_3rdParty_MCPs/1_community_mcp.py)

```python
import asyncio
import sys
from langchain_mcp_adapters.client import MultiServerMCPClient

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


async def main():
    print("Connecting to Community MCP Server via uvx (duckduckgo-mcp-server)...")

    # 1. Spawn community server using uvx on demand over STDIO
    client = MultiServerMCPClient(
        {
            "duckduckgo_search": {
                "transport": "stdio",
                "command": "uvx",
                "args": ["duckduckgo-mcp-server"],
            }
        }
    )

    # 2. Retrieve the tools exposed by the community server
    tools = await client.get_tools()

    print(f"\nSuccessfully discovered {len(tools)} tool(s) from Community MCP:")
    for tool in tools:
        print(f" - Tool Name: {tool.name}")
        print(f"   Description: {tool.description}")
        print(f"   Args: {tool.args}\n")

    # 3. Invoke the community tool 'search' with a live query
    search_tool = next(t for t in tools if t.name == "search")
    query = "Model Context Protocol LangChain"
    print(f"--- Executing search for: '{query}' ---")
    search_results = await search_tool.ainvoke({"query": query})

    print("\n--- Search Results ---")
    for item in search_results:
        print(item.get("text", item))


if __name__ == "__main__":
    asyncio.run(main())
```

---

## 📝 Part 2: Hosted 3rd-Party MCP Code Breakdown

File: [`3_3rdParty_MCPs/2_tavily_mcp.py`](file:///d:/Projects/MCP%20Guild/3_3rdParty_MCPs/2_tavily_mcp.py)

```python
import asyncio
import os
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()


async def main():
    tavily_api_key = os.getenv("TAVILY_API_KEY", "")

    if not tavily_api_key:
        print("Note: TAVILY_API_KEY not set in .env. Skipping live call.")
        return

    # Hosted cloud endpoint with API key authentication
    tavily_url = f"https://mcp.tavily.com/mcp/?tavilyApiKey={tavily_api_key}"

    client = MultiServerMCPClient(
        {
            "tavily_search": {
                "transport": "streamable_http",
                "url": tavily_url,
            }
        }
    )

    tools = await client.get_tools()
    print(f"Discovered tools on Tavily: {[t.name for t in tools]}")


if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🚀 How to Run

### 1. Run Community MCP (DuckDuckGo via uvx):
```bash
uv run python 3_3rdParty_MCPs/1_community_mcp.py
```

### 2. Run Cloud-Hosted MCP (Tavily AI Search):
1. Store your Tavily API key in `.env`:
   ```env
   TAVILY_API_KEY=your_key_here
   ```
2. Run the client:
   ```bash
   uv run python 3_3rdParty_MCPs/2_tavily_mcp.py
   ```

### ✅ Verified Tavily Output:
```text
Connecting to 3rd-Party Hosted MCP server (Tavily) over HTTP...
Connected! Discovered 5 tool(s) on Tavily MCP:
 - Tool: tavily_search
 - Tool: tavily_extract
 - Tool: tavily_crawl
 - Tool: tavily_map
 - Tool: tavily_research

--- Executing live search via Tavily Hosted MCP ---
Result: [{'type': 'text', 'text': '{"query":"What is Model Context Protocol?","results":[{"title":"Model Context Protocol","url":"https://en.wikipedia.org/wiki/Model_Context_Protocol"...}]'}]
```
