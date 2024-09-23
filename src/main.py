import random
import time

print("Welcome to the ⭐Brain Blitz⭐ Game!")
time.sleep(2)
print("You will be presented with a series of questions.\n") 
time.sleep(2)
print("You must answer correctly within 20 seconds to advance to the next question.\n")
print("After 5 incorrect answers, it's GAME OVER😝😝😝\n")
time.sleep(2)
print('gOODLUCK!')

def game_questions_and_answer():
    return [
        # EASY
        ("Who is the richest man in the world?", "Elon Musk"),
        ("What is the capital city of France?", "Paris"),
        # Add more questions as needed
    ]

def quiz_game():
    score = 0  # To keep track of the player's score
    max_attempts = 5  # Maximum allowed wrong answers
    wrong_attempts = 0  # To count the number of wrong attempts

    questions_and_answers = game_questions_and_answer()
    total_questions = len(questions_and_answers)

    for i, (question, correct_answer) in enumerate(questions_and_answers):
        while wrong_attempts < max_attempts:
            print(f"\nQuestion {i + 1}: {question}")
            
            start_time = time.time()  # Record the start time
            user_answer = input("Your answer: ").strip()
            elapsed_time = time.time() - start_time  # Calculate elapsed time

            if elapsed_time > 20:
                print(f"Time's up! You took too long to answer (more than 20 seconds).\n")
                wrong_attempts += 1
            elif user_answer.lower() == correct_answer.lower():
                print("Correct!\n")
                score += 1
                break  # Move to the next question
            else:
                wrong_attempts += 1
                print(f"Wrong! ({wrong_attempts}/{max_attempts} wrong attempts)\n")

            if wrong_attempts >= max_attempts:
                print("Game Over! You've reached the maximum number of wrong attempts.")
                print(f"Your score: {score}")
                return  # Exit the game

    print(f"Congratulations! You completed the quiz. You scored {score} out of {total_questions}.")

if __name__ == "__main__":
    quiz_game()
