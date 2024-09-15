from openai import OpenAI

client=OpenAI(
    api_key="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"
)
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant like alexa and google cloud named jarvis."},
        {
            "role": "user",
            "content": "What is coding ."
        }
    ]
)
print(completion.choices[0].message)