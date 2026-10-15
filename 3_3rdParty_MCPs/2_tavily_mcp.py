import asyncio
import os
import sys
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Load environment variables from .env
load_dotenv()


async def main():
    tavily_api_key = os.getenv("TAVILY_API_KEY", "")

    if not tavily_api_key:
        print("=================================================================")
        print("Note: TAVILY_API_KEY is not set in environment or .env file.")
        print("Hosted MCP servers require authentication via API key in the URL.")
        print("Get a free API key at: https://tavily.com")
        print("Add to .env: TAVILY_API_KEY=your_key_here")
        print("=================================================================\n")
        return

    tavily_url = f"https://mcp.tavily.com/mcp/?tavilyApiKey={tavily_api_key}"
    print(f"Connecting to 3rd-Party Hosted MCP server (Tavily) over HTTP...")

    # 1. Initialize MultiServerMCPClient targeting the remote hosted server
    client = MultiServerMCPClient(
        {
            "tavily_search": {
                "transport": "streamable_http",
                "url": tavily_url,
            }
        }
    )

    # 2. Discover tools hosted on the remote server
    tools = await client.get_tools()

    print(f"Connected! Discovered {len(tools)} tool(s) on Tavily MCP:")
    for tool in tools:
        print(f" - Tool: {tool.name}")
        print(f"   Description: {tool.description}")
        print(f"   Args: {tool.args}\n")

    # 3. Invoke tool if available
    search_tool = next((t for t in tools if "search" in t.name), None)
    if search_tool:
        print("--- Executing live search via Tavily Hosted MCP ---")
        result = await search_tool.ainvoke({"query": "What is Model Context Protocol?"})
        print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
