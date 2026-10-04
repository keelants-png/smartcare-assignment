# SmartCare v0.5 - Layered Architecture
# Student: Keelan - U3279389

from domain.patient import Patient
from domain.practitioner import Practitioner
from repository.clinic_repository import ClinicRepository
from service.clinic_service import ClinicService


def main():
    print("=== SmartCare Clinic v0.5 (Layered Architecture) ===")
    print("")

    repo = ClinicRepository()
    service = ClinicService(repo)

    alice = Patient("P001", "Alice Smith", "1990-05-12", "0400 111 222")
    bob = Patient("P002", "Bob Jones", "1985-11-03", "0400 333 444")
    dr_chen = Practitioner("D001", "Dr. Chen", "General Practice")

    repo.add_patient(alice)
    repo.add_patient(bob)
    repo.add_practitioner(dr_chen)

    print("Registered: " + alice.name + ", " + bob.name + ", " + dr_chen.name)
    print("")

    print("--- Booking appointments ---")
    service.book_appointment(alice, dr_chen, "2026-05-20", "09:00")
    service.book_appointment(bob, dr_chen, "2026-05-20", "09:00")
    service.book_appointment(bob, dr_chen, "2026-05-20", "09:30")

    service.daily_report("2026-05-20")

    print("--- Cancelling A001 ---")
    service.cancel_appointment("A001")

    service.daily_report("2026-05-20")

    print("=== End of demo ===")


if __name__ == "__main__":
    main()
