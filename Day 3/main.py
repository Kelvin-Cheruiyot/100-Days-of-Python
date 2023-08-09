s1=input("You see a two roads ahead where do you go?Left or Right? l or r: ")
if s1=='l':
  print('You continue running')
  s2=input("You see ahead there is a river what do you do?Swim across or Wait for the boat? s or w: ")
  if s2=='w':
    print('You row across the river to a land')
    s3=input("You see ahead there is a house with three doors.Which door will you open?Blue or Red or Yellow? b or r or y: ")
    if s3=='r':
      print('Game Over. The door was rigged with explosives')
    elif s3=='b':
      print('Game Over. There was no door. It was an illusion.')
    else:
      print('Congratulations You Win!!!')
else:
  print("Game  Over. You fall into a prey hole")