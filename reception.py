import json
import os
from datetime import datetime, timedelta

DATA_DIR = "Text Files"
os.makedirs(DATA_DIR, exist_ok=True)
PATIENT_FILE = os.path.join(DATA_DIR, "patient.txt")
RECEPTIONIST_FILE = os.path.join(DATA_DIR, "receptionist_data.txt")

def data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return {}

def data_save(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)



def add_new_patient():
    patient_info = data(PATIENT_FILE)
    patient_id = input("Patient ID or Passport Number: ")
    name = input("Patient name: ")
    address = input("Address: ")
    birth_date = input("Birth Date (YYYY-MM-DD): ")
    current_age = int(input("Current Age: "))
    phone_number = input("Phone Number: ")
    nationality = input("Nationality: ")
    gender = input("Gender: ")

    patient_info[patient_id] = {
        'name': name,
        'address': address,
        'birth_date': birth_date,
        'current_age': current_age,
        'phone_number': phone_number,
        'nationality': nationality,
        'gender': gender,
        'family_member': [],
        'medical_history': [],
        'medication_history': [],
        'last_visit': str(datetime.now().date())
    }
    data_save(patient_info, PATIENT_FILE)
    print("--- Data stored ---")

def register_family_member(patient_id):
    patient_info = data(PATIENT_FILE)
    if patient_id not in patient_info:
        print("Patient not found.")
        return

    while True:
        family = {
            'name': input("Name: "),
            'birth_date': input("Family Member Birth Date: "),
            'gender': input("Gender: "),
            'age': int(input("Age: "))
        }
        patient_info[patient_id]['family_member'].append(family)
        data_save(patient_info, PATIENT_FILE)
        more = input("Do you want to add another family member? (y/n): ")
        if more.lower() != 'y':
            break

def add_medication_history(patient_id):
    patient_info = data(PATIENT_FILE)
    if patient_id not in patient_info:
        print("Patient not found.")
        return

    diseases = {
        'heart disease': input("Heart Problem (y/n): "),
        'kidney disease': input("Kidney Problem (y/n): "),
        'high blood pressure': input("High Blood Pressure (y/n): "),
        'other disease': input("Any other disease: ")
    }
    patient_info[patient_id]['medication_history'].append(diseases)
    data_save(patient_info, PATIENT_FILE)
    print("Successfully Recorded")

def view_information(patient_id):
    patient_info = data(PATIENT_FILE)
    patient_data = patient_info.get(patient_id)

    if not patient_data:
        print("Patient not found.")
        return

    print(f"Patient Information for {patient_id}:")
    print('\n'.join(f"{key}: {value}" for key, value in patient_data.items()))

def edit_info(patient_id):
    patient_info = data(PATIENT_FILE)

    if patient_id not in patient_info:
        print("Patient not found.")
        return

    print("Edit the Information:")
    for key, value in patient_info[patient_id].items():
        if key not in ['family_member', 'medical_history', 'medication_history']:
            new_value = input(f"{key} ({value}): ")
            if new_value:
                patient_info[patient_id][key] = new_value
    data_save(patient_info, PATIENT_FILE)
    print("Information updated.")

def delete_inactive():
    patient_data = data(PATIENT_FILE)
    cutoff_date = datetime.now() - timedelta(days=365)
    inactive_patients = [pid for pid, pdata in patient_data.items() if datetime.strptime(pdata['last_visit'], '%Y-%m-%d') < cutoff_date]

    for patient_id in inactive_patients:
        del patient_data[patient_id]

    data_save(patient_data, PATIENT_FILE)
    print(f"Deleted {len(inactive_patients)} inactive patients.")


