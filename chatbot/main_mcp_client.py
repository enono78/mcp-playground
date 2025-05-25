import asyncio

from chatbot.queries.mcp_chat_bot import MCP_ChatBot


async def main():
    chatbot = MCP_ChatBot()
    await chatbot.connect_to_server_and_run()


if __name__ == "__main__":
    asyncio.run(main())