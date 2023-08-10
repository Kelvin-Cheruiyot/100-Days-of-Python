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
x=[rock,paper,scissors]
i=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if i>=3 or i<0:
  print("Invalid")
else:
  print(x[i])
  r=random.randint(0,2)
  print(f'Comp chose: ')
  print(x[r])
  if i==0 and r==2:
    print("Win!")
  elif r>i:
    print("Lose")
  elif r==1 and i==2:
    print("Lose")
  elif i>r:
    print("Win!")
  elif r==i:
    print("Draw")