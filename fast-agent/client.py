import asyncio
from mcp_agent.core.fastagent import FastAgent

fast = FastAgent("Tool Caller")

# Connect to remote MCP server and call the tool
@fast.agent(
    "tool_caller",
    "Call the add tool on the MCP server.",
    servers=["mcp_math_server_sse"]
)
async def main():
    async with fast.run() as agent:
        print("agent", agent)
        result = await agent.tool_caller.call_tool("add",  arguments= {
                    "a": 4,
                    "b": 4
                })
        print("Tool result:", result.content[0].text)

if __name__ == "__main__":
    asyncio.run(main())

