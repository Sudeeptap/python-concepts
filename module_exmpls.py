#1. What is a module?
#A module is a Python file containing code that you can reuse in another Python file.

# Imagine your Doctor's Assistant application has several responsibilities:
#- Checking appointment availability
#- Booking appointments
#  - Finding doctors
# You don't need to put all the code in one huge file. You can split it into smaller files and import functions when needed.

from functions import check_availability_2

result2 = check_availability_2(3)
print(result2)
