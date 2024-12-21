from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import joblib

# Initialize FastAPI app
app = FastAPI()

# Load the trained model and encoders
model = joblib.load('rf_model.joblib')
le_origin = joblib.load('le_origin.joblib')
le_destination = joblib.load('le_destination.joblib')
le_vehicle = joblib.load('le_vehicle.joblib')
le_weather = joblib.load('le_weather.joblib')
le_traffic = joblib.load('le_traffic.joblib')

# Define the input schema with alias
class ShipmentDetails(BaseModel):
    Origin: str
    Destination: str
    Vehicle_Type: str
    Distance_km: float = Field(..., alias="Distance (km)")  # Alias for compatibility
    Weather_Conditions: str
    Traffic_Conditions: str

# Preprocessing function with feature order
def preprocess_input(data):
    df = pd.DataFrame([data])
    df['Origin_Encoded'] = le_origin.transform(df['Origin'])
    df['Destination_Encoded'] = le_destination.transform(df['Destination'])
    df['Vehicle_Type_Encoded'] = le_vehicle.transform(df['Vehicle_Type'])
    df['Weather_Encoded'] = le_weather.transform(df['Weather_Conditions'])
    df['Traffic_Encoded'] = le_traffic.transform(df['Traffic_Conditions'])
    df = df.drop(columns=['Origin', 'Destination', 'Vehicle_Type', 'Weather_Conditions', 'Traffic_Conditions'])
    
    # Reorder columns to match training order
    feature_order = ['Origin_Encoded', 'Destination_Encoded', 'Vehicle_Type_Encoded',
                     'Distance (km)', 'Weather_Encoded', 'Traffic_Encoded']
    df = df[feature_order]
    return df

# Define the API endpoint
@app.post('/predict')
def predict(shipment: ShipmentDetails):
    try:
        # Preprocess the input data
        processed_data = preprocess_input(shipment.dict(by_alias=True))  # Use alias for input compatibility

        # Make prediction
        prediction = model.predict(processed_data)

        # Return the prediction as JSON
        return {'prediction': 'Delayed' if prediction[0] == 'Yes' else 'On Time'}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run the FastAPI app
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
