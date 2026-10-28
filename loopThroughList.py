appointment_slots = [
    {"time": "10:00 AM", "available": True},
    {"time": "10:30 AM", "available": False},
    {"time": "11:00 AM", "available": True}
]
for slot in appointment_slots:
    if slot["available"]:
        print(f"Available slot is at {slot['time']}")