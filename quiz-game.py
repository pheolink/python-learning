import random

print("Welcome to my computer quiz")

playing = input("Do you want to play: ")

if playing.lower() not in ("yes", "y"):
    print("Okay! Let's play some other time.")
    quit()

print("Okay! Let's play :) ")

questions = [
    "What does CPU stand for? ",
    "What does GPU stand for? ",
    "What does RAM stand for? ",
    "What does PSU stand for? ",
    "What does SSD stand for? "
]

answers = [
    "Central Processing Unit",
    "Graphics Processing Unit",
    "Random Access Memory",
    "Power Supply",
    "Solid State Drive"
]

# Use a set to keep track of asked questions
asked_questions = set()
score = 0

# Loop until all questions are asked
while len(asked_questions) < len(questions):
    # Generate a random index that hasn't been asked before
    random_question = random.randint(0, len(questions) - 1)
    while random_question in asked_questions:
        random_question = random.randint(0, len(questions) - 1)
    
    # Add the current question index to the set of asked questions
    asked_questions.add(random_question)
    
    # Ask the question
    print(f"\nQuestion {len(asked_questions)}: {questions[random_question]}")
    answer = input("Your answer: ").strip().lower()
    
    # Check if the answer is correct
    if answer == answers[random_question].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is: {answers[random_question]}")

# Print final score
print(f"\nQuiz completed! Your final score is: {score}/{len(questions)}")
