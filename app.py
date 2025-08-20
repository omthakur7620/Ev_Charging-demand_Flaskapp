from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("ev_demand_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>🚗 Welcome to the EV Demand Prediction API!</h2><p>Visit <b>/predict</b> to test.</p>"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return "I will make the predictions. Send a POST request with JSON data to get results."

    else:  # POST request
        data = request.json
        # Example input:
        # {"City_Population":500000,"Number_of_EVs":12000,"Avg_Income":40000,"Gas_Price":105,"Charging_Stations_Available":15,"Green_Policy":1,"Urbanization_Rate":70}
        
        features = np.array([[data["City_Population"], data["Number_of_EVs"], data["Avg_Income"], 
                              data["Gas_Price"], data["Charging_Stations_Available"], 
                              data["Green_Policy"], data["Urbanization_Rate"]]])
        
        # Scale features
        features_scaled = scaler.transform(features)

        # Predict
        prediction = model.predict(features_scaled)[0]
        
        return jsonify({"Demand_Level": "High" if prediction==1 else "Low"})

if __name__ == "__main__":
    app.run(debug=True)
