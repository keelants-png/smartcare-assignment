class ClinicRepository:
    def __init__(self):
        self.patients = []
        self.practitioners = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_practitioner(self, practitioner):
        self.practitioners.append(practitioner)
