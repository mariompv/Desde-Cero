# AGENT_INICIO

Un chatbot simple usando la API de Nebius AI Studio con el modelo Meta-Llama-3.1-70B-Instruct.

## 🚀 Características

- Integración con Nebius AI Studio
- Uso del modelo Meta-Llama-3.1-70B-Instruct
- Cliente OpenAI compatible
- Respuestas limpias y directas

## 📋 Requisitos

- Python 3.8+
- API Key de Nebius AI Studio

## 🔧 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/AGENT_INICIO.git
cd AGENT_INICIO
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura tu API Key:
   - Crea un archivo `.env` en la raíz del proyecto
   - Añade una línea con `NEBIUS_API_KEY=<tu_api_key>`
   - O exporta la variable de entorno `NEBIUS_API_KEY` antes de ejecutar el script

## 🎯 Uso

Ejecuta el script:
```bash
python main.py
```

El script enviará un mensaje "Hello!" al modelo y mostrará la respuesta.

## 📝 Personalización

Para cambiar el mensaje, edita la línea en `main.py`:
```python
"content": """Hello!"""  # Cambia este mensaje
```

## 🔒 Seguridad

- **IMPORTANTE**: Nunca subas tu API key a GitHub
- El archivo `.gitignore` está configurado para excluir archivos sensibles
- Para uso en producción, usa variables de entorno

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request. 