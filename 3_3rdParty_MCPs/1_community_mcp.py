import asyncio
import sys
from langchain_mcp_adapters.client import MultiServerMCPClient

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


async def main():
    print("Connecting to Community MCP Server via uvx (duckduckgo-mcp-server)...")

    # 1. Configure MultiServerMCPClient to run a community MCP server on-demand using uvx
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
