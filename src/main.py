import random
import time

class QuizGame:
    def __init__(self):
        self.score = 0  # To keep track of the player's score
        self.max_attempts = 5  # Maximum allowed wrong answers
        self.wrong_attempts = 0  # To count the number of wrong attempts
        self.questions_and_answers = self.game_questions_and_answer()  # Load questions

    def game_questions_and_answer(self):
        """Returns a list of quiz questions and their corresponding answers."""
        return [
            # EASY
            ("Who is the richest man in the world?", "Elon Musk"),
            ("What is the capital city of France?", "Paris"),
            # Add more questions as needed
        ]

    def ask_question(self, question, correct_answer):
        """Asks a question and checks the user's answer."""
        while self.wrong_attempts < self.max_attempts:
            print(f"\nQuestion: {question}")
            start_time = time.time()  # Record the start time
            user_answer = input("Your answer: ").strip()
            elapsed_time = time.time() - start_time  # Calculate elapsed time

            if elapsed_time > 20:
                print(f"Time's up! You took too long to answer (more than 20 seconds).\n")
                self.wrong_attempts += 1
            elif user_answer.lower() == correct_answer.lower():
                print("Correct!\n")
                self.score += 1
                break  # Move to the next question
            else:
                self.wrong_attempts += 1
                print(f"Wrong! ({self.wrong_attempts}/{self.max_attempts} wrong attempts)\n")

            if self.wrong_attempts >= self.max_attempts:
                print("Game Over! You've reached the maximum number of wrong attempts.")
                print(f"Your score: {self.score}")
                return  # Exit the game

    def play(self):
        """Starts the quiz game."""
        print("Welcome to the ⭐Brain Blitz⭐ Game!")
        time.sleep(2)
        print("You will be presented with a series of questions.\n") 
        time.sleep(2)
        print("You must answer correctly within 20 seconds to advance to the next question.\n")
        print("After 5 incorrect answers, it's GAME OVER😝😝😝\n")
        time.sleep(2)
        print('gOODLUCK!')

        for question, correct_answer in self.questions_and_answers:
            self.ask_question(question, correct_answer)

        print(f"Congratulations! You completed the quiz. You scored {self.score} out of {len(self.questions_and_answers)}.")

if __name__ == "__main__":
    game = QuizGame()
    game.play()
