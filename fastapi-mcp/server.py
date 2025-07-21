from fastapi_mcp import FastApiMCP
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# Create FastAPI app
app = FastAPI(
    title="Math MCP server",
    description="A service that provides math tools",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Math MCP running"}

class AddInput(BaseModel):
    a: int
    b: int

# Define tools
@app.post("/api/v1/add", operation_id="add")
def add(input: AddInput) -> int:
    print(f"add called with {input.a}, {input.b}")
    return input.a + input.b

@app.post("/api/v1/subtract", operation_id="subtract")
def subtract(a: int, b: int) -> int:
    print(f"subtract called with {a}, {b}")
    return a - b


mcp = FastApiMCP(app, include_operations=["add", "subtract"])
mcp.mount()

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=9090, reload=True)