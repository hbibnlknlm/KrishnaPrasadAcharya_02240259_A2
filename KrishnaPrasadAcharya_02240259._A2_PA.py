import random
# Global Score Tracker
scores = {
    "guess_game": 0,
    "rps": 0,
    "trivia": 0
}

# Part A - Games
def guess_number_game():
    print("\n--- Guess the Number Game ---")
    number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < 1 or guess > 100:
                print("Out of range.")
                continue
            attempts += 1
            if guess == number:
                print("Correct!")
                break
            elif guess < number:
                print("Too low.")
            else:
                print("Too high.")
        except ValueError:
            print("Invalid input.")
    score = max(0, 100 - attempts)
    print(f"You scored: {score}")
    scores["guess_game"] += score

def rock_paper_scissors():
    print("\n--- Rock Paper Scissors ---")
    choices = ["rock", "paper", "scissors"]
    user = input("Choose rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid choice.")
        return
    computer = random.choice(choices)
    print(f"Computer chose {computer}")
    if user == computer:
        print("Draw!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
        scores["rps"] += 1
    else:
        print("You lose!")

def trivia_game():
    print("\n--- Trivia Pursuit: Bhutan Quiz ---")
    questions = {
        "Geography": {
            "What is the capital city of Bhutan?": ["Thimphu", "Paro", "Punakha", "Phuentsholing"],
            "Which mountain is the highest in Bhutan?": ["Gangkhar Puensum", "Jomolhari", "Masang Kang", "Black Mountain"]
        },
        "History": {
            "Who was the first King of Bhutan?": ["Ugyen Wangchuck", "Jigme Dorji Wangchuck", "Jigme Singye Wangchuck", "Jigme Khesar Namgyel Wangchuck"],
            "In which year did Bhutan transition to a constitutional monarchy?": ["2008", "1998", "2010", "2003"]
        },
        "Culture": {
            "What is the national sport of Bhutan?": ["Archery", "Wrestling", "Football", "Cricket"],
            "Which festival is widely celebrated in Bhutan with mask dances and rituals?": ["Tshechu", "Losar", "Diwali", "Holi"]
        },
        "Science": {
            "Which gas do plants absorb from the atmosphere during photosynthesis?": ["Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"]
        },
        "Math": {
            "What is the value of π (pi) approximately?": ["3.14", "2.71", "1.61", "1.41"]
        }
    }
    for category, q_set in questions.items():
        print(f"\nCategory: {category}")
        for question, options in q_set.items():
            print(f"{question}")
            for i, opt in enumerate(options, 1):
                print(f"{i}. {opt}")
            try:
                answer = int(input("Your choice (1-4): "))
                if options[answer - 1] == options[0]:
                    print("Correct!")
                    scores["trivia"] += 1
                else:
                    print(f"Wrong! Correct answer is: {options[0]}")
            except (ValueError, IndexError):
                print("Invalid input.")

def overall_score():
    print("\n--- Overall Score ---")
    for game, score in scores.items():
        print(f"{game.capitalize().replace('_', ' ')}: {score}")
    print("")

def main():
    while True:
        print("\n=== Games Menu ===")
        print("1. Guess Number game")
        print("2. Rock Paper Scissors")
        print("3. Trivia Pursuit Game")
        print("4. Check Current Overall Score")
        print("0. Exit games menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            guess_number_game()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            trivia_game()
        elif choice == "4":
            overall_score()
        elif choice == "0":
            print("Exiting games... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
