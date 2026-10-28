class Appointment:
    def __init__(self, time, availability):
        self.time = time
        self.availability = availability

class OnlineAppointment(Appointment):
    def __init__(self, time, availability, meetingLink):
        super().__init__(time, availability)
        self.meetingLink = meetingLink

    def get_meeting_link(self):
        # Complete this method
        return self.meetingLink

online = OnlineAppointment(
    "11:00 AM",
    True,
    "https://example.com/meeting"
)

print(online.time)
print(online.get_meeting_link())