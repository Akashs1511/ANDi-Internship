import pandas as pd
from datetime import datetime
import os

# Initialize data files if they don't exist
def initialize_files():
    if not os.path.exists("appointments.csv"):
        pd.DataFrame(columns=["patient_name", "date", "time", "doctor"]).to_csv("appointments.csv", index=False)
    if not os.path.exists("prescriptions.csv"):
        pd.DataFrame(columns=["patient_name", "drug", "dosage", "date"]).to_csv("prescriptions.csv", index=False)
    if not os.path.exists("drugs.csv"):
        # Sample drugs by type
        drugs = [
            {"type": "Painkiller", "name": "Ibuprofen", "dosage": "200mg"},
            {"type": "Painkiller", "name": "Paracetamol", "dosage": "500mg"},
            {"type": "Antibiotic", "name": "Amoxicillin", "dosage": "250mg"},
        ]
        pd.DataFrame(drugs).to_csv("drugs.csv", index=False)
    if not os.path.exists("treatments.csv"):
        # Sample pre-filled treatments
        treatments = [
            {"name": "Fever", "drug": "Paracetamol", "dosage": "500mg, 3 times daily"},
            {"name": "Infection", "drug": "Amoxicillin", "dosage": "250mg, twice daily"},
        ]
        pd.DataFrame(treatments).to_csv("treatments.csv", index=False)

# Drug Manager Class
class DrugManager:
    def __init__(self):
        self.drugs = pd.read_csv("drugs.csv")

    def get_drugs_by_type(self, drug_type):
        return self.drugs[self.drugs["type"] == drug_type]

    def list_types(self):
        return self.drugs["type"].unique()

# Doctor Class
class Doctor:
    def __init__(self, name):
        self.name = name

    def book_appointment(self, patient_name, date, time):
        appointments = pd.read_csv("appointments.csv")
        new_appointment = pd.DataFrame({
            "patient_name": [patient_name],
            "date": [date],
            "time": [time],
            "doctor": [self.name]
        })
        appointments = pd.concat([appointments, new_appointment], ignore_index=True)
        appointments.to_csv("appointments.csv", index=False)
        print(f"Appointment booked for {patient_name} on {date} at {time}")

    def write_prescription(self, patient_name):
        drug_manager = DrugManager()
        print("\nAvailable Drug Types:", drug_manager.list_types())
        drug_type = input("Select drug type (e.g., Painkiller): ")
        drugs = drug_manager.get_drugs_by_type(drug_type)
        print("Available Drugs:\n", drugs)

        drug_name = input("Enter drug name: ")
        dosage = input("Enter dosage (or press Enter to use default): ")
        if not dosage:
            dosage = drugs[drugs["name"] == drug_name]["dosage"].iloc[0]

        prescriptions = pd.read_csv("prescriptions.csv")
        new_prescription = pd.DataFrame({
            "patient_name": [patient_name],
            "drug": [drug_name],
            "dosage": [dosage],
            "date": [datetime.now().strftime("%Y-%m-%d")]
        })
        prescriptions = pd.concat([prescriptions, new_prescription], ignore_index=True)
        prescriptions.to_csv("prescriptions.csv", index=False)
        print(f"Prescription written for {patient_name}: {drug_name}, {dosage}")

    def use_treatment_template(self, patient_name):
        treatments = pd.read_csv("treatments.csv")
        print("Available Treatments:\n", treatments)
        treatment_name = input("Select treatment name (e.g., Fever): ")
        treatment = treatments[treatments["name"] == treatment_name]
        if treatment.empty:
            print("Treatment not found!")
            return

        drug = treatment["drug"].iloc[0]
        dosage = treatment["dosage"].iloc[0]
        prescriptions = pd.read_csv("prescriptions.csv")
        new_prescription = pd.DataFrame({
            "patient_name": [patient_name],
            "drug": [drug],
            "dosage": [dosage],
            "date": [datetime.now().strftime("%Y-%m-%d")]
        })
        prescriptions = pd.concat([prescriptions, new_prescription], ignore_index=True)
        prescriptions.to_csv("prescriptions.csv", index=False)
        print(f"Applied treatment {treatment_name} for {patient_name}: {drug}, {dosage}")

    def generate_invoice(self, patient_name):
        # Simplified invoice
        appointments = pd.read_csv("appointments.csv")
        patient_appointments = appointments[appointments["patient_name"] == patient_name]
        print(f"\nInvoice for {patient_name}:")
        print(f"Appointments:\n{patient_appointments}")
        print("Total Cost: $50 (flat rate for demo)")

# Patient Class
class Patient:
    def __init__(self, name):
        self.name = name

    def view_history(self):
        appointments = pd.read_csv("appointments.csv")
        prescriptions = pd.read_csv("prescriptions.csv")
        patient_appointments = appointments[appointments["patient_name"] == self.name]
        patient_prescriptions = prescriptions[prescriptions["patient_name"] == self.name]
        print(f"\nAppointments for {self.name}:\n", patient_appointments)
        print(f"\nPrescriptions for {self.name}:\n", patient_prescriptions)

# Main System
def main():
    initialize_files()
    doctor = Doctor("Dr. Smith")

    while True:
        print("\nDoctor Appointment Booking System")
        print("1. Book Appointment")
        print("2. Write Prescription")
        print("3. Use Treatment Template")
        print("4. Generate Invoice")
        print("5. Patient History")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            patient_name = input("Enter patient name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            doctor.book_appointment(patient_name, date, time)

        elif choice == "2":
            patient_name = input("Enter patient name: ")
            doctor.write_prescription(patient_name)

        elif choice == "3":
            patient_name = input("Enter patient name: ")
            doctor.use_treatment_template(patient_name)

        elif choice == "4":
            patient_name = input("Enter patient name: ")
            doctor.generate_invoice(patient_name)

        elif choice == "5":
            patient_name = input("Enter patient name: ")
            patient = Patient(patient_name)
            patient.view_history()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()