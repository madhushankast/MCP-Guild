from fastmcp import FastMCP

# Create an instance of FastMCP
mcp = FastMCP("1_MCPServer_stdio")


@mcp.tool()
async def fetch():
    """Use this tool to fetch data from a source."""
    # Simulate fetching data from a source
    # (e.g., API calls, database query, etc.)
    return {"data": "Hello, MCP!"}


@mcp.tool()
async def process(path: str):
    """Use this tool to process the fetched data."""
    # Simulate processing the fetched data
    # (e.g., transformations, reading a file from path)
    return {
        "status": "success",
        "processed_path": path,
        "message": f"Processed data from {path}",
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
