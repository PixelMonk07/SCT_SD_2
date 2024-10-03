import random

print("Welcome to the number guessing game!")

# Generate a random number between 1 and 100
random_num = random.randint(1, 100)

# Initialize a variable to track whether the user has guessed correctly
guessed_correctly = False

# Loop until the correct number is guessed
while not guessed_correctly:
    try:
        user_input = int(input("Enter a number between 1-100: "))
        
        # Check if the user input is within the valid range
        if user_input < 1 or user_input > 100:
            print("Invalid input! Please enter a number between 1 and 100.")
        else:
            # Compare the user's guess with the random number
            if random_num == user_input:
                print("Congrats! You guessed the correct number!")
                guessed_correctly = True  # Update the flag to exit the loop
            elif random_num > user_input:
                print("Higher number please!")
            else:
                print("Lower number please!")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")
