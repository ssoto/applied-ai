import anthropic

client = anthropic.Anthropic()

# --- Datos simulados — en producción serían consultas a tu BD ---

USUARIOS = {
    "u123": {"nombre": "María García", "nivel": "intermedio", "objetivo": "resistencia"},
    "u456": {"nombre": "Carlos López", "nivel": "principiante", "objetivo": "pérdida de peso"},
}

PLANES = {
    "u123": {"días": ["lunes", "miércoles", "viernes"], "cardio": "30 min", "fuerza": "45 min"},
    "u456": {"días": ["martes", "jueves"], "cardio": "20 min", "fuerza": "20 min"},
}

# --- Herramientas ---

tools = [
    {
        "name": "buscar_usuario",
        "description": "Busca un usuario por nombre. Devuelve id, nivel y objetivo.",
        "input_schema": {
            "type": "object",
            "properties": {
                "nombre": {"type": "string", "description": "Nombre completo del usuario"}
            },
            "required": ["nombre"]
        }
    },
    {
        "name": "obtener_plan",
        "description": "Devuelve el plan de entrenamiento actual del usuario.",
        "input_schema": {
            "type": "object",
            "properties": {
                "usuario_id": {"type": "string"}
            },
            "required": ["usuario_id"]
        }
    }
]

# --- Lógica de ejecución de herramientas ---

def ejecutar_tool(nombre: str, params: dict):
    if nombre == "buscar_usuario":
        for uid, u in USUARIOS.items():
            if params["nombre"].lower() in u["nombre"].lower():
                return {"id": uid, **u}
        return {"error": "Usuario no encontrado"}

    if nombre == "obtener_plan":
        return PLANES.get(params["usuario_id"], {"error": "Plan no encontrado"})

# --- Loop del agente ---

system_prompt = (
    "Eres un asistente de FitCoach, una plataforma de entrenamiento personalizado. "
    "Ayuda a los usuarios con información sobre sus planes usando las herramientas disponibles. "
    "Sé conciso y claro."
)

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
                print(f"  → {block.name}({block.input})")
                data = ejecutar_tool(block.name, block.input)
                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(data)
                })

        messages.append({"role": "user", "content": results})


if __name__ == "__main__":
    preguntas = [
        "¿Cuál es el plan de entrenamiento de María García?",
        "¿Cuántos días entrena Carlos López a la semana?",
    ]
    for pregunta in preguntas:
        print(f"\nUsuario: {pregunta}")
        print(f"FitCoach: {run_agent(pregunta)}")
