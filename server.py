"""
This module defines the Flask application and its routes for running the emotion detector 
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint that receives text input and returns the detected emotion.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    emotions = ", ".join([
        f"'{key}': {value}"
        for key, value in response.items()
        if key != "dominant_emotion"
    ])

    return f"""For the given statement, the system response is {emotions}.
        The dominant emotion is {response["dominant_emotion"]}
    """

@app.route("/")
def render_index_page():
    """
    Render the main index page
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
