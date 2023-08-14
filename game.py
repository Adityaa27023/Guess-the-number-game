import random

def calculate_score(attempts):
    max_attempts = 3
    max_score = 100
    penalty = 10
    
    if attempts == 1:
        return max_score
    elif attempts > max_attempts:
        return 0
    else:
        return max_score - (penalty * (attempts - 1))

def guess_the_number():
    target_number = random.randint(1, 100)
    attempts = 0
    score = 0
    
    print("Welcome to Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            score = calculate_score(attempts)
            print(f"Congratulations! You've guessed the number {target_number} in {attempts} attempts.")
            print(f"Your score is: {score}")
            break
        
        if attempts == 3:
            print(f"Sorry, you've used all {attempts} attempts. The target number was {target_number}.")
            break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        guess_the_number()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    guess_the_number()
