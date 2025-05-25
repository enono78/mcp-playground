import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mcp.server.fastmcp import FastMCP
from chatbot.tools.papers.search_papers import search_papers as search_papers_tool
from chatbot.tools.papers.extract_info import extract_info as extract_info_tool



# Initialize FastMCP server
mcp = FastMCP("research")

@mcp.tool()
def search_papers(topic: str, max_results: int = 5) -> List[str]:
    return search_papers_tool(topic, max_results)

@mcp.tool()
def extract_info(paper_id: str) -> str:
    return extract_info_tool(paper_id)

if __name__ == '__main__':
    mcp.run(transport="stdio")
