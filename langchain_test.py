import os
from langchain_openai import ChatOpenAI
from langchain_community.callbacks import get_openai_callback
from turtle_bot import robot_functions_list_1, TurtleRobot
from ROS_LLM_interfaces import Response, Request
import json

# For ROS-LLM System interface emulation
robot = TurtleRobot()
response = Response()
request = Request()

# Create an LLM with an agent that can access these tools
llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools(robot_functions_list_1)

query = "Have the robot navigate a square pattern on the ground."

# Get the response with token usage data
with get_openai_callback() as cb:
    print()
    tool_calls = llm_with_tools.invoke(query).tool_calls
    print(tool_calls)
    print()
print()

print(f"Usage information: {cb}")

# call all of the tools in order
for call in tool_calls:
    # Redump the json text into into a string for the function callback, I ended up modifying it
    #   anyway.
    request.request_text = json.dumps(call)
    robot.function_call_callback(request=request, response=response)

