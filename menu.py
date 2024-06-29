import json
import os
from datetime import datetime, timedelta

DATA_DIR = "Text Files"
os.makedirs(DATA_DIR, exist_ok=True)
PATIENT_FILE = os.path.join(DATA_DIR, "patient.txt")
RECEPTIONIST_FILE = os.path.join(DATA_DIR, "receptionist_data.txt")
DOCTOR_FILE = os.path.join(DATA_DIR, "doctor_data.txt")

def data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return {}

def data_save(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)

def receptionist_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    receptionist_data = data(RECEPTIONIST_FILE)
    if username in receptionist_data and receptionist_data[username]['password'] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

def doctor_login():
    username = input("Username: ")
    password = input("Password: ")
    doctor_info = data(DOCTOR_FILE)
    if username in doctor_info and doctor_info[username]['password'] == password:
        print("Logged in as Doctor")
        return True
    else:
        print("Invalid")
        return False

def reception_menu():
    while True:
        print("*** Welcome to the Receptionist Menu ***")
        print("1. Register New Patient")
        print("2. Edit Patient Information")
        print("3. Register Family Members")
        print("4. Add Medication History")
        print("5. View Patient Information")
        print("6. Delete Inactive Patient")
        print("7. Logout")
        choice = input("Enter your Number: ")

        if choice == "1":
            from reception import add_new_patient
            add_new_patient()
        elif choice == "2":
            from reception import edit_info
            patient_id = input("Enter patient ID/passport number: ")
            edit_info(patient_id)
        elif choice == "3":
            from reception import register_family_member
            patient_id = input("Patient ID: ")
            register_family_member(patient_id)
        elif choice == "4":
            from reception import add_medication_history
            patient_id = input("Enter patient ID/passport number: ")
            add_medication_history(patient_id)
        elif choice == "5":
            from reception import view_information
            patient_id = input("Enter patient ID/passport number: ")
            view_information(patient_id)
        elif choice == "6":
            from reception import delete_inactive
            delete_inactive()
        elif choice == "7":
            print("Exiting from the Receptionist Menu")
            break
        else:
            print("Invalid choice!")

def doctor_menu():
    while True:
        print("\nDoctor Menu:")
        print("1. View Patient by ID")
        print("2. Add Medical Result")
        print("3. Add Medical Certification")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            from doctor import view_patient_id
            view_patient_id()
        elif choice == "2":
            from doctor import medical_result
            medical_result()
        elif choice == "3":
            from doctor import medic_history
            medic_history()
        elif choice == "4":
            print("Exiting from the Doctor Menu")
            break
        else:
            print("Invalid choice!")
