from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletionMessage
from functions import robot_functions_list_1
import json

MODEL = "gpt-4o-mini"

client = OpenAI()

tools = []
for function in robot_functions_list_1:
    tools.append({
        "type": "function",
        "function": function
    })

conversation = [{"role": "system", "content": "You are a helpful AI assistant."}]

def execute_function_call(message: ChatCompletionMessage):
    for tool_call in message.tool_calls:
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        print("func ", name, "(", args, ")")
        conversation.append({
            "tool_call_id": tool_call.id,
            "role": "tool",
            "name": name,
            "content": "",
        })

call_count = 0

def create_completion():
    global call_count
    response = client.chat.completions.create(
        model=MODEL,
        messages=conversation,
        tools=tools
    ) 
    response_message = response.choices[0].message
    conversation.append(response_message)

    call_count += 1

    if call_count > 10:
        return "I'm sorry, I can't help you with that."
    if (response_message.content):
        call_count = 0
        return response_message.content
    if len(response_message.tool_calls) > 0:
        # run the function call
        execute_function_call(response_message)
        # pass the result back to the model
        create_completion()

user_input = ""

while(user_input != "exit"):
    user_input = input("You: ")
    message = {"role": "user", "content": user_input}
    conversation.append(message)

    response = create_completion()
    print("AI: ", response)
