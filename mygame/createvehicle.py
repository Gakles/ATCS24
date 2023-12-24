# create_vehicle.py
import json
import os
from gameobjects.supply_truck import Supply_Truck

def create_vehicle(vehicle_type):

    current_directory = os.path.dirname(__file__)  # Get the directory of the current script
    file_path = os.path.join(current_directory, "data", f"{vehicle_type.lower()}_data.json")
    print(file_path)
    with open(file_path, 'r') as file:
        data = json.load(file)

    vehicle_class_name = data.get('class')

    if not vehicle_class_name:
        raise ValueError(f"Class information not found in JSON for vehicle type: {vehicle_type}")

    # Use globals() to dynamically get the class based on its name
    vehicle_class = globals().get(vehicle_class_name)

    if not vehicle_class:
        raise ValueError(f"Unknown vehicle class: {vehicle_class_name}")

    # Combine common attributes with specific attributes

    return vehicle_class(data)

# Add more conditions or classes as needed
