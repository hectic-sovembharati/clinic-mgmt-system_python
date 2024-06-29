import json
import os
from datetime import datetime
from reception import *

DATA_DIR = "Text Files"
os.makedirs(DATA_DIR, exist_ok=True)
DOCTOR_FILE = os.path.join(DATA_DIR, "doctor_data.txt")
PATIENT_FILE = os.path.join(DATA_DIR, "patient.txt")

def data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return {}

def data_save(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)


def view_patient_id():
    patient_id = input("Patient ID / Passport Number: ")
    view_information(patient_id)

def medical_result():
    patient_id = input("Patient ID / Passport Number: ")
    patient_info = data(PATIENT_FILE)
    if patient_id not in patient_info:
        print("Sorry Not Found Try Again")
        return

    result = {
        'date': str(datetime.now().date()),
        'blood_pressure': input("Blood pressure: "),
        'sickness': input("Sickness: "),
        'drug_prescription': input("Drug prescription: "),
        'temperature': input("Temperature: "),
        'additional_information': input("Additional information: ")
    }
    patient_info[patient_id]['medical_history'].append(result)
    patient_info[patient_id]['last_visit'] = str(datetime.now().date())
    data_save(patient_info, PATIENT_FILE)
    print("Medical result added successfully.")

def medic_history():
    patient_id = input("Patient ID/Passport Number: ")
    patient_info = data(PATIENT_FILE)
    if patient_id not in patient_info:
        print("Not Found the result")
        return

    certificate = {
        'date': str(datetime.now().date()),
        'details': input("Details: ")
    }
    patient_info[patient_id].setdefault('medical_certificate', []).append(certificate)
    data_save(patient_info, PATIENT_FILE)
    print("Added!!!!!!")


