import requests


def emotion_detector(text_to_analyse):
    # Define the URL for the Watson NLP Emotion Prediction API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Define the headers required for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Define the input JSON payload containing the text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyse } }
    
    # Send a POST request to the Watson NLP API with the URL, headers, and input JSON
    response = requests.post(url, headers=headers, json=input_json)
    
    # Return the raw text response from the API
    return response.text