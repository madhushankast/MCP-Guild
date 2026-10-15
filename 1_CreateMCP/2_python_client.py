import asyncio
import os
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Path to the MCP server script
mcp_server_script = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "1_MCPServer_stdio.py"
)

# Configure stdio server parameters to execute the server via python
server_params = StdioServerParameters(
    command=sys.executable,
    args=[str(mcp_server_script)],
    env=dict(os.environ),
)


async def main():
    print(f"Connecting to MCP server at: {mcp_server_script} ...")

    # Connect to the server through standard I/O (stdio)
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # 1. Initialize session handshake
            await session.initialize()
            print("Connected to MCP server successfully!\n")

            # 2. List tools provided by the server
            tools_response = await session.list_tools()
            print("--- Available Tools ---")
            for tool in tools_response.tools:
                print(f"Tool Name: {tool.name}")
                print(f"Description: {tool.description}")
                print(f"Schema: {getattr(tool, 'input_schema', getattr(tool, 'inputSchema', None))}\n")

            # 3. Call tool: fetch()
            print("--- Calling tool 'fetch' ---")
            fetch_result = await session.call_tool("fetch", arguments={})
            for content in fetch_result.content:
                print(f"Fetch Output: {content.text}")

            # 4. Call tool: process(path=...)
            print("\n--- Calling tool 'process' ---")
            process_result = await session.call_tool(
                "process", arguments={"path": "sample_data.csv"}
            )
            for content in process_result.content:
                print(f"Process Output: {content.text}")


if __name__ == "__main__":
    asyncio.run(main())
