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
