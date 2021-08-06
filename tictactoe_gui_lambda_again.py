#GUIDE
#First, look at the initilization codes (Line 12 to 26).
#Then, see what buttons exist (line 168 to 212).
#Then see all the functions (line 33 to 162).
#The rest of the stuff is just the usual (Like root = Tk()) or 
#the mainloop code.
#In total, there are 3 defined functions, 11 buttons (9 of which are 
#the grid buttons), and 1 label
#

#INITIALIZATION
from tkinter import *


over = False                #Game over variable
first_player = True         #Player 1 goes first
player_text = "Player 1's turn!"   


blank = '    '      
grid = ((1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3))
grid_slot = {i:blank for i in grid  }#Initializes the grid. Currently,
#each slot is blank. Whenever a player chooses a slot during their
#chance, that slot gets occupied by that particular player

win_condition = (((1,1), (1,2), (1,3)), ((1,1), (2,1), (3,1)),
    ((1,1), (2,2), (3,3)), ((2,1), (2,2), (2,3)), ((3,1), (3,2), (3,3)),
    ((1,3), (2,2), (3,1)), ((1,2), (2,2), (3,2)), ((1,3), (2,3), (3,3)))    
# If any of the grid slots match the above tuples, they player wins



def wincheck():   #To check if a player has won the game
    global over   
    global first_player
    global player_text

    #Mindbending stuff ahead (IMO)
    x = tuple(coord for coord,occupied in grid_slot.items() if\
    occupied == ' X ') # Tuple containing all slots occupied by X
    o = tuple(coord for coord,occupied in grid_slot.items() if\
    occupied == ' O ') # Tuple containing all slots occupied by O

    combx = []  #Initializing an empty list for combinations (nCr)
                #of tuples (taken 3 at once) possible for player X
    combo = []  #Same thing as above, but for O

    #MIND BENDER REGION
    for i, j in enumerate(x):   #Creating combinations and appending   
        for k in range(i + 1, len(x)):
            for z in range(k+1, len(x)):
                combx.append((j, x[k], x[z]))
    for i, j in enumerate(o):
        for k in range(i + 1, len(o)):
            for z in range(k+1, len(o)):
                combo.append((j, o[k], o[z]))
    

    for comb in combx:  #If any of the combinations matches the win
                        #condition, the player wins and the game is over
        if comb in win_condition:
            player_text = ("Player 1 wins!")
            playerDisplay['text'] = player_text
            over = True
    for comb in combo:    
        if comb in win_condition:
            player_text = ("Player 2 wins!")
            playerDisplay['text'] = player_text
            over = True

    #Taking the case of a draw game
    draw_var = 9    #Integer assigned to this variable. Every time a 
                    #slot gets filled, the number is decreased.
                    #When this number reaches 0, the game is a draw
    for i, j in grid_slot.items():
        if j != blank:
            draw_var = draw_var - 1
    if draw_var == 0 and over == False:
        over = True
        player_text = ("The game is a draw!")
        
    if over == True: #If game is over, all buttons (except) must be
                     #disabled and the reset button must be enabled  
        one_one['state'] = DISABLED
        one_two['state'] = DISABLED
        one_three['state'] = DISABLED
        two_one['state'] = DISABLED
        two_two['state'] = DISABLED
        two_three['state'] = DISABLED
        three_one['state'] = DISABLED
        three_two['state'] = DISABLED
        three_three['state'] = DISABLED
        button_retry['state'] = NORMAL
    playerDisplay['text'] = player_text


def click(coordinate):  #Whenever a player clicks on a grid button, a
                        #coordinate corresponding to the button
                        #is used as an argument for this function
    global first_player
    global player_text
    if first_player == True:   
        entry = format('X', '^3') #entry is the variable that will
                                   #replace the 'blank' in the chosen
                                   #slot
        player_text = ("Player 2's turn!")

    elif first_player == False:
        entry = format('O', '^3')
        player_text = ("Player 1's turn!")

    grid_slot[coordinate] = entry
    button_dict[coordinate]['text'] = grid_slot[coordinate] #replacing
                                    #the button's 'blank' with X or O
    button_dict[coordinate]['state'] = DISABLED #Disabling the button
                                    #after it is clicked

    if first_player == True:        #Changing player turn
        first_player = False
    elif first_player == False:
        first_player = True
    playerDisplay['text'] = player_text #This will change the player
                                        #text (that appears at the
                                        #bottom of the window) to  
                                        #whichever player's turn
                                        #is running
    wincheck()

def reset():     #Reset the game when the reset button is hit
    global grid_slot                
    grid_slot = {i:blank for i in grid} 
    global over
    global first_player
    global player_text
    over = False        #Reset game over to False
    first_player = True     #Player 1 goes first
    player_text = "Player 1's turn!"
    
    #Setting back all grid buttons to normal state and then setting
    #them all back to blank.
    one_one['state'] = NORMAL
    one_one['text'] = grid_slot[(1,1)]
    one_two['state'] = NORMAL
    one_two['text'] = grid_slot[(1,2)]
    one_three['state'] = NORMAL
    one_three['text'] = grid_slot[(1,3)]
    two_one['state'] = NORMAL
    two_one['text'] = grid_slot[(2,1)]
    two_two['state'] = NORMAL
    two_two['text'] = grid_slot[(2,2)]
    two_three['state'] = NORMAL
    two_three['text'] = grid_slot[(2,3)]
    three_one['state'] = NORMAL
    three_one['text'] = grid_slot[(3,1)]
    three_two['state'] = NORMAL
    three_two['text'] = grid_slot[(3,2)]
    three_three['state'] = NORMAL
    three_three['text'] = grid_slot[(3,3)]

    #Retry button is disabled, again.
    button_retry['state'] = DISABLED
    playerDisplay['text'] = player_text



root = Tk()

#BUTTONS!
#PlayerDisplay button shows which player's turn it is.
playerDisplay = Label(root, text = player_text, relief=SUNKEN, bd=2)

#Grid buttons
one_one = Button(root, text = grid_slot[(1,1)], command= lambda: click(tuple((1,1))))
one_two = Button(root, text = grid_slot[(1,2)], command= lambda: click(tuple((1,2))))
one_three = Button(root, text = grid_slot[(1,3)], command= lambda: click(tuple((1,3))))
two_one = Button(root, text = grid_slot[(2,1)], command= lambda: click(tuple((2,1))))
two_two = Button(root, text = grid_slot[(2,2)], command= lambda: click(tuple((2,2))))
two_three = Button(root, text = grid_slot[(2,3)], command = lambda: click(tuple((2,3))))
three_one = Button(root, text = grid_slot[(3,1)], command = lambda: click(tuple((3,1))))
three_two = Button(root, text = grid_slot[(3,2)], command = lambda: click(tuple((3,2))))
three_three = Button(root, text = grid_slot[(3,3)], command = lambda: click(tuple((3,3))))

button_dict = {(1,1):one_one,           #Creating a dictionary for 
                (1,2):one_two,          #every grid button
                (1,3):one_three,        #This dictionary is later used
                (2,1):two_one,          #in the click function(line113)
                (2,2):two_two,
                (2,3):two_three, 
                (3,1):three_one, 
                (3,2):three_two, 
                (3,3):three_three}  

#Exit and retry buttons. Exit button will always be active. Retry
#button will only be active whenever the game is over
button_exit = Button(root, text="Exit", command=root.quit)
button_retry = Button(root, text="Play another game", state=DISABLED, command=reset)


#Displaying each button on the window
one_one.grid(column=0, row=0, padx=10, pady=10)
one_two.grid(column=0, row=1, padx=10, pady=10)
one_three.grid(column=0, row=2, padx=10, pady=10)
two_one.grid(column=1, row=0, padx=10, pady=10)
two_two.grid(column=1, row=1, padx=10, pady=10)
two_three.grid(column=1, row=2, padx=10, pady=10)
three_one.grid(column=2, row=0, padx=10, pady=10)
three_two.grid(column=2, row=1, padx=10, pady=10)
three_three.grid(column=2, row=2, padx=10, pady=10)

button_retry.grid(column=0, row=4, columnspan=2, pady=5, padx=1)
playerDisplay.grid(column = 0, row=3, columnspan=3, sticky=W+E)
button_exit.grid(column=2, row=4, pady=5, padx=1)





    






root.mainloop()

