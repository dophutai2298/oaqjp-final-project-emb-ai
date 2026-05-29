"""
Emotion Detection Flask Application
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Render the main index page.
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze user emotion and return formatted response.
    """

    text_to_analyze = request.args.get('textToAnalyze')

    # Handle blank input
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    formatted_response = (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )

    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    