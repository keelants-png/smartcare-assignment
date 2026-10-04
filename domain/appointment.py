class Appointment:
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
