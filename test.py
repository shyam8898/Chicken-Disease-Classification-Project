from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.predict import PredictionPipeline

app = Flask(__name__)

@app.route("/")
@cross_origin()
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    if 'image1' not in request.files:
        return "No image part"
    
    image = request.files['image1']
    if image.filename == '':
        return "No selected file"
    
    # Assuming you have a function like 'decodeImage' that handles image processing
    decoded_image = decodeImage(image.read(),image.filename)  # Replace 'decodeImage' with your actual image processing function
    classifier = PredictionPipeline(image.filename)
    result = classifier.predict(decoded_image)  # Call your classifier's predict function
    
    return render_template('index.html', results=result)

if __name__ == "__main__":
    app.run(debug=True)
