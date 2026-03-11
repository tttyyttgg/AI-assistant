from ollama import chat

messages = []#blank message memory

def brain(text):

    global messages

    if text == "remove all history":
        messages = []
        return "Memory cleared"

    messages.append({"role": "user", "content": text})#add text to blank memory so that ai can remember 

    ai_reply = ""  #blank variable 

    stream = chat(
        model="qwen2.5:1.5b",
        messages=messages,
        stream=True
    )

    for chunk in stream:
        part = chunk.message.content
        if part:
            ai_reply += part
            print(part, end="", flush=True)

    print()

    messages.append({"role": "assistant", "content": ai_reply})

    if len(messages) > 10:
        messages = messages[-10:]

    return ai_reply
