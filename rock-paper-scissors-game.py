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
choice = int(input("Which would you choose? \n Type the number:\n0 - rock \n1 - paper \n2 - scissors\n"))
game = [rock, paper, scissors]
if choice < 0 or choice > 2:
  print("You entered something else. \nGame over!")
else:
  print (game[choice])

  print("Computer selection:")
  choice_comp = random.randint(0,2)
  print(game[choice_comp])

  choice_matrix = [ 
    ["Draw.", "You lost...", "You won!"],
    ["You won!", "Draw.", "You lost..."],
    ["You lost...", "You won!", "Draw."]
  ]
  print(choice_matrix[choice][choice_comp])
