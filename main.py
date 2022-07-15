import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
handGestures = [rock, paper, scissors]

playerChoice = int( input("Welcome to Rock Paper Scissors !\nWhat do you choose ? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n") )
if playerChoice > 2 or playerChoice < 0:
    print("Invaild Choice.")
    exit()
print(f"You Chose :\n{ handGestures[playerChoice] }")

computerChoice = random.randint(0,2)
print(f"Computer Chose :\n{ handGestures[computerChoice] }")

if (playerChoice == 0 and computerChoice == 2) or (playerChoice == 1 and computerChoice == 0) or (playerChoice == 2 and computerChoice == 1):
    print("You Win !")
elif playerChoice == computerChoice:
    print("Draw")
else:
    print("You Lose")