import asyncio
import os
import sys
from langchain_mcp_adapters.client import MultiServerMCPClient

# Path to the MCP server script
mcp_server_script = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "1_MCPServer_stdio.py"
)


async def main():
    print(f"Connecting to MCP server via LangChain adapter...")
    print(f"Server script: {mcp_server_script}\n")

    # 1. Initialize MultiServerMCPClient with stdio transport configuration
    client = MultiServerMCPClient(
        {
            "my_stdio_server": {
                "transport": "stdio",
                "command": sys.executable,
                "args": [mcp_server_script],
            }
        }
    )

    # 2. Retrieve LangChain-compatible tools from the MCP server
    tools = await client.get_tools()

    print(f"Successfully converted {len(tools)} MCP tool(s) to LangChain tools:")
    for tool in tools:
        print(f" - Name: {tool.name}")
        print(f"   Description: {tool.description}")
        print(f"   Args: {tool.args}\n")

    # 3. Invoke tool 'fetch' using LangChain's .ainvoke()
    print("--- Invoking 'fetch' tool via LangChain ---")
    fetch_tool = next(t for t in tools if t.name == "fetch")
    fetch_result = await fetch_tool.ainvoke({})
    print(f"Result: {fetch_result}\n")

    # 4. Invoke tool 'process' using LangChain's .ainvoke()
    print("--- Invoking 'process' tool via LangChain ---")
    process_tool = next(t for t in tools if t.name == "process")
    process_result = await process_tool.ainvoke({"path": "analytics.csv"})
    print(f"Result: {process_result}\n")

    print("LangChain MCP tool integration complete!")


if __name__ == "__main__":
    asyncio.run(main())
