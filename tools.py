from langchain.tools import Tool 
from langchain_community.tools import DuckDuckGoSearchRun


# def basic_info_funct(query):
#     print(query)
#     return ""
company_search = DuckDuckGoSearchRun()
basic_info_tool  = Tool(
    name = "basic_info_tool",
    func=company_search.run,
    description="""
    Use this to gather fundamental information such as:
    - Name
    - Location
    - Founding date
    - Mission
    - Values
    
    Sources an be from:
    - Company's official website
    - Google
    - etc
    """
)


tool_list = [
    basic_info_tool
]