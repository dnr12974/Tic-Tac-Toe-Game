import tkinter

def set_tile(row, column):
    global curr_player

    if (game_over):
        return

    if board[row][column]["text"] != "":
        # Spot already taken
        return
    
    board[row][column]["text"] = curr_player  # Mark the board

    if curr_player == playerO:  # Switch player
        curr_player = playerX
    else:
        curr_player = playerO
    
    label["text"] = curr_player + "'s Move"

    # Check for winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    # Check horizontally, 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " Wins!", foreground=color_black)
            for column in range(3):
                board[row][column].config(foreground=color_green, background=color_light_gray)
            game_over = True
            return
    
    # Check vertically, 3 columns
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " Wins!", foreground=color_black)
            for row in range(3):
                board[row][column].config(foreground=color_green, background=color_light_gray)
            game_over = True
            return
    
    # Check diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " Wins!", foreground=color_black)
        for i in range(3):
            board[i][i].config(foreground=color_green, background=color_light_gray)
        game_over = True
        return

    # Check anti-diagonally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " Wins!", foreground=color_black)
        board[0][2].config(foreground=color_green, background=color_light_gray)
        board[1][1].config(foreground=color_green, background=color_light_gray)
        board[2][0].config(foreground=color_green, background=color_light_gray)
        game_over = True
        return
    
    # Check for a tie
    if (turns == 9):
        game_over = True
        label.config(text="It's a Draw!", foreground=color_black)


def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label.config(text=curr_player + "'s Move", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_purple, background=color_teal)


# Game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

color_purple = "#8e44ad"
color_green = "#27ae60"
color_black="#000000"
color_orange = "#000000"
color_teal = "#1abc9c"
color_light_gray = "#bdc3c7"

turns = 0
game_over = False

# Window setup
window = tkinter.Tk()  # Create the game window
window.title("Ultimate Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player + "'s Move", font=("Verdana", 20), background=color_teal,
                      foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Verdana", 50, "bold"),
                                            background=color_teal, foreground=color_purple, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="Play Again", font=("Verdana", 18), background=color_teal,
                        foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# Center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

# Format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
