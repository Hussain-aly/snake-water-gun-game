import random

def playgame():
    player_choice =input("Enters S for 'Snake' , W for 'Water' , G for 'gun' : ").lower()
    Com_choice = random.choice (['s' , 'w' , 'g'.lower])



    if player_choice == Com_choice :
       print("It's draw! ")

    elif (player_choice == 's' and Com_choice == 'w') :
        print("You Win! ")  

    elif(player_choice == 'g' and Com_choice == 's') :
        print("You Win! ")
    
    elif(player_choice == 'w' and Com_choice == 'g') :
        print("You Win! ")

    else:
        print("You lose! ")
    

    print(f"You chose: {player_choice}")

    print(f"Computer chose: {Com_choice}")

while True:
  playgame()
  play_again = input("Do you want to play again? (y/n): ").lower()
  if play_again != 'y':
    break

   
print("Thanks for playing")


  
        

    
      

     
    

