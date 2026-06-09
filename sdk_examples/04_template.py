import anthropic

# =============================================================
# TEMPLATE — adapta este agente a tu startup
#
# Pasos:
#   1. Define tus herramientas en `tools`
#   2. Implementa la lógica en `ejecutar_tool`
#   3. Personaliza el `system_prompt`
#   4. El loop del agente no necesita cambios
# =============================================================

client = anthropic.Anthropic()

# --- 1. Define tus herramientas ---

tools = [
    {
        "name": "tu_tool_aqui",                         # ← cambia el nombre
        "description": "Qué hace tu tool en lenguaje natural para que Claude la entienda",
        "input_schema": {
            "type": "object",
            "properties": {
                "parametro": {
                    "type": "string",
                    "description": "Descripción del parámetro"
                }
            },
            "required": ["parametro"]
        }
    }
    # Añade más tools aquí siguiendo el mismo esquema
]

# --- 2. Conecta con tus datos ---

def ejecutar_tool(nombre: str, params: dict):
    if nombre == "tu_tool_aqui":
        # TODO: sustituir por tu lógica real (BD, API, fichero...)
        return {"resultado": f"Datos para: {params['parametro']}"}

# --- 3. Define el comportamiento del agente ---

system_prompt = (
    "Eres un asistente de [TU STARTUP]. "
    "Tu función es [describe qué hace]. "
    "Usa las herramientas disponibles para responder con datos reales."
)

# --- 4. Loop del agente — no necesitas tocarlo ---

def run_agent(pregunta: str) -> str:
    messages = [{"role": "user", "content": pregunta}]

    while True:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system=system_prompt,
            tools=tools,
            messages=messages
        )

        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            return response.content[0].text

        results = []
        for block in response.content:
            if block.type == "tool_use":
                data = ejecutar_tool(block.name, block.input)
                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(data)
                })

        messages.append({"role": "user", "content": results})


if __name__ == "__main__":
    while True:
        pregunta = input("\nTú: ").strip()
        if not pregunta:
            break
        print(f"Agente: {run_agent(pregunta)}")
