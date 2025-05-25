from dotenv import load_dotenv

from chatbot.queries.process import ChatModelQuery
from chatbot.tools.tools_schema import tools

if __name__ == '__main__':
    # search_papers("computers")
    # print(extract_info("1310.7911v2"))
    load_dotenv()
    model = ChatModelQuery(tools=tools)
    model.chat_loop()


