#Name: Pujan Upadhyay
#University Student Number: 2408612


#importing everything'*' from noughtsandcrosses_2408612 
from noughtsandcrosses_2408612 import *


#declaring main() function    
def main():
    '''
        As its name suggests it is the main function of our program.
        The board variable that is passed as an argument in other function is declared here
        it returns nothing, but calls other function as per user need
    '''
    board = [ ['1','2','3'],\
              ['4','5','6'],\
              ['7','8','9']]
    #displaying the welcome message
    welcome(board)
    #score of player when played
    total_score = 0
    #use of while loop so that it will keep running until the condtion met
    while True:
        #taking the choice from user by calling menu() function
        choice = menu()
        if choice == '1':
            #taking the score from playing the game by playing the game
            score = play_game(board)
            #adding the score to total_score
            total_score += score
            print(f'\nYour current score is: {total_score}\n')
        if choice == '2':
            #saving the score in file
            save_score(total_score)
            #re-intitalizing the total value after the previous value was stored in file
            total_score=0
        if choice == '3':
            #keeping the stored scores of user into variable and displaying it.
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('\nThank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return


    
# Program execution begins here
if __name__ == '__main__':
    main()
