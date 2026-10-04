# Stage 2 - Requirements prototype
# Implements FR-01: patient record must have ID, name, DOB, phone

class Patient:
    def __init__(self, patient_id, name, dob, phone):
        if not patient_id:
            raise ValueError("Patient ID is required")
        if not name:
            raise ValueError("Name is required")
        if not phone:
            raise ValueError("Phone is required")
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.phone = phone


# Test valid patient
p1 = Patient("P001", "Alice Smith", "1990-05-12", "0400 111 222")
print("Registered:", p1.name)

# Test invalid patient (missing phone)
try:
    p2 = Patient("P002", "Bob Jones", "1985-11-03", "")
except ValueError as e:
    print("Validation caught:", e)
