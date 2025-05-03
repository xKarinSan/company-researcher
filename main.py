from os import getenv
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai import ChatOpenAI

from langchain.chains import LLMChain
from langchain_core.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from tools import tool_list
from classes import GeneralInfo
load_dotenv()

openai_api_key = getenv("OPENAI_API_KEY","")
llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)
parser = PydanticOutputParser(pydantic_object=GeneralInfo)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert researcher that does a thorough research on a specified company
            Answer the user query and use the necessary tools.
            \n {format_instructions}
            """
        ),
        (
            "placeholder",
            "{chat_history}"
        ),
        (
            "human",
            "{query}"
        ),
        (
            "placeholder",
            "{agent_scratchpad}"
        )
    ]
).partial(format_instructions = parser.get_format_instructions())

tools = tool_list

research_agent = create_tool_calling_agent(
    llm = llm,
    prompt = prompt,
    tools = tools
)

agent_executor = AgentExecutor(agent=research_agent, tools=tools, verbose=True)
query = input("What company do you want to know about?")
raw_response = agent_executor.invoke({"query":query})

try:
    structured_response = parser.parse(raw_response.get("output"))
    print(f"Name: \n {structured_response.name}")
    print(f"Locaton: \n {structured_response.location}")
    print(f"Founding Date: \n {structured_response.founding_date}")
    print(f"Mission: \n {structured_response.mission}")
    print("Values: ")
    for value in structured_response.values:
        print(f" {value}")
    print("Products: ")
    for product in structured_response.products:
        print(f" {product}")
    print(f"Industry: \n {structured_response.industry}")
    print(f"Market Segment: \n {structured_response.market_segment}")
    print(f"Business model: \n {structured_response.business_model}")

except Exception as e:
    print("Error parsing response",e, "Raw Response - ",raw_response)