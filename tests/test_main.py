import importlib
import os
import sys
import types
from unittest.mock import MagicMock


def test_main_calls_openai_with_env(monkeypatch):
    # Ensure the project root is on the Python path
    project_root = os.path.dirname(os.path.dirname(__file__))
    monkeypatch.syspath_prepend(project_root)
    # Ensure the expected environment variable is present
    monkeypatch.setenv("NEBIUS_API_KEY", "test-key")

    # Mock the OpenAI client and the dotenv loader
    mock_client = MagicMock()
    mock_completion = MagicMock()
    mock_choice = MagicMock()
    mock_choice.message.content = "hello"
    mock_completion.choices = [mock_choice]
    mock_client.chat.completions.create.return_value = mock_completion

    dummy_openai = types.SimpleNamespace(OpenAI=MagicMock(return_value=mock_client))
    dummy_dotenv = types.SimpleNamespace(load_dotenv=MagicMock())

    monkeypatch.setitem(sys.modules, "openai", dummy_openai)
    monkeypatch.setitem(sys.modules, "dotenv", dummy_dotenv)

    # Import the module; its top-level code will execute using the mocks
    if "main" in sys.modules:
        importlib.reload(sys.modules["main"])
    else:
        importlib.import_module("main")

    # Assert the OpenAI client was instantiated with the env key
    dummy_openai.OpenAI.assert_called_once_with(
        base_url="https://api.studio.nebius.com/v1/",
        api_key="test-key",
    )

    # Ensure the expected completion call occurred
    mock_client.chat.completions.create.assert_called_once_with(
        model="meta-llama/Meta-Llama-3.1-70B-Instruct",
        messages=[{"role": "user", "content": "Hello!"}],
        temperature=0.6,
    )
