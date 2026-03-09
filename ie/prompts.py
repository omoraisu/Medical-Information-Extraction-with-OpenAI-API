# Define system instructions
system_message = [
    {
        'role': 'system',
        'content': 'You are data engineer specializing in the medical data. For each transcription, extract age, recommended treatment, and ICD-10 code. Return structured JSON for each entry.'
    }
]