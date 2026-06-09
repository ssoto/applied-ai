import anthropic

client = anthropic.Anthropic()

# Una herramienta = un nombre, una descripción (para Claude) y un esquema de parámetros
herramienta = {
    "name": "buscar_usuario",
    "description": "Busca un usuario por nombre y devuelve su perfil completo",
    "input_schema": {
        "type": "object",
        "properties": {
            "nombre": {
                "type": "string",
                "description": "Nombre completo del usuario"
            }
        },
        "required": ["nombre"]
    }
}

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    tools=[herramienta],
    messages=[{
        "role": "user",
        "content": "¿Cuál es el perfil de María García?"
    }]
)

# stop_reason == "tool_use" → Claude quiere llamar una herramienta
print(f"stop_reason: {response.stop_reason}")
for block in response.content:
    if block.type == "tool_use":
        print(f"Claude quiere llamar: {block.name}")
        print(f"Con parámetros: {block.input}")
