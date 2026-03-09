from ie.processing import (
    load_transcriptions,
    build_user_messages,
    parse_tool_calls,
    save_structured_data,
)
from ie.extractor import extract_medical_information


def run_pipeline(
    input_path: str = "data/raw/transcriptions.csv",
    output_path: str = "data/processed/extracted_data.csv",
):
    """
    Full pipeline:
    1. Load transcription data
    2. Build messages
    3. Extract structured information using OpenAI
    4. Parse tool calls into a dataframe
    5. Save structured output
    """
    df = load_transcriptions(input_path)
    user_messages = build_user_messages(df)
    response = extract_medical_information(user_messages)
    df_structured = parse_tool_calls(response, df)
    save_structured_data(df_structured, output_path)

    return df_structured