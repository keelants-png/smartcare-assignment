# Stage 3 - Domain model class skeletons
# Student: Keelan - U3279389


class Patient:
    def __init__(self, patient_id, name, dob, phone):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.phone = phone

    def update_contact(self, phone):
        pass

    def get_appointment_history(self):
        pass


class Practitioner:
    def __init__(self, practitioner_id, name, specialty):
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty

    def update_availability(self, schedule):
        pass

    def get_schedule(self, date):
        pass


class Appointment:
    def __init__(self, appointment_id, patient, practitioner, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date = date
        self.time = time
        self.status = "Booked"

    def cancel(self):
        pass

    def is_duplicate(self, practitioner, date, time):
        pass


# Quick check that the classes load
p = Patient("P001", "Alice Smith", "1990-05-12", "0400 111 222")
d = Practitioner("D001", "Dr. Chen", "General Practice")
a = Appointment("A001", p, d, "2026-05-20", "09:00")
print("Patient:", p.name)
print("Practitioner:", d.name)
print("Appointment:", a.appointment_id, a.date, a.time, a.status)
