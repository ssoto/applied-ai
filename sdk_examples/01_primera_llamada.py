import anthropic

# Prerequisitos:
#   pip install anthropic
#   export ANTHROPIC_API_KEY="sk-ant-..."

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": "¿Cómo puedo mejorar mi plan de entrenamiento?"
    }]
)

print(response.content[0].text)
