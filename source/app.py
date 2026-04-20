from flask import Flask, request, jsonify
import joblib
import requests

from flask import render_template
from utils import preprocess

app = Flask(__name__)

svm_model = joblib.load("models/svm_model.pkl")
nb_model = joblib.load("models/nb_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_with(model, text):
    #print(f"DEBUG: Processing text: {text}")
    clean = preprocess(text)
    #print("DEBUG: Preprocessing done")
    
    vec = vectorizer.transform([clean])
    #print("DEBUG: Vectorization done")
    
    pred = model.predict(vec)[0]
    #print(f"DEBUG: Prediction: {pred}")

    # confidence
    if hasattr(model, "decision_function"):
        conf = float(model.decision_function(vec).max())
    elif hasattr(model, "predict_proba"):
        conf = float(model.predict_proba(vec)[0].max())
    else:
        conf = None

    return {
        "prediction": pred,
        "confidence": conf
    }


@app.route("/predict", methods=["POST"])
def predict():
    # print("Request Received!")
    data = request.get_json(silent=True)
    # print(f"Data received: {data}")
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    text = data.get("text", "").strip()
    model_choice = data.get("model", "svm")

    if not text:
        return jsonify({"error": "Text is required"}), 400

    if model_choice == "svm":
        result = {"svm": predict_with(svm_model, text)}

    elif model_choice == "nb":
        result = {"nb": predict_with(nb_model, text)}

    elif model_choice == "both":
        result = {
            "svm": predict_with(svm_model, text),
            "nb": predict_with(nb_model, text)
        }

    else:
        return jsonify({"error": "Invalid model choice"}), 400

    return jsonify({
    "input": text,
    "result": result
    })

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
