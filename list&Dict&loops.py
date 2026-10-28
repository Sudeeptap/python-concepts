
appointments = [
    {
        "patient": "Rajesh",
        "time": "10:00 AM",
        "available": True
    },
    {
        "patient": "Priya",
        "time": "10:30 AM",
        "available": False
    },
    {
        "patient": "Anil",
        "time": "11:00 AM",
        "available": True
    }
]

for appointment in appointments:
    if appointment["available"]:   
        print(f"Available appointment for {appointment['patient']} is at {appointment['time']}")
