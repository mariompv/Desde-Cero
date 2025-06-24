import os
from openai import OpenAI

# SOLO PARA USO LOCAL, NO SUBIR ESTA KEY A GIT
api_key = "eyJhbGciOiJIUzI1NiIsImtpZCI6IlV6SXJWd1h0dnprLVRvdzlLZWstc0M1akptWXBvX1VaVkxUZlpnMDRlOFUiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDExNDE1OTM1OTc1NjY3NDI4Mzk4NyIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwiaXNzIjoiYXBpX2tleV9pc3N1ZXIiLCJhdWQiOlsiaHR0cHM6Ly9uZWJpdXMtaW5mZXJlbmNlLmV1LmF1dGgwLmNvbS9hcGkvdjIvIl0sImV4cCI6MTkwODQxMjk1NywidXVpZCI6IjgxMTQzMGY1LTk0ODgtNDg5NC05ZDI1LTJlNDE3YmViZmMyNiIsIm5hbWUiOiJORUJJVVNfQVBJX0tFWSIsImV4cGlyZXNfYXQiOiIyMDMwLTA2LTIzVDAyOjQyOjM3KzAwMDAifQ.VY0PSlk1BB7HoKMgstjbnL3cIyIMRHWmUJmJ_zubIUg"

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

