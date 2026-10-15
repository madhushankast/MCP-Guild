from fastmcp import FastMCP

# 1. Create an instance of FastMCP for HTTP transport
mcp = FastMCP("1_http_mcp")


# 2. Define Tool 1: fetch_http()
@mcp.tool()
async def fetch_http():
    """Use this tool to fetch data from an HTTP MCP server."""
    # Simulate fetching data from an external API or database source
    return {"data": "Hello, HTTP MCP!"}


# 3. Define Tool 2: process_http(path: str)
@mcp.tool()
async def process_http(path: str):
    """Use this tool to process data over HTTP."""
    # Simulate processing or transforming data received from path
    return {
        "status": "success",
        "processed_path": path,
        "message": f"Processed HTTP data from {path}",
    }


# 4. Run the server using HTTP transport on port 8050
if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8050)
