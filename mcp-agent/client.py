import asyncio
from dotenv import load_dotenv
from rich import print
from mcp.types import CallToolResult
from mcp_agent.agents.agent import Agent
from mcp_agent.app import MCPApp

load_dotenv()  # load environment variables from .env


async def test_sse():
    app: MCPApp = MCPApp(name="test-app")
    async with app.run():
        print("MCP App initialized.")

        agent: Agent = Agent(
            name="agent",
            instruction="You are an assistant",
            server_names=["mcp_math_server_sse"],
        )

        async with agent:
            call_tool_result: CallToolResult = await agent.call_tool(
                "add",
                arguments= {
                    "a": 4,
                    "b": 4
                }
            )
            print("result", call_tool_result.content[0].text )

            assert call_tool_result.content[0].text == "8"
            print("SSE test passed!")


if __name__ == "__main__":
    asyncio.run(test_sse())