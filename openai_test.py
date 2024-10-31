from openai import OpenAI

client = OpenAI()

conversation = [{"role": "system", "content": "You are a helpful AI assistant."}]

user_input = ""

while(user_input != "exit"):
    user_input = input("You: ")
    message = {"role": "user", "content": user_input}
    conversation.append(message)
    completion = client.chat.completions.create(model="gpt-4o-mini", messages=conversation) 
    response = completion.choices[0].message.content
    print("AI : " + response)
    conversation.append({"role": "system", "content": response})
    
