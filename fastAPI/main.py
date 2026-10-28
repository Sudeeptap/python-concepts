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
