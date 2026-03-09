import json
import pandas as pd

def load_transcriptions(csv_path: str) -> pd.DataFrame:
    """
    Load the raw transcription dataset.
    """
    return pd.read_csv(csv_path)

def build_user_messages(df: pd.DataFrame) -> list[dict]:
    """
    Convert each dataframe row into a user message for the OpenAI API.
    """
    messages = []

    for _, row in df.iterrows():
        messages.append(
            {
                "role": "user",
                "content": (
                    f"Medical specialty: {row['medical_specialty']}\n"
                    f"Transcription: {row['transcription']}"
                ),
            }
        )

    return messages


def parse_tool_calls(response, df: pd.DataFrame) -> pd.DataFrame:
    """
    Parse tool call arguments from the model response and return
    a structured dataframe.
    """
    new_data = []

    tool_calls = response.choices[0].message.tool_calls

    for i in range(len(df)):
        data = json.loads(tool_calls[i].function.arguments)
        data["medical_specialty"] = df.loc[i, "medical_specialty"]
        new_data.append(data)

    return pd.DataFrame(new_data)

def save_structured_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Save the structured dataframe to CSV.
    """
    df.to_csv(output_path, index=False)