### House Price Prediction Web App
This project is a Flask-based machine learning web application that predicts house prices based on various input features such as area, number of bedrooms, furnishing status, etc. It uses a pre-trained regression model to make the predictions.

## Features:
1. Simple and responsive UI with HTML & CSS.
2. Real-time prediction using a trained ML model (house_price_model.pkl).
3. Clean form with dropdowns for categorical fields.
4. REST API endpoint at /predict that accepts JSON input.

### Dataset Description:
A Comprehensive Dataset for Price Forecasting with 13 key Features.

Link: http://kaggle.com/datasets/harishkumardatalab/housing-price-prediction?resource=download

## Usage:
1. Predict price of a house based on input features.
2. Compare different property configurations.
3. Analyze impact of amenities (AC, basement, etc.).
4. Assist real estate agents in price estimation.
5. Use as a demo project for ML + Flask deployment.

## Technologies Used:
1. **Flask** - Web Framework
2. **HTML + CSS** - Frontend
3. **Pickle** - Model Serialization
4. **scikit-learn** - ML Training & Inference
5. **NumPy + Pandas** - Data Handling

## Project Structure
```bash
houseprice_prediction/
│
├── app.py                  # Main Flask backend
├── house_price_model.pkl   # Trained ML model
├── scaler.pkl              # Pre-fitted Scaler
├── templates/
│   └── index.html          # Frontend HTML Form
├── static/                 # (Optional) CSS or Images
├── snapshots/              # Form and Response Screenshots
├── .gitignore
├── requirements.txt
└── README.md
```

### Setup Instructions

## clone the repo: 
```bash
git clone https://github.com/shrinathasati/Python-Developer-Role-Assignment.git
cd Python-Developer-Assignment
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Run the application
```bash
python app.py
```

## Access application
```bash
http://localhost:5000/
```



