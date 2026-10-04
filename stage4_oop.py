# SmartCare Clinic Appointment Booking System - Stage 4
# OOP Implementation
# Student: Keelan - U3279389


class Patient:
    def __init__(self, patient_id, name, dob, phone):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.phone = phone

    def update_contact(self, phone):
        self.phone = phone


class Practitioner:
    def __init__(self, practitioner_id, name, specialty):
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty


class Appointment:
    VALID_STATUSES = {"Booked", "Cancelled", "Completed"}

    def __init__(self, appointment_id, patient, practitioner, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date = date
        self.time = time
        self.status = "Booked"

    def cancel(self):
        if self.status == "Cancelled":
            return False
        self.status = "Cancelled"
        return True

    def is_duplicate(self, practitioner, date, time):
        return (self.practitioner.practitioner_id == practitioner.practitioner_id
                and self.date == date
                and self.time == time
                and self.status == "Booked")


class ClinicSchedule:
    def __init__(self):
        self.patients = []
        self.practitioners = []
        self.appointments = []
        self.next_id = 1

    def add_patient(self, patient):
        self.patients.append(patient)
        print("Added patient: " + patient.name)

    def add_practitioner(self, practitioner):
        self.practitioners.append(practitioner)
        print("Added practitioner: " + practitioner.name)

    def book_appointment(self, patient, practitioner, date, time):
        for appt in self.appointments:
            if appt.is_duplicate(practitioner, date, time):
                print("ERROR: " + practitioner.name + " already booked at " + date + " " + time)
                return None

        appt = Appointment("A" + str(self.next_id).zfill(3), patient, practitioner, date, time)
        self.next_id += 1
        self.appointments.append(appt)
        print("SUCCESS: Booked " + appt.appointment_id + " for " + patient.name + " with " + practitioner.name)
        return appt

    def cancel_appointment(self, appointment_id):
        for appt in self.appointments:
            if appt.appointment_id == appointment_id:
                appt.cancel()
                print("SUCCESS: Cancelled " + appointment_id)
                return
        print("ERROR: Appointment not found")

    def daily_report(self, date):
        print("")
        print("--- Daily Report for " + date + " ---")
        for appt in self.appointments:
            if appt.date == date:
                print(appt.time + " | " + appt.patient.name + " with " + appt.practitioner.name + " | " + appt.status)
        print("--- End of Report ---")
        print("")


# ==================== DEMO ====================

if __name__ == "__main__":
    print("=== SmartCare Clinic - Stage 4 OOP Implementation ===")
    print("")

    clinic = ClinicSchedule()

    alice = Patient("P001", "Alice Smith", "1990-05-12", "0400 111 222")
    bob = Patient("P002", "Bob Jones", "1985-11-03", "0400 333 444")
    dr_chen = Practitioner("D001", "Dr. Chen", "General Practice")

    clinic.add_patient(alice)
    clinic.add_patient(bob)
    clinic.add_practitioner(dr_chen)

    print("")
    print("--- Booking appointments ---")
    clinic.book_appointment(alice, dr_chen, "2026-05-20", "09:00")
    clinic.book_appointment(bob, dr_chen, "2026-05-20", "09:00")
    clinic.book_appointment(bob, dr_chen, "2026-05-20", "09:30")

    clinic.daily_report("2026-05-20")

    print("--- Cancelling A001 ---")
    clinic.cancel_appointment("A001")

    clinic.daily_report("2026-05-20")

    print("=== End of demo ===")
