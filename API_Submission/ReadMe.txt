****************************** Shipment API and Testing Scripts ******************************

Files

1. shipment_api.py

Purpose: 
- Implements a FastAPI-based backend for predicting shipment outcomes based on input data.
- Leverages a pre-trained Random Forest model and label encoders for preprocessing.

Key Features:

- Endpoints:
  * /predict: Accepts shipment details and returns a prediction (Delayed or On Time).

- Input Validation:
  * Uses Pydantic models for schema validation.

- Model Loading:
  * Loads serialized model (rf_model.joblib) and encoders (joblib files).

- Preprocessing:
  * Transforms categorical inputs into encoded values matching the model's training data.


2. api_implementation.py

Purpose:
- Provides a simple client script to test the shipment prediction API.

Key Features:
- Sends a POST request to the API endpoint (http://127.0.0.1:8000/predict).
- Prints the API's response, which contains the shipment prediction.


Instructions

Running the API:

1. Ensure all required files (rf_model.joblib, encoders) are in the same directory as shipment_api.py.

2. Install dependencies:
   * pip install fastapi uvicorn joblib pandas scikit-learn pydantic

3. Start the API server:
   * python shipment_api.py

4. The API will be available at http://127.0.0.1:8000.


Testing the API:

1. Open a terminal and navigate to the directory containing api_implementation.py.

2. Run the test script:
   * python api_implementation.py

3. Check the terminal output for the prediction result.