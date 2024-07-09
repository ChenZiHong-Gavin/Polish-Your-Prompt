import os
from typing import Callable, List, Optional, Dict, Any
import openai
import tiktoken
from retry import retry
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env"))


class OpenAIChat:
    def __init__(
        self,
        api_base: Optional[str] = os.getenv("API_BASE"),
        api_key: Optional[str] = os.getenv("API_KEY"),
        model_name: str = "gpt-3.5-turbo",
        max_tokens: int = 1000,
        temperature: float = 0.0,
    ) -> None:
        openai.api_key = api_key
        openai.api_base = api_base
        self.model = model_name
        self.max_tokens = max_tokens
        self.temperature = temperature

    @retry(tries=3, delay=1)
    def generate(
        self,
        messages: Optional[List[Dict[str, Any]]] = None,
        prompt: Optional[str] = None,
    ) -> str:
        if messages is None:
            assert prompt is not None, "Messages or prompt must be provided."
            messages = [{"role": "user", "content": prompt}]
        try:
            completions = openai.ChatCompletion.create(
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                messages=messages,
            )
            return completions.choices[0].message.content
        except openai.error.InvalidRequestError as e:
            return str(f"Error: {e}")
        except openai.error.AuthenticationError:
            return "Error: The provided OpenAI API key is invalid"
        except Exception as e:
            print(f"Retrying LLM call {e}")
            raise e

    def generate_streaming(
        self,
        messages: Optional[List[Dict[str, Any]]] = None,
        prompt: Optional[str] = None,
        on_token_callback: Callable = None,
    ) -> str:
        if messages is None:
            assert prompt is not None, "Messages or prompt must be provided."
            messages = [{"role": "user", "content": prompt}]
        completions = openai.ChatCompletion.create(
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            messages=messages,
            stream=True,
        )
        result = ""
        for message in completions:
            delta = message["choices"][0]["delta"]
            if "content" in delta:
                result += delta["content"]
            on_token_callback(message)
        return result

    def num_tokens_from_string(self, string: str) -> int:
        """Get token count from string."""
        encoding = tiktoken.encoding_for_model(self.model)
        num_tokens = len(encoding.encode(string))
        return num_tokens
