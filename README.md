# SmartCare Clinic Appointment Booking System

**Student:** Keelan
**Student ID:** U3279389
**Unit:** 4483-8995 Software Technology

## Overview

A simple clinic appointment booking system for SmartCare Community Clinic,
built iteratively across Stages 1-5. The system replaces fragmented
spreadsheet and paper processes with a layered Python application.

## Architecture (Stage 5)

- Presentation layer: `main.py`
- Service layer: `service/clinic_service.py`
- Domain layer: `domain/patient.py`, `domain/practitioner.py`, `domain/appointment.py`
- Repository layer: `repository/clinic_repository.py`

## How to Run

python3 main.py

## Features Implemented

- FR-01: Patient registration
- FR-04: Practitioner registration
- FR-06: Book appointment
- FR-07: Prevent duplicate bookings
- FR-08: Cancel appointment
- FR-09: View practitioner schedule
- FR-10: View patient appointment history
- FR-11: Appointment status tracking (Booked / Cancelled)
- FR-12: Daily appointment report

## AI Use Declaration

AI (ChatGPT) was used to assist with brainstorming, requirements review,
CRC/UML review, pair-programming suggestions, and SOLID/architecture
review. All suggestions were evaluated using the Ask-Check-Explain
framework, and decisions (Accept / Modify / Reject / Keep unverified) are
documented in each stage's AI review record.
