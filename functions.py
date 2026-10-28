def check_availability_2(available_slots):
    if(available_slots > 0):
       return f"Available slots: {available_slots}"
    else:
        return "No available slots."

# return only available appointments

appointments = [
    {"time": "10:00 AM", "available": True},
    {"time": "10:30 AM", "available": False},
    {"time": "11:00 AM", "available": True}
]

def get_available_appointments(appointments):
    available_appts=[]
    for appointment in appointments:
        if appointment["available"]:
            available_appts.append(appointment["time"])
    return available_appts

if __name__ == "__main__":
    available_appointments = get_available_appointments(appointments)
    print(available_appointments)