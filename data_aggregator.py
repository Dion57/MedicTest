import json
import time

# Initialize an empty data aggregation structure
aggregated_data = {"patients": []}

while True:
    # Load and process data from the simulated sources
    with open('mock_data.json', 'r') as file:
        mock_data = json.load(file)
    
    # Aggregating data from simulated sources
    for patient in mock_data['patients']:
        # Check if the patient is already in the aggregated data
        existing_patient = next((p for p in aggregated_data["patients"] if p["id"] == patient["id"]), None)
        if existing_patient:
            # If the patient already exists, update their data
            existing_patient["vitals"].update(patient["vitals"])
            existing_patient["lab_results"].update(patient["lab_results"])
        else:
            # If the patient doesn't exist, add them to the aggregated data
            aggregated_data["patients"].append(patient)

    # Save the aggregated data to a file or send it to the visualization component
    with open('aggregated_data.json', 'w') as file:
        json.dump(aggregated_data, file, indent=2)

    # Simulate data aggregation updates every 5 minutes
    time.sleep(300)
