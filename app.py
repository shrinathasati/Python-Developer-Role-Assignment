from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('house_price_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))  # Make sure you have this scaler.pkl saved

# Helper to map yes/no to 1/0
def map_yes_no(value):
    return 1 if value.lower() == 'yes' else 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    try:
        # Extract features from input JSON
        area = float(data['area'])
        bedrooms = int(data['bedrooms'])
        bathrooms = int(data['bathrooms'])
        stories = int(data['stories'])
        mainroad = map_yes_no(data['mainroad'])
        guestroom = map_yes_no(data['guestroom'])
        basement = map_yes_no(data['basement'])
        hotwaterheating = map_yes_no(data['hotwaterheating'])
        airconditioning = map_yes_no(data['airconditioning'])
        parking = int(data['parking'])
        prefarea = map_yes_no(data['prefarea'])
        furnishingstatus = data['furnishingstatus'].lower()

        # Furnishing status one-hot encoding (baseline: furnished)
        furnishing_semi = 1 if furnishingstatus == 'semi-furnished' else 0
        furnishing_unfurnished = 1 if furnishingstatus == 'unfurnished' else 0

        # Create input array
        input_features = np.array([[ 
            area,
            bedrooms,
            bathrooms,
            stories,
            mainroad,
            guestroom,
            basement,
            hotwaterheating,
            airconditioning,
            parking,
            prefarea,
            furnishing_semi,
            furnishing_unfurnished
        ]])

        # Scale input features
        input_scaled = scaler.transform(input_features)

        # Predict price
        prediction = model.predict(input_scaled)

        return jsonify({'predicted_price': round(float(prediction[0]), 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
