import openai
def chat_Completion(text):
    openai.api_key = "YOUR_API_KEY"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{text}"}],
        temperature = 0.8
    )
    result = response['choices'][0]['message']['content']
    return result

#print(chat_Completion("Hello"))
