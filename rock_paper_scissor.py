import random

user_wins = 0
computer_wins = 0

options_for_conditions = ["rock", "paper", "scissor", "r", "p", "s"]
options = ["rock", "paper", "scissor"]

while True:
  user_input = input("Type Rock R/Paper P/ Scissor S or Q to quit: ").lower()
  
  if user_input == "q":
    print("Game ended !")
    print("Good bye")
    break
  
  if user_input not in options_for_conditions:
    print("Type Rock R/Paper P/ Scissor S or Q to qui")
    continue

  random_number = random.randint(0, 2)
  # rock : 0, paper : 1, scissors : 2
  computer_pick = options[random_number]
  print("Computer picked", computer_pick + ".")
  
  
  if (user_input == "rock" or user_input == 'r') and (computer_pick == "scissor" or computer_pick == "s"):
    print("You won !")
    user_wins += 1
    

  elif (user_input == "paper" or user_input == 'p') and (computer_pick == "rock" or computer_pick == "r"):
    print("You won !")
    user_wins += 1
    

  elif (user_input == computer_pick):
    print("You & conmputer picked same. try again !")
    user_wins += 0

  elif (user_input == "scissor" or user_input == 's') and (computer_pick == "paper" or computer_pick == "p"):
    print("You won !")
    user_wins += 1
    
  else:
    print("You lost !")
    computer_wins += 1
   

print("You won", user_wins, "times")
print("Computer won", computer_wins,  "times")

print("Game ended !")
print("Good bye")
