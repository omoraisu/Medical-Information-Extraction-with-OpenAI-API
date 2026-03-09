from config import client, model
from prompts import system_message
from schemas import function_definition


def extract_medical_information(user_messages: list[dict]):
    """
    Call the OpenAI API with the system message, user messages,
    and function definition schema.
    """
    messages = [system_message] + user_messages

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=function_definition,
    )

    return response