import os
from mistralai import Mistral


class LLM:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = Mistral(api_key=self.api_key)
        self.model = "mistral-large-latest"

    def generate_response(self, user_message: str, context: str) -> str:
        """Generates a response from the LLM based on the user message."""
        with open("prompts/system_message_schema.txt", "r", encoding="utf-8") as file:
            system_message_schema = file.read()

        system_message = system_message_schema.replace("{context}", context)

        chat_response = self.client.chat.complete(
            model= self.model,
            messages = [
                {
                    "role": "system",
                    "content": system_message
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ]
        )
        return chat_response.choices[0].message.content