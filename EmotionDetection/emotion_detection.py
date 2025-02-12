import requests
import json


def emotion_detector(text_to_analyse):
    # Define the URL for the Watson NLP Emotion Prediction API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Define the headers required for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Define the input JSON payload containing the text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyse } }
    
    # Send a POST request to the Watson NLP API with the URL, headers, and input JSON
    response = requests.post(url, headers=headers, json=input_json)

    # Return all values as None if status_code = 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Parse the JSON response
    response_json = json.loads(response.text)
    
    # Extract emotion scores
    emotions = response_json["emotionPredictions"][0]["emotion"]
    
    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Format the output
    formatted_output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

    return formatted_output