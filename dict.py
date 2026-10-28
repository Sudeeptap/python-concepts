appointment = {"patient_name": "Rajesh", "appointment_time": "10:30 AM", "is_available": True}
print(appointment["patient_name"])
print(appointment["appointment_time"])
print(appointment["is_available"])
appointment["doctor_name"] = "Dr. Smith"

appointment["is_available"] = False
print(f"updated appointment is {appointment}")
