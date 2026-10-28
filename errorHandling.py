try:
    available_slots="three"
    print(available_slots>0)
except TypeError:
    print("Error: available_slots should be a number.")

try:
    available_slots=int("threee")
    print(available_slots>0)
except ValueError:
    print("Error: pls enter a valid number.")