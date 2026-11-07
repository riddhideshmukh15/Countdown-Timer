
import time

while True:

    try:
        seconds = int(input("Enter seconds: "))

        if seconds <= 0:
            print("Please enter a positive number!")
            continue

    except ValueError:
        print("Invalid input! Enter numbers only.")
        continue

    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

    choice = input("Do you want to start again? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you for using Countdown Timer!")
        break
