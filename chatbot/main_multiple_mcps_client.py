import asyncio

from chatbot.queries.multiple_mcps_chat_bot import MCP_ChatBot


async def main():
    chatbot = MCP_ChatBot()
    try:
        # the mcp clients and sessions are not initialized using "with"
        # like in the previous lesson
        # so the cleanup should be manually handled
        await chatbot.connect_to_servers()  # new!
        await chatbot.chat_loop()
    finally:
        await chatbot.cleanup()  # new!


if __name__ == "__main__":
    asyncio.run(main())