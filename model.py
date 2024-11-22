from groq import Groq

client = Groq(api_key="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")
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")



#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