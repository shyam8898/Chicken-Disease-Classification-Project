from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage, encodeImageIntoBase64
from cnnClassifier.pipeline.predict import PredictionPipeline
import base64

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"



@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.files['image1']
    image_bytes = image.read()
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    decodeImage(image_base64, clApp.filename)
    result = clApp.classifier.predict()
    predictions = f"Chicken Type: {result[0]['image']}"
    return render_template('index.html', results=predictions)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080, debug=True) #local host
    # app.run(host='0.0.0.0', port=8080) #for AWS
    # app.run(host='0.0.0.0', port=80) #for AZURE

