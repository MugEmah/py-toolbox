# VICTORIA UNIVERSITY HEALTH CENTRE
# CLINIC PATIENT RECORD SYSTEM

# Patient records
patients = [
    ("PAT-0001", "Nabirye Hilary", 21, "A+", "0701234567"),
    ("PAT-0002", "Muge Emm", 27, "B+", "0701298754"),
    ("PAT-0003", "Ogwal Aaron", 28, "A+", "0701297632"),
    ("PAT-0004", "Kaliisa Doreen", 20, "O-", "079539751"),
    ("PAT-0005", "Ntambi Michael", 26, "A-", "075648213")
]

# Welcome banner
def display_banner():
    print("=" * 60)
    print(" VICTORIA UNIVERSITY HEALTH CENTRE")
    print(" Clinic Patient Record System v1.0")
    print("=" * 60)

# Main Menu
def display_menu():
    print("\nMAIN MENU")
    print("1. Add New Patient")
    print("2. Search Patient by Name")
    print("3. Update Patient Phone Number")
    print("4. Display All Patients")
    print("5. Display Statistics Report")
    print("6. Exit")

# Exception Class
class PatientValidationError(Exception):
    """Custome exception for invalid patient data."""
    pass

# New patient function
def add_patient():

    try:
        # auto patient ID generation
        patient_id = f"PAT-{len(patients) + 1:04d}"

        print("\n=== ADD NEW PATIENT ===")

        # Input patient details
        full_name = input("Enter full name: ").strip().title()

        age = int(input("Enter age: "))

        blood_type = input("Enter blood type: ").strip().upper()

        phone_number = input("Enter phone number: ").strip()

        # Validation
        if age < 1 or age > 120:
            raise PatientValidationError(
                "Age must be btn 1 and 120"
            )
        
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise PatientValidationError(
                "Phone number must contain exactly 10 digits."
            )
        
        # Patient record(tuple)
        patient_record = (
            patient_id,
            full_name,
            age,
            blood_type,
            phone_number
        )

        # Add to patient list list
        patients.append(patient_record)

        print(f"\nPatient added successfully with ID: {patient_id}")

    except ValueError:
        print("Error: Age must be a valid number.")

    except PatientValidationError as error:
        print(f"Validation Error: {error}")

# Patient name search
def search_patient():

    try:
        print("\n=== SEARCH PATIENT ===")

        search_name = input("Enter patient name to search: ").strip().lower()

        found = False

        # search thru patient records
        for patient in patients:

            patient_id, full_name, age, blood_type, phone_number = patient

            # Case insensitive search
            if search_name in full_name.lower():
                print("\nPatient Found")
                print("-" * 50)

                print(f"Patient ID  : {patient_id}")
                print(f"Full Name   : {full_name}")
                print(f"Age         : {age}")
                print(f"Blood Type  : {blood_type}")
                print(f"Phone Number: {phone_number}")

                found = True

        #If no match found
        if not found:
            print("No matching patient record found.")

    except Exception as error:
        print(f"Error: {error}")

# Updating Patients Phone Number
def  update_phone_number():

    try:
        print("\n=== UPDATE PATIENT PHONE NUMBER ===")

        patient_id = input("Enter Patient ID: ").strip().upper()

        found = False

        # Loop thru patient records
        for index, patient in enumerate(patients):

            current_id, full_name, age, blood_type, phone_number = patient

            # Check if the ID Matches
            if current_id == patient_id:
                print(f"Current Phone Number: {phone_number}")

                new_phone = input("Enter new phone number: ").strip()

                # Validate phone number
                if not new_phone.isdigit() or len(new_phone) != 10:
                    raise PatientValidationError(
                        "Phone number contain exactly 10 digits"
                    )
                
                # Update tuple
                updated_record = (current_id, full_name, age, blood_type, new_phone)

                # Replace old record
                patients[index] = updated_record

                print("\nPhone number update successfully.")

                found = True
                break

        # If patient ID is not found
        if not found:
            print("Patient ID not found.")

    except PatientValidationError as error:
        print(f"Validation Error: {error}")

    except Exception as error:
        print(f"Error: {error}")

# Display All Patients
def display_all_patients():

    try:
        print("\n=== ALL PATIENT RECORDS ===")

        # Check for empty patient list
        if not patients:
            print("No patient records found.")
            return
        
        # Table header
        print("-" * 85)

        print(
            f"{'Patient ID':<12}"
            f"{'Full Name':<25}"
            f"{'Age':<8}"
            f"{'Blood Type':<15}"
            f"{'Phone Number':<15}"
        )

        print("-" * 85)

        #Patient records
        for patient in patients:

            patient_id, full_name, age, blood_type, phone_number = patient

            print(
                f"{patient_id:<12}"
                f"{full_name:<25}"
                f"{age:<8}"
                f"{blood_type:<15}"
                f"{phone_number:<15}"
            )

        print("-" * 85)

    except Exception as error:
        print(f"Error: {error}")

# Calculate total patients
def get_total_patients():
    return len(patients)

# Calculate average age
def get_average_age():
    total_age = sum(patient[2] for patient in patients)
    return total_age / len(patients)

# Get youngest patient
def get_youngest_patient():
    return min(patients, key=lambda patient: patient[2])

# Get oldest patient
def get_oldest_patient():
    return max(patients, key=lambda patient: patient[2])

# Display statistics report
def display_statistics():

    try:
        print("\n=== PATIENT STATISTICS REPORT ===")

        # check if list is empty
        if not patients:
            print("No patient records found.")
            return
        
        # Get statistics
        total_patients = get_total_patients()
        average_age = get_average_age()
        youngest_patient = get_youngest_patient()
        oldest_patient = get_oldest_patient()

        # Display report
        print(f"Total Patients : {total_patients}")
        print(f"Average Age    : {average_age:.1f}")

        print(
            f"Youngest Patient : "
            f"{youngest_patient[1]} ({youngest_patient[2]} years)"
        )

        print(
            f"Oldest Patient   : "
            f"{oldest_patient[1]} ({oldest_patient[2]} years)"
        )

    except Exception as error:
        print(f"Error: {error}")


# Main Program
if __name__ == "__main__":
    display_banner()

    while True:
        display_menu()

        choice = input("\nEnter your choice from the menu: ").strip()

        if choice == "1":
            add_patient()

        elif choice == "2":
            search_patient()

        elif choice == "3":
            update_phone_number()

        elif choice == "4":
            display_all_patients()

        elif choice == "5":
            display_statistics()

        elif choice == "6":
            print("Exiting system...")
            break

        else:
            print("Invalid menu option")