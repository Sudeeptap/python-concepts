#Create a function called get_available_slots 
# that accepts a list of appointment dictionaries
#  and returns only the available appointment times.

def get_available_slots(appointments):
    available_slots=[]
    for appointment in appointments:
        if appointment["available"]:
            available_slots.append(appointment["time"])

    return available_slots
        