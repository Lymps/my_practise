import random

secret_number = random.randint(1, 30)

print("Hello :)\nplease guess the number in range from 1 to 30 ")
print("You have 5 chances")

for guessing_times in range(1, 6):
    try:
        print("Please write your chosen number: ")
        answer = int(input())
        if answer < secret_number:
            print("Your number is too low")
        elif answer > secret_number:
            print("Your number is too high")
        else:
            break
    except ValueError:
        print("Please write only numbers")
if answer == secret_number:
    print(f"Great you have guessed secret number after {guessing_times} times")
else:
    print(f"Sorry, you had lost, correct number was {secret_number}")
