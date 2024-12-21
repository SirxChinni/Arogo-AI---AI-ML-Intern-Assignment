import requests

# Define the API endpoint
url = "http://127.0.0.1:8000/predict"

# Define the test data with the alias
test_data = {
    "Origin": "Jaipur",
    "Destination": "Mumbai",
    "Vehicle_Type": "Truck",
    "Distance (km)": 1603.0,  
    "Weather_Conditions": "Rain",
    "Traffic_Conditions": "Light"
}

# Send the POST request
response = requests.post(url, json=test_data)

# Print the response
print(response.json())
