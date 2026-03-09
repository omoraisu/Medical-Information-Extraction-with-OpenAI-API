# Define function definition
function_definition = [{
    'type': 'function',
    'function': {
        'name': 'get_recommended_treatment',
        'description': "Extract the numeric age of the patient per row from the 'transcription' column if available. Return null if not found. Then, derive recommended treatment for each patient per column given the transcription details from the transcription column. Match each recommended treatment with the corresponding International Classification of Diseases (ICD) code. Return the ICD-10 code in standard format (e.g., A00.0). Return null if uncertain.", 
        'parameters': {
            'type': 'object',
            'properties': {
                'age': {'type': ['string', 'null'],
                       'description': 'Patient age'},
                'recommended_treatment': {
                    'type': ['string', 'null'],
                    'description': 'Recommended treatment for the patient given the transcription details.'
                },
                'icd_code': {
                    'type': ['string', 'null'],
                    'description': 'Matched International Classification of Diseases (ICD) code with the provided recommended treatment.'
                }
            }        
        }
    }
}]