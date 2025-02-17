from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://iris-render.onrender.com/"  # Ensure this API URL is correct

@app.route("/", methods=["GET"])
def index():
    

    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.json()
        sepal_length = float(data["sepal_length"])
        sepal_width = float(data["sepal_width"])
        petal_length = float(data["petal_length"])
        petal_width = float(data["petal_width"])

        # Send the request to the deployed API
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            prediction = response.json().get("answer", "Unknown")
            return jsonify({"prediction": prediction})
        else:
            return jsonify({"error": "API request failed"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
