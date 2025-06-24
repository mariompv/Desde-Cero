import os
from dotenv import load_dotenv

# LangGraph and LangChain imports
try:
    from langgraph.graph import ChatAgent
    from langchain_openai import ChatOpenAI
    from langchain.agents import tool
except ImportError:
    # These packages may not be installed in the execution environment
    ChatAgent = None
    ChatOpenAI = None
    def tool(func=None, **kwargs):
        return func

# Additional tool libraries
try:
    import tabily as tb
except ImportError:
    tb = None

try:
    from PIL import Image
except ImportError:
    Image = None

try:
    import sympy as sp
except ImportError:
    sp = None

try:
    from duckduckgo_search import DDGS
except ImportError:
    DDGS = None

try:
    import wikipedia
except ImportError:
    wikipedia = None

load_dotenv()
api_key = os.getenv("NEBIUS_API_KEY")
if not api_key:
    raise ValueError("NEBIUS_API_KEY environment variable not set")

# Initialize the LLM client using Nebius endpoint
llm = None
if ChatOpenAI:
    llm = ChatOpenAI(
        base_url="https://api.studio.nebius.com/v1/",
        api_key=api_key,
        model="meta-llama/Meta-Llama-3.1-70B-Instruct",
        temperature=0.6,
    )

# Tool definitions
@tool
def convert_image(input_path: str, output_path: str) -> str:
    """Convert an image to PNG format."""
    if Image is None:
        return "Pillow not installed"
    img = Image.open(input_path)
    img.save(output_path, format="PNG")
    return f"Saved image to {output_path}"

@tool
def evaluate_math(expression: str) -> str:
    """Evaluate a math expression."""
    if sp is None:
        return "sympy not installed"
    try:
        result = sp.sympify(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

@tool
def make_table(data: list) -> str:
    """Create an ASCII table from data."""
    if tb is None:
        return "tabily not installed"
    return tb.tabily(data)

@tool
def search_internet(query: str) -> str:
    """Search the internet using DuckDuckGo."""
    if DDGS is None:
        return "duckduckgo-search not installed"
    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=5):
                results.append(r.get("body", ""))
        return "\n".join(results)
    except Exception as e:
        return f"Error: {e}"

@tool
def search_wikipedia(query: str) -> str:
    """Fetch a summary from Wikipedia."""
    if wikipedia is None:
        return "wikipedia not installed"
    try:
        return wikipedia.summary(query, sentences=2)
    except Exception as e:
        return f"Error: {e}"

# Build the agent with LangGraph if available
if ChatAgent and llm:
    agent = ChatAgent(
        llm=llm,
        tools=[
            convert_image,
            evaluate_math,
            make_table,
            search_internet,
            search_wikipedia,
        ],
    )
else:
    agent = None

def main():
    if agent is None:
        print("LangGraph or dependencies missing. Agent cannot run.")
        return
    print("Enter a message (or 'quit'): ")
    while True:
        user_input = input('> ').strip()
        if user_input.lower() == 'quit':
            break
        response = agent.invoke(user_input)
        print(response)

if __name__ == "__main__":
    main()
