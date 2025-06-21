
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent


async def main():
    print("Starting MultiServer MCP Client 8...")
    client = MultiServerMCPClient(
        {
            "math":{
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio"
            }
            ,
            "weather":{
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable_http"
            }
        }
    )

    model = ChatGroq(
        api_key="",
        model="qwen-qwq-32b"
    )
    print("Client created, fetching tools...")
    tools = await client.get_tools()
    print("Tools fetched, creating agent...")
    agent = create_react_agent(
        model=model,
        tools=tools
    )
    print("Agent created, invoking tools...")



    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "add 5 and 3"}]},
    )

    print(f"Math Response: {math_response['messages'][-1].content}")

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is the weather in New York?"}]},
    )
    print(f"Weather Response: {weather_response['messages'][-1].content}")



if __name__ == "__main__":
    import asyncio
    print("Starting MultiServer MCP Client 50...")
    import os
    asyncio.run(main())    