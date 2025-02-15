from flask import Flask, render_template, request
import requests
import numpy
import joblib
from io import BytesIO

app = Flask(__name__)
  # Ensure model is available
model_path='model.pkl'
model=joblib.load(model_path)
# Load the model
# iris_model = joblib.load(MODEL_PATH)
MODEL_URL = "https://huggingface.co/krishnash16/Iris/resolve/main/model.pkl"
MODEL_PATH = "model.pkl"

def load_model():
    model_url = MODEL_URL
    try:
        response = requests.get(model_url)
        response.raise_for_status()
        return joblib.load(BytesIO(response.content))
    except Exception as e:
        print(f"Error loading")
        return None
model =load_model()
    
@app.route('/', methods=['GET', 'POST'])
def iris():
    if request.method == 'POST':
        try:
            sepal_length = float(request.form['sepal_length'])
            sepal_width = float(request.form['sepal_width'])
            petal_length = float(request.form['petal_length'])
            petal_width = float(request.form['petal_width'])
            ans = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

            ans_name = ["Setosa", "Versicolor", "Virginica"][ans[0]]
            return render_template("index.html", prediction=ans_name)
        except Exception as e:
            return render_template("index.html", prediction=f"Error: {str(e)}")
    return render_template("index.html", prediction=None)


