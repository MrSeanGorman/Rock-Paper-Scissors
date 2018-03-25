from rps import compare

def main():
    sets = int(input("How many sets would you like to make this best-of? (Odd numbers only, please)"))
    wins_required = sets / 2 + 0.5
    p1_wins = 0
    p2_wins = 0
    while wins_required > p1_wins or wins_required > p2_wins:
        player_one_choice = input('Player One, would you like to play rock, paper, or scissors?')
        player_two_choice = input('Player Two, would you like to play rock, paper, or scissors?')
        print('Player One chose {} and Player Two chose {}!'.format(player_one_choice.lower(), player_two_choice.lower()))
        result = compare(player_one_choice.lower(), player_two_choice.lower())
        if result == 'Player One wins!':
            p1_wins = p1_wins + 1
            print('Player one won that rounb and the score is now P1: {} P2: {}'.format(p1_wins, p2_wins))
        elif result == 'Player Two wins!':
            p2_wins = p2_wins + 1
            print('Player two won that round and the score is now P1: {} P2: {}'.format(p1_wins, p2_wins))
        else:
            print('That round was a tie and the score remains P1: {} P2: {}'.format(p1_wins, p2_wins))
    if p1_wins == wins_required:
        print('Player One has won with a final score of P1: {} P2: {}'.format(p1_wins, p2_wins))
    else:
        print('Player Two has won with a final score of P1: {} P2: {}'.format(p1_wins, p2_wins))
    play_again = input('Would you like to play again?')
    while play_again.lower().startswith('y'):
        main()
    exit()
    


if __name__ == "__main__":
    main()