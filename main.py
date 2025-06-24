import os
from openai import OpenAI
from dotenv import load_dotenv

# Carga tu API key desde un archivo `.env` o una variable de entorno.
# Crea un archivo `.env` con `NEBIUS_API_KEY=<tu_api_key>` o exporta la variable
# antes de ejecutar este script. No edites este archivo para agregar la clave.
load_dotenv()

api_key = os.getenv("NEBIUS_API_KEY")
if not api_key:
    raise ValueError("NEBIUS_API_KEY environment variable not set")

print("Iniciando conexión con Nebius API...")
print(f"Longitud de la API key: {len(api_key)}")

client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key=api_key,
)

print("Enviando solicitud al modelo...")

completion = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-70B-Instruct",
    messages=[
        {
            "role": "user",
            "content": """Hello!"""
        }
    ],
    temperature=0.6
)

print(completion.choices[0].message.content)
