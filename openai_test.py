from openai import OpenAI

client = OpenAI()

message = {"role":"user", "content": input("This is the beginning of your chat with AI. [To exit, send \"###\".]\n\nYou:")}

conversation = [{"role": "system", "content": "DIRECTIVE_FOR_gpt-3.5-turbo"}]

while(message["content"]!="###"):
    conversation.append(message)
    completion = client.chat.completions.create(model="gpt-4o-mini", messages=conversation) 
    message["content"] = input(f"Assistant: {completion.choices[0].message.content} \nYou: ")
    print()
    conversation.append(completion.choices[0].message)
