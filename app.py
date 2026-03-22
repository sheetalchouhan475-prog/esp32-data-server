from flask import Flask, request, jsonify
import joblib

# Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")  # ensure model.pkl GitHub repo me uploaded ho

# Home route
@app.route("/")
def home():
    return "AI Agriculture Server Running"

# Predict route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # ESP32 JSON data

    # Extract sensor values
    soil = data["soil"]
    temp = data["temp"]
    humidity = data["humidity"]

    # Prediction (Decision Tree model)
    prediction = model.predict([[soil, temp, humidity]])

    # Convert prediction to readable message
    if prediction[0] == 1:
        result = "Irrigation Needed"
    else:
        result = "No Irrigation Needed"

    return jsonify({"prediction": result})

# Correct way to start Flask server
if __name__== "__main__":
    app.run()
