class Patient:
    def __init__(self, patient_id, name, dob, phone):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.phone = phone

    def update_contact(self, phone):
        self.phone = phone
