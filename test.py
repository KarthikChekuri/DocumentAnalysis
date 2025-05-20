from openai import OpenAI

client = OpenAI(api_key="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")

models = client.models.list()
for m in models.data:
    print(m.id)

print("✅ Script finished")
