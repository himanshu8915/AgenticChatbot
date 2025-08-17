from dotenv import load_dotenv
load_dotenv()


from langchain_community.tools import TavilySearchResults
search_tool=TavilySearchResults()

class ToolKit:

    @staticmethod
    def return_tools():
        return [search_tool]