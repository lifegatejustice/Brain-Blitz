import random

def game_questions_and_answer():
    # List of questions with questions and answers
    return [
        # EASY
        ("Who is the richest man in the world?", "Elon Musk"),
        ("What is the capital city of France?", "Paris"),
        ("Which country won the FIFA World Cup in 2018?", "France"),
        ("What is 5 + 7?", "12"),
        ("Who is the all-time top scorer in the UEFA Champions League?", "Cristiano Ronaldo"),
        # BASIC
        ("What is the largest planet in our solar system?", "Jupiter"),
        ("Who won the Ballon d'Or in 2021?", "Lionel Messi"),
        ("What is the square root of 144?", "12"),
        ("In which year did the Titanic sink?", "1912"),
        ("Which football club has won the most Premier League titles?", "Manchester United"),
        # INTERMEDIATE
        ("What is the chemical symbol for gold?", "Au"),
        ("Who won the FIFA Women's World Cup in 2019?", "USA"),
        ("What is the smallest prime number?", "2"),
        ("What is the capital of Canada?", "Ottawa"),
        ("Which country won the first-ever FIFA World Cup in 1930?", "Uruguay"),
        # ADVANCED
        ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
        ("Which footballer has the most international goals for his country?", "Cristiano Ronaldo"),
        ("What is the value of Pi to three decimal places?", "3.142"),
        ("Which element has the atomic number 1?", "Hydrogen"),
        ("Which football club won the UEFA Champions League in 2022?", "Real Madrid"),
        # CHALLENGING
        ("Who was the first person to walk on the moon?", "Neil Armstrong"),
        ("Which country has won the most FIFA World Cup titles?", "Brazil"),
        ("What is the chemical formula for water?", "H2O"),
        ("Which planet is closest to the Sun?", "Mercury"),
        ("Who won the Golden Boot in the 2018 FIFA World Cup?", "Harry Kane"),
        # HARD
        ("What is the capital city of Australia?", "Canberra"),
        ("Which footballer scored a hat-trick in the 2014 FIFA World Cup Final?", "No one (It was Mario Götze who scored the winning goal, but not a hat-trick)"),
        ("What is the longest river in the world?", "Nile"),
        ("Who discovered penicillin?", "Alexander Fleming"),
        ("Which footballer has won the most Ballon d'Or awards?", "Lionel Messi"),
        # VERY HARD
        ("What is the capital of Iceland?", "Reykjavik"),
        ("Which football team did Zinedine Zidane manage to three consecutive Champions League titles?", "Real Madrid"),
        ("What is the largest desert in the world?", "Sahara Desert"),
        ("Which element has the highest atomic number?", "Oganesson (Og, atomic number 118)"),
        ("Who scored the fastest goal in FIFA World Cup history?", "Hakan Şükür"),
        # DIFFICULT
        ("Which country was the first to give women the right to vote?", "New Zealand"),
        ("Which footballer holds the record for most goals scored in a calendar year?", "Lionel Messi"),
        ("Who painted the ceiling of the Sistine Chapel?", "Michelangelo"),
        ("What is the capital of Bhutan?", "Thimphu"),
        ("Which country hosted the 2010 FIFA World Cup?", "South Africa"),
        # VERY DIFFICULT
        ("What is the tallest mountain in the world?", "Mount Everest"),
        ("Which footballer has the most assists in Premier League history?", "Ryan Giggs"),
        ("What is the speed of light in vacuum in meters per second?", "299,792,458 m/s"),
        ("Which is the only continent without an active volcano?", "Australia"),
        ("Which country won the first-ever Women's FIFA World Cup?", "USA")
    ]
    
    return questions_and_answers

def quiz_game():
    score = 0  # To keep track of the player's score
    max_attempts = 5  # Maximum allowed wrong answers
    wrong_attempts = 0  # To count the number of wrong attempts

    questions_and_answers = game_questions_and_answer()
    total_questions = len(questions_and_answers)

    for i, (question, correct_answer) in enumerate(questions_and_answers):
        while wrong_attempts < max_attempts:
            print(f"Question {i + 1}: {question}")
            user_answer = input("Your answer: ").strip()

            if user_answer.lower() == correct_answer.lower():
                print("Correct!\n")
                score += 1
                break  # Move to the next question
            else:
                wrong_attempts += 1
                if wrong_attempts < max_attempts:
                    print(f"Wrong! Try again. ({wrong_attempts}/{max_attempts} wrong attempts)\n")
                else:
                    print("Game Over! You've reached the maximum number of wrong attempts.")
                    print(f"Your score{score}")
                    return  # Exit the game

    print(f"Congratulations! You completed the quiz. You scored {score} out of {total_questions}.")

if __name__ == "__main__":
    quiz_game()