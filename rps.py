def compare(p1, p2):
    choices_dict = {'rock' : 'paper', 'paper' : 'scissors', 'scissors' : 'rock'}
    if p1 == p2:
        return 'Its a tie!'
    elif p2 == choices_dict.get(p1):
        return 'Player Two wins!'
    else:
        return 'Player One wins!'



def main():
    player_one_choice = input('Player One, would you like to play rock, paper, or scissors?')
    player_two_choice = input('Player Two, would you like to play rock, paper, or scissors?')
    print('Player One chose {} and Player Two chose {}!'.format(player_one_choice.lower(), player_two_choice.lower()))
    print(compare(player_one_choice.lower(), player_two_choice.lower()))
    play_again = input('Would you like to play again?')
    while play_again.lower().startswith('y'):
        main()
    exit()
    
    


    
    

if __name__ == '__main__':
    main()