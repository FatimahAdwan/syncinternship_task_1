import openai
import gradio

openai.api_key = "input your key"

messages = [{"role": "system", "content": "You are a pythonista"}]

def CustomChatGPT(Type):
    messages.append({"role": "user", "content": Type})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

Web = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")

Web.launch(share=True)
