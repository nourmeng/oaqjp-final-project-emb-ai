"""
server.py

This module defines a Flask web application that provides an emotion detection service.
It exposes two routes: the home page and an emotion detector endpoint.
"""

# Import necessary modules from Flask
from flask import Flask, request, render_template

# Import the emotion_detector function from the EmotionDetection module
from EmotionDetection.emotion_detection import emotion_detector

# Create a Flask application instance
app = Flask(__name__)

@app.route("/")
def home():
    """
    Render the home page.

    Returns:
        str: The rendered HTML template for the home page.
    """
    return render_template("index.html")


# Define a route for the emotion detector endpoint
@app.route("/emotionDetector")
def emotion_detection():
    """
    Analyze the emotion of the provided text.

    Returns:
        str: A formatted string with emotion scores and the dominant emotion,
             or an error message if the input text is invalid.
    """
    # Get the text to analyze from the query parameters
    text_to_analyse = request.args.get("textToAnalyze")

    # Call the emotion_detector function with the text to analyze
    result = emotion_detector(text_to_analyse)

    # Check if the dominant emotion is None (indicating an error)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract emotion scores and the dominant emotion from the result
    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    # Construct a formatted string with the emotion scores and the dominant emotion
    formatted_text = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    # Return the formatted string as the response
    return formatted_text

# Run the Flask application if this script is executed directly
if __name__ == "__main__":
    # Start the Flask development server
    app.run(host="127.0.0.1", port=5000, debug=True)
    