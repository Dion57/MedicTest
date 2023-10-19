import json
import time

def generate_alerts(patient_data):
    alerts = []

    for patient in patient_data['patients']:
        vitals = patient['vitals']

        # Check for abnormal heart rate
        if vitals['heart_rate'] < 60 or vitals['heart_rate'] > 100:
            alerts.append(f"Alert: Abnormal heart rate for patient {patient['name']} ({patient['id']}): {vitals['heart_rate']} bpm")

        # Check for high blood pressure
        systolic, diastolic = map(int, vitals['blood_pressure'].split('/'))
        if systolic > 140 or diastolic > 90:
            alerts.append(f"Alert: High blood pressure for patient {patient['name']} ({patient['id']}): {vitals['blood_pressure']} mmHg")

        # Check for fever
        if vitals['temperature'] > 100.4:
            alerts.append(f"Alert: Fever for patient {patient['name']} ({patient['id']}): {vitals['temperature']}°F")

    return alerts

while True:
    with open('mock_data.json', 'r') as file:
        mock_data = json.load(file)

    alerts = generate_alerts(mock_data)

    if alerts:
        print("Simulated Alerts:")
        for alert in alerts:
            print(alert)

    # Simulate alerts generation every 10 minutes
    time.sleep(600)
