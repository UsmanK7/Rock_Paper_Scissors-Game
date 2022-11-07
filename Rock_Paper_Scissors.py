import random
choice=int(input("What do you choose? type 0 for rock, type 1 for paper, type 2 for sccissors \n"))
rock=('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
  ''')
paper=('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
  ''')
scissors=('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
  ''')
won=('''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
''')
comp=('''
     .-""""""-.
   .'          '.
  /   O      O   \
 :           `    :
 |                |   
 :    .------.    :
  \  '        '  /
   '.          .'   
     '-......-'
''')
choice_image=[rock,paper,scissors]
human_choice=choice_image[choice]
print(human_choice)

print("Computer chooses")

choice2=random.randint(0,2)
comp_choice=choice_image[choice2]
print(comp_choice)

if(choice2==0 and choice==2):
  print("Computer won Game over!")
  print(comp)
elif(choice2==2 and choice==1):
  print("Computer won Game over!")
  print(comp)
elif(choice2==2 and choice==0):
  print("Computer won Game over!")
  print(comp)
elif(choice2==2 and choice==0):
  print("you won")
  print(won)
elif(choice2==1 and choice==2):
  print("you won")
  print(won)
elif(choice2==0 and choice==2):
  print("you won")
  print(won)
else:
  print("its a tie ☺")
