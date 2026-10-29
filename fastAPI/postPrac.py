from fastapi import FastAPI
app = FastAPI()

from pydantic import BaseModel
from datetime import date

class AppointmentRequest(BaseModel):
    patient_name: str
    doctor_id: int
    appointment_date: date

@app.post("/appointments")
def create_appointment(appointment_request: AppointmentRequest):
   return {
        "patient_name": appointment_request.patient_name,
        "doctor_id": appointment_request.doctor_id
    }

appointments = [
    {"id": 1, "doctor_id": 123, "status": "available"},
    {"id": 2, "doctor_id": 123, "status": "booked"},
    {"id": 3, "doctor_id": 456, "status": "available"},
]

@app.get("/appointments-search")
def search_appointments(doctor_id: int, status: str | None = None, patient_name: str | None = None):
    results = find_appointments(appointments, doctor_id, status, patient_name)
    return {"appointments": results}

def find_appointments(appointments, doctor_id, status=None, patient_name=None):
    results = []

    for appointment in appointments:
        if (
            appointment["doctor_id"] == doctor_id
            and (status is None or appointment["status"] == status)
            and (patient_name is None or appointment["patient_name"] == patient_name)
        ):
            results.append(appointment)

    return results