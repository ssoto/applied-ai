import anthropic

client = anthropic.Anthropic()

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

# Implementación fake — en producción sería una consulta a BD o API
def buscar_usuario(nombre: str) -> dict:
    usuarios = {
        "maría garcía": {"id": "u123", "nivel": "intermedio", "objetivo": "resistencia"},
        "carlos lópez": {"id": "u456", "nivel": "principiante", "objetivo": "pérdida de peso"},
    }
    return usuarios.get(nombre.lower(), {"error": "Usuario no encontrado"})


messages = [{"role": "user", "content": "¿Cuál es el perfil de María García?"}]

# Turno 1: Claude pide llamar la herramienta
response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    tools=[herramienta],
    messages=messages,
)

print(f"stop_reason: {response.stop_reason}")

messages.append({"role": "assistant", "content": response.content})

# Ejecutar las tools que Claude pidió y recoger resultados
tool_results = []
for block in response.content:
    if block.type == "tool_use":
        print(f"Claude llama: {block.name}({block.input})")
        data = buscar_usuario(block.input["nombre"])
        print(f"Resultado: {data}")
        tool_results.append({
            "type": "tool_result",
            "tool_use_id": block.id,
            "content": str(data),
        })

messages.append({"role": "user", "content": tool_results})

# Turno 2: Claude genera la respuesta final con los datos reales
final = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    tools=[herramienta],
    messages=messages,
)

print(f"\nRespuesta: {final.content[0].text}")
