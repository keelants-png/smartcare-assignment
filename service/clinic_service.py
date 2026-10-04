from domain.appointment import Appointment


class ClinicService:
    def __init__(self, repository):
        self.repository = repository
        self.appointments = []
        self.next_id = 1

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
