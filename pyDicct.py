# .get() vs [] for dictionary key access
appointment = {"time": "10:00 AM"}
#print(appointment.get("available"))  # returns "Not available" if key doesn't exist

# Requirements:
# 1. Create a function named parse_duration.
# 2. Accept duration_text as a parameter.
# 3. Use try and except ValueError.
# 4. If conversion succeeds, return the integer.
# 5. If conversion fails, return "Invalid duration".


def parse_duration(duration_text):
    try:
        duration = int(duration_text)
        return duration
    except ValueError:
        return "Invalid duration"


result=parse_duration("4min ")
print(result)  # Output: Invalid duration