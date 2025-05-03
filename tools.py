from langchain.tools import Tool 
from langchain_community.tools import DuckDuckGoSearchRun
from json import loads, dumps

duck_search = DuckDuckGoSearchRun()
basic_info_tool  = Tool(
    name = "basic_info_tool",
    func=duck_search.run,
    description="""
    Use this to gather fundamental information such as:
    - Name, location, founding date
    - Mission and values
    - Products/services
    - Industry and market segments
    - Businss model
    
    Sources an be from:
    - Company's official website
    - Google
    - etc
    """
)

competitor_comparison_tool = Tool(
    name = "competitor_comparison_tool",
    func=duck_search.run,
    description="""
    Use this to get the following information of the company's competitors:
    - Who are their competitors
    - Market share, price and customer base
    - Competitive advantages and disadvantage
    """
)

def save_to_json(data:str, filename:str="company.json"):
    data_dict = loads(data)
    json_object = dumps(data_dict, indent=4)
    with open(filename, "w") as outfile:
        outfile.write(json_object)


save_json_tool = Tool(
    name = "save_as_json_tool",
    func=save_to_json,
    description="""
    Use this tool to save the final structured company research data into a JSON file.
    Only use after all research is completed and structured into the correct format.
    Input should be the data stringified as JSON, and it will be saved as a file.    """
)

tool_list = [
    basic_info_tool,
    competitor_comparison_tool,
    save_json_tool
]