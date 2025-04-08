import random

def roll():
    return random.randint(1,6)

while True:
    number_of_players=int(input("Enter number of players( 2 -> 4 )\n"))
    if 2<= number_of_players <=4:
        break
    else:
        continue

player_score=[]
for i in range(number_of_players):
   player_score.append(0)
max_score=50

while max(player_score)<max_score:

    for player_idx in range(number_of_players):
        print(f'player number {player_idx+1} turn has just started!🚀')
        print(f'your total score is {player_score[player_idx]}')
        current_score=0
        
        while  True:

            while True:
                should_roll = input('Do you want to roll? (y/n):🤔 ').lower()
                if should_roll in ['y', 'n']:
                    break
                print("Invalid input. Please enter 'y' to roll or 'n' to stop.")
                
            if should_roll=='y':
                value=roll()
            else:
                player_score[player_idx]+=current_score
                break

            if value==1:
                current_score=0
                print(f'you rolled {value} so your score in this round is {current_score} 😓')
                break
            
            current_score+=value
            print(f'you rolled {value} so your new score in this round  is {current_score} 🥳')

        if player_score[player_idx]>=50:
            print(f'player number {player_idx+1} just won with score {player_score[player_idx]} 🥳🥳🥳')
            break
    



    
