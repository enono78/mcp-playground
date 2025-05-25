from typing import List

import anthropic

from chatbot.tools.execute_tool import execute_tool


class ChatModelQuery:
    def __init__(self, tools: List[dict]):
        self.client = anthropic.Anthropic()
        self.tools: List[dict] = tools

    def process_query(self, query):
        messages = [{'role': 'user', 'content': query}]

        response = self.client.messages.create(max_tokens=2024,
                                               model='claude-3-7-sonnet-20250219',
                                               tools=self.tools,
                                               messages=messages)

        process_query = True
        while process_query:
            assistant_content = []

            for content in response.content:
                if content.type == 'text':

                    print(content.text)
                    assistant_content.append(content)

                    if len(response.content) == 1:
                        process_query = False

                elif content.type == 'tool_use':

                    assistant_content.append(content)
                    messages.append({'role': 'assistant', 'content': assistant_content})

                    tool_id = content.id
                    tool_args = content.input
                    tool_name = content.name
                    print(f"Calling tool {tool_name} with args {tool_args}")

                    result = execute_tool(tool_name, tool_args)
                    messages.append({"role": "user",
                                     "content": [
                                         {
                                             "type": "tool_result",
                                             "tool_use_id": tool_id,
                                             "content": result
                                         }
                                     ]
                                     })
                    response = self.client.messages.create(max_tokens=2024,
                                                           model='claude-3-7-sonnet-20250219',
                                                           tools=self.tools,
                                                           messages=messages)

                    if len(response.content) == 1 and response.content[0].type == "text":
                        print(response.content[0].text)
                        process_query = False

    def chat_loop(self):
        print("Type your queries or 'quit' to exit.")
        while True:
            try:
                query = input("\nQuery: ").strip()
                if query.lower() == 'quit':
                    break

                self.process_query(query)
                print("\n")
            except Exception as e:
                print(f"\nError: {str(e)}")
