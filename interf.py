import tkinter as tk
from tkinter import messagebox
import requests

def predict():
    # Collect input from the form
    origin = entry_origin.get()
    destination = entry_destination.get()
    vehicle_type = entry_vehicle_type.get()
    distance = entry_distance.get()
    weather_conditions = entry_weather_conditions.get()
    traffic_conditions = entry_traffic_conditions.get()

    # Validate inputs
    if not (origin and destination and vehicle_type and distance and weather_conditions and traffic_conditions):
        messagebox.showerror("Input Error", "All fields are required!")
        return

    # Prepare the API payload
    try:
        distance = float(distance)
    except ValueError:
        messagebox.showerror("Input Error", "Distance must be a number!")
        return

    test_data = {
        "Origin": origin,
        "Destination": destination,
        "Vehicle_Type": vehicle_type,
        "Distance (km)": distance,
        "Weather_Conditions": weather_conditions,
        "Traffic_Conditions": traffic_conditions
    }

    # Send the POST request
    try:
        url = "http://127.0.0.1:8000/predict"
        response = requests.post(url, json=test_data)
        response.raise_for_status()  # Raise an error for HTTP errors
        result = response.json()
        messagebox.showinfo("Prediction Result", f"Prediction: {result['prediction']}")
    except Exception as e:
        messagebox.showerror("API Error", str(e))

# Create the GUI
root = tk.Tk()
root.title("Shipment Prediction")

# Set the window icon (make sure the .ico file is in the same directory or specify the full path)
root.iconbitmap('lorry.ico')  # Path to your .ico file

# Labels and Entry widgets
tk.Label(root, text="Origin:").grid(row=0, column=0, padx=10, pady=5)
entry_origin = tk.Entry(root)
entry_origin.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Destination:").grid(row=1, column=0, padx=10, pady=5)
entry_destination = tk.Entry(root)
entry_destination.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Vehicle Type:").grid(row=2, column=0, padx=10, pady=5)
entry_vehicle_type = tk.Entry(root)
entry_vehicle_type.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Distance (km):").grid(row=3, column=0, padx=10, pady=5)
entry_distance = tk.Entry(root)
entry_distance.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Weather Conditions:").grid(row=4, column=0, padx=10, pady=5)
entry_weather_conditions = tk.Entry(root)
entry_weather_conditions.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Traffic Conditions:").grid(row=5, column=0, padx=10, pady=5)
entry_traffic_conditions = tk.Entry(root)
entry_traffic_conditions.grid(row=5, column=1, padx=10, pady=5)

# Predict Button
btn_predict = tk.Button(root, text="Predict", command=predict)
btn_predict.grid(row=6, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
