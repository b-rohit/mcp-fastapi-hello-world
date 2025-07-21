from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI
import uvicorn

# MCP service instance
mcp = FastMCP("Math-MCP", stateless_http=True)

# Define tools
@mcp.tool()
def add(a: int, b: int) -> int:
    print(f"add called with {a}, {b}")
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    print(f"subtract called with {a}, {b}")
    return a - b

mcp_app = mcp.streamable_http_app()

# Create FastAPI app
app = FastAPI(
    title="Math MCP server",
    description="A service that provides math tools",
    version="1.0.0",
    lifespan=mcp_app.router.lifespan_context,
)

# Mount the MCP ASGI app
app.mount("/api/v1", mcp_app, "mcp")

# Root path works fine
@app.get("/")
async def root():
    return {"message": "Math MCP running"}


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=9090, reload=True)