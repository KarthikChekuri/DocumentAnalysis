from openai import OpenAI

client = OpenAI(api_key="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")

models = client.models.list()

print("Available models:")

for model in models.data:
    print("-", model.id)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Say AI"}]
)
print(response.choices[0].message.content)
