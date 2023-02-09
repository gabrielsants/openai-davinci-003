import openai as ai

def chat(question,chat_log = None) -> str:
    if(chat_log == None):
        chat_log = start_chat_log
    prompt = f"{chat_log}Human: {question}\nAI:"
    response = completion.create(
        prompt = prompt, 
        model="text-davinci-003",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop = "\nHuman: ")
    return response.choices[0].text

if __name__ == "__main__":
    ai.api_key = YOU_API_KEY

    completion = ai.Completion()

    start_chat_log = """Human: Hello, I am Human.
    AI: Hello, human I am openai gpt3.
    Human: How are you?
    AI: I am fine, thanks for asking. 
    """

    print("\nYou\'re chatting with openai model text-davinci-003!\nType quit any time to stop the conversation. Enjoy!\n")
    question = ""
    while True:
        question = input("Me: ")
        if question == "quit":
            break
        print("AI: ",chat(question,start_chat_log))
