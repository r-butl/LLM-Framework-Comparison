from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_core.messages import ToolMessage
from termcolor import colored
import robot_functions_list
from turtle_bot import TurtleRobot
from langgraph.checkpoint.memory import MemorySaver
from ROS_LLM_interfaces import Response, Request
from langchain_core.messages import HumanMessage

MODEL = "gpt-4o-mini"

INITIAL_PROMPT = (
    "You are a helpful AI assistant"
)

memory = MemorySaver()

turtelbot = TurtleRobot()
def tool_node(state: dict):
    result = []
    for tool_call in state["messages"][-1].tool_calls:
        response = turtelbot.function_call_callback({ "request_text": tool_call }, { "response_text": None })
        result.append(ToolMessage(content=response.response_text, tool_call_id=tool_call["id"]))
    return {"messages": result}

model = ChatOpenAI(model=MODEL).bind_tools(robot_functions_list)

agent = create_react_agent(model, tool_node, state_modifier=INITIAL_PROMPT, checkpointer=memory)


user_input = ""

while(user_input != "exit"):
    user_input = input(colored("You: ", "blue"))
    message = {"role": "user", "content": user_input}
    print(agent.invoke(
        {"messages": [HumanMessage("user_input")]},
    ))