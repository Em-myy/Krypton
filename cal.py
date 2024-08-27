
from time import process_time
question = input("Enter a password: ")
password = int(question)
bruteForce_pass = 0
while bruteForce_pass != password:
    bruteForce_pass += 1
print("The password is: ", bruteForce_pass)
print("Process time: ", process_time())
