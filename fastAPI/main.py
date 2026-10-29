from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/abouts")
def greet():
    return {"message": "This is a simple FastAPI application."}

@app.get("/doctors/{doctor_id}")
def get_doctor(doctor_id:int):
    return {"doctor_id": doctor_id, "name": f"Doctor {doctor_id}"}

@app.get("/doctors/{doctore_id}/{date}")
def get_doctor_schedule(doctore_id:int, date:str):
    return {
        "doctor_id": doctore_id,
        "date": date,
    }

@app.get("/appointments")
def get_appointments(doct_id:int, status:str="available"):
    return {
        "doctor_id": doct_id,
        "status": status
    }

appointments = [
    {"id": 1, "doctor_id": 123, "status": "available", "patient_name": "John Doe"},
    {"id": 2, "doctor_id": 123, "status": "booked", "patient_name": "Jane Smith"},
    {"id": 3, "doctor_id": 456, "status": "available", "patient_name": "Bob Johnson"},
]

@app.get("/appointments-search")
def search_appointments(doctor_id: int, status: str | None = None, patient_name: str | None = None):
    results = find_appointments(appointments, doctor_id, status)
    return {"appointments": results}

def find_appointments(appointments, doctor_id, status, patient_name=None):
    results = []

    for appointment in appointments:
        if status is None:
            if appointment["doctor_id"] == doctor_id:
                results.append(appointment)
        else:
            if appointment["doctor_id"] == doctor_id and appointment["status"] == status:
                results.append(appointment)

    return results