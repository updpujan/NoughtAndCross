#Name: Pujan Upadhyay
#University Student Number: 2408612


#importing random so that we can use the random value to determine computer move
import random
#importing os.path to check if the file exixts or not
import os.path
#importing json to store and retrive the dictonery value from file
import json
#using seed to determine the pattern of random value
random.seed(0)


#declaring draw_board function
def draw_board(board):
    '''
        draw_board(board) function is used to draw the board for game as 3x3 matrix form
        it's structure will look:  -------------
                                   | 1 | 2 | 3 |
                                   -------------
                                   | 4 | 5 | 6 |
                                   -------------
                                   | 7 | 8 | 9 |
                                   -------------
        this function will make the board like structure where there will be number from
        1 to 9 to represents which box is which number but later we will enter 'X' or 'O'
        as per user and computer input. 
    '''
    #using for loop to to keep the number in their respective postion
    for row in board:
        print('-'*13)
        for num in row:
            print(f"| {num}",end=' ')
        print(end='|\n')
    print('-'*13)
    pass


#declaring welcome(board) function 
def welcome(board):
    '''
        welcome(board) function desplays the welcome message and says what this
        program is used. Example, welcome to this game. and this function will
        display the draw_board(board function)
    '''
    # prints the welcome message
    print("Welcome to the \"Unbeatable Nought and CAROSSES\" game.")
    print("The board layout is shown below:")
    # display the board by calling draw_board(board)
    draw_board(board)
    print("When Prompted, enter the number corresponding  to the square you want.\n")
    pass


#declaring initialise_board(board) function
def initialise_board(board):
    '''
        this function is same as draw_board(board) function but inplace of number
        it will keep single space ' ', like:
                                   ----------
                                   |  |  |  |
                                   ----------
                                   |  |  |  |
                                   ----------
                                   |  |  |  |
                                   ----------
    '''
    # using loop to to keep single space ' ' in above box 
    for row in board:
        for i in range(len(row)):
            row[i]=' '
    #returing the above empty board
    return board


#declaring get_player_move(board)    
def get_player_move(board):
    '''
        this function as its name suggest it is used to to take the player move.
        this function will ask user to input the number from 1-9. if it is out of
        range then it will ask again by rasing exception. then it will return row and col
        of that number. eg if choose 5 then row=1 and col=1.
                            
    '''
    # using while loop so that until the input is valid it will keep running
    while True:
        try:
            #use of try except block to raise the error
            x_value = int(input("\t\t    1 2 3\n\t\t    4 5 6\nChoose Your Square: 7 8 9 :"))
            if(x_value < 0 or x_value > 9):
                raise ValueError("Out of Rnage")
        except ValueError as err:
            print("Error: Invalid Input")
        else:
            if(x_value == 1):
                row = 0
                col = 0
            elif(x_value == 2):
                row = 0
                col = 1
            elif(x_value == 3):
                row = 0
                col = 2
            elif(x_value == 4):
                row = 1
                col = 0
            elif(x_value == 5):
                row = 1
                col = 1
            elif(x_value == 6):
                row = 1
                col = 2
            elif(x_value == 7):
                row = 2
                col = 0
            elif(x_value == 8):
                row = 2
                col = 1
            elif(x_value == 9):
                row = 2
                col = 2
            break
    #returning row and col
    return row, col


#declaring choose_computer_move(board)
def choose_computer_move(board):
    '''
        this function will use imported random.randint module to give the value
        from 1-9. And it will check if the selected area in board is occupied or not,
        if not then it will return row and col of that number else it will keep
        using random to generate the random value.
        
    '''
    # using while loop to take the value which has not occupied the postion in board
    while True:
        o_value = random.randint(1,9)
        if(o_value == 1):
            row = 0
            col = 0
        elif(o_value == 2):
            row = 0
            col = 1
        elif(o_value == 3):
            row = 0
            col = 2
        elif(o_value == 4):
            row = 1
            col = 0
        elif(o_value == 5):
            row = 1
            col = 1
        elif(o_value == 6):
            row = 1
            col = 2
        elif(o_value == 7):
            row = 2
            col = 0
        elif(o_value == 8):
            row = 2
            col = 1
        elif(o_value == 9):
            row = 2
            col = 2
    # return row and col if condition is met
        if(board[row][col] == ' '):
           return row, col
        

#declaring check_for_win(board,mark)
def check_for_win(board, mark):
    '''
        this function is used to check the condtion for win. there are 8 condtion
        in this game for win. this function will check every condtion, if the
        condition is met then it will return True if some one either user or computer won
        and return false if no win.
    '''
    # checking all the condtion for win
    if((board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or
       (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or
       (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or
       (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or
       (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark) or
       (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or
       (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or
       (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark)):
        #someone won
        return True        
    else:
        # no one won, so False
        return False


#declaring check_for_win(board)
def check_for_draw(board):
    '''
        this function will check if the the game is draw or not. for the condtion to
        be true in  draw case, all the spaces ' ' must be occupied and no any condtion
        for win must be met. If all the spaces are occupied then it will return True
        else False
    '''
    # checking all the postion of board if they are occupied or not
    c = 0
    for row in board:
        for x in row:
            if x == ' ':
                c+=1
    if c == 0:
        #draw case
        return True
    else:
        #non draw case
        return False


#declaring play_game(board) function       
def play_game(board):
    '''
        in this function, above mentioned function will run. if you chooese to play then
        this function will do all the task.
        first it will initialise_board(board) function, this will make single space ' '
        in every postion of board.
        then, draw_board(board) will display the empty board to user.

        then, it will ask user for input to put in the board as 'X'.
        it will check if the following place is occupied or not. if occupied then
        it will ask user for input again.
        else, it keep 'X' in that postion and display the board as:
            if the player choose 5 then:
                                   -------------
                                   |   |   |   |
                                   -------------
                                   |   | X |   |
                                   -------------
                                   |   |   |   |
                                   -------------
        as place is not occupied it will keep there. and then check_for_win(board)
        function will check all the condition for win, if true then return 1
        else, it will check for draw and if true then returns 0. else, it will call
        for computer move. as same after the computer move is made then, checks for win,
        if true then returns -1 and if draw then 0.

        this process will keep on runnig=ng till there is win by user, win by computer or
        draw.

    '''
    #keeps ' ' in all postion of board
    initialise_board(board)
    #display the board to user
    draw_board(board)
    #use of while loop as we dont know till when the loop will keep running
    while True:
        #taking user move 
        try:
            #use to try except block, if the user inputs wrong input
            result = get_player_move(board)
            #checking if the entered postion is empty or occupied
            if(board[result[0]][result[1]] != ' '):
                raise ValueError("The place is already occupied, choose again")
        except ValueError as err:
            print(err)
        else:
            mark='X'
            #as postion not occupied keep 'X' in that place
            board[result[0]][result[1]] = mark
            #displays the latest board
            draw_board(board)
            #checking for win
            if(check_for_win(board, mark) == True):
                print("You Win!")
                return 1
            #checking for draw
            elif(check_for_draw(board) == True):
                print("Draw!")
                return 0
            #calling computers move
            else:
                result = choose_computer_move(board)
                mark='O'
                #keeping the computer move in board
                board[result[0]][result[1]] = mark
                #displaying the latest board
                draw_board(board)
                #checking for win by computer
                if(check_for_win(board, mark) == True):
                    print("You lose!")
                    return -1
                #checking for draw
                elif(check_for_draw(board) == True):
                    print("Draw!")
                    return 0                    


#declaring menu() function
def menu():
    '''
        this function is ued to display the menu of this program. simply, what we can do in
        this program. according to the number or character choosen from menu, other functions will be called and
        runned.        
    '''
    while True:
        try:
            #displaying all the menu otions
            print("\nEnter one of the following options:")
            print("\t1 - Play the game")
            print("\t2 - Save score to leaderboard")
            print("\t3 - Load and display the leaderboard")
            print("\tq - End the program")
            #tsking the choice from user
            choice = input("1, 2, 3 or q? ").lower().strip()
            #checking if the input is valid or not, if valid then return that input else raise error
            if(choice == '1' or choice == '2' or choice == '3' or choice == 'q'):
                return choice
                break
            else:
                raise ValueError("Invalid Input!!!")
        except ValueError as err:
            print("Error:",err)


#declaring load_scores() function
def load_scores():
    '''
        this function is used to load the all scores from file and display it to user.
        first, it check if file exists or not. if exists then will open file the in read mode
        then keep all the data in leaders.
        since we are storing and retriving the data in dictionery form we are using json module to do so.
        if the file is empty then it will display 'No users in leaderboard'.
        and if file is not found then it will create it and show message 'No users in leaderboard'
    '''
    #checking if file exists
    if(os.path.exists('leaderboard.txt')):
        #opeing the file in read mode
            with open('leaderboard.txt','r') as file:
                try:
                    #keeping the dictionery value from file to variable in dictionery format as key value.
                    leaders = json.load(file)
                except:
                    leaders = 'No users in leaderboard'
    else:
        #creating the file 
        with open('leaderboard.txt','w') as file:
            leaders = 'No users in leaderboard'
    #returing leaders
    return leaders    


#declaring save_score(score) function
def save_score(score):
    '''
        this function is used to save the score in file. if the user is new then new score will be saved else score will be added
        to the old score.
        first, it will open the file in read mode and store all the value in single variable. then open the file in write mode.
        it will check if the usename given by user already exists, if yes then it will add to its value othrwise, new user with
        new score will be saved in file.
    '''
    #asking the user for their name
    name=input("Username:")
    #checking if file exists
    if(os.path.exists('leaderboard.txt')):
        #opening the file in read mode
            with open('leaderboard.txt','r') as file:
                #keeping all the value in single variable
                try:
                    leaderboard = json.load(file)
                except:
                    #as error occurs, which means there is no data in file then new user will be added to dictionery
                    with open("leaderboard.txt",'w') as write_file:
                        #declaring dictionery
                        leaderboard = {}
                        #keeping the user name and their score in dictioney
                        leaderboard[name] = score
                        #keeing the data in file
                        json.dump(leaderboard,write_file)
                else:
                    #as error does not occure, else block will run
                    try:
                        #checks if the entered username is in dictionery or not
                        if(leaderboard[name]):
                            #if present then it will take new value and add it with old value and store in dictionery by appending it
                            old_score = leaderboard[name]
                            new_score = old_score + score
                            leaderboard[name] = new_score
                            #opening the file in write mode and keeping all the data inside file
                            with open("leaderboard.txt",'w') as write_file:
                                json.dump(leaderboard,write_file)
                    except:
                        #if the username does not exists then it will keep the current score to that username in dictionery
                        leaderboard[name] = score
                        #opening file in write mode to keep the data in file
                        with open("leaderboard.txt",'w') as write_file:
                            json.dump(leaderboard,write_file)
    else:
        #if file does not exists then will create it and keep the data in variable and then into file
        with open('leaderboard.txt','w') as write_file:
            leaderboard = {}
            leaderboard[name] = score
            json.dump(leaderboard,write_file)
    #it returns nothing
    return 


#declaring display_leaderboard(leaders) function    
def display_leaderboard(leaders):
    '''
        this function is used to display the leaderboard of user which stores the data of users name and
        their score in dictionery form. it display each item one by one in key value pair. if the varable is empty then
        will display 'no data in file' message. 
    '''
    print('\n\t LEADERBOARD')
    
    if type(leaders) is not dict:
        print(f'\t{leaders}')
    else:
        for key,value in leaders.items():
            print(f"{key}: {value}")
    pass
