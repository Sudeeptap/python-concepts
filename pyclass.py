# A class is a blueprint for creating objects that share a structure and behavior.
# Code	Meaning
# class Appointment:	Defines the blueprint.
# __init__	Initializes a new object when it is created.
# self	Refers to the particular object being worked with.
# time and available	Values supplied when creating an appointment.
# self.time = time	Stores the time on that object.
# self.available = available	Stores availability on that object. 
class Appointment:
    def __init__(self, time, available):
        self.time = time
        self.available = available

    def get_status(self):
        if self.available:
            return f"Appointment at {self.time} is available."
        else:
            return f"Appointment at {self.time} is not available."
        
    def mark_as_booked(self):
        self.available = False
        return f"Appointment at {self.time} has been booked."


appointment1 = Appointment("10:00 AM", True)
appointment2 = Appointment("10:30 AM", False)

print(appointment1.get_status())
print(appointment2.get_status())
print(appointment1.mark_as_booked())

