import tkinter as tk
import random

def next_turn(row, col):
    global player

    if buttons[row][col]['text'] == "" and not check_winner():
        buttons[row][col]['text'] = player
        result = check_winner()

        if result == True:   # Someone won
            label.config(text=player + " Won! 🎉")
            disable_buttons()
        elif result == "Tie":
            label.config(text="It's a Tie! 🤝")
        else:
            player = players[1] if player == players[0] else players[0]
            label.config(text=player + " turn...")

def check_winner():
    
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            highlight_buttons([(i, 0), (i, 1), (i, 2)])
            return True

   
    for j in range(3):
        if buttons[0][j]['text'] == buttons[1][j]['text'] == buttons[2][j]['text'] != "":
            highlight_buttons([(0, j), (1, j), (2, j)])
            return True

  
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        highlight_buttons([(0, 0), (1, 1), (2, 2)])
        return True

    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        highlight_buttons([(2, 0), (1, 1), (0, 2)])
        return True

 
    if not empty_spaces():
        return "Tie"

    return False

def empty_spaces():
    spaces = 9
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] != "":
                spaces -= 1
    return spaces != 0  

def highlight_buttons(coords):
    for (i, j) in coords:
        buttons[i][j].config(bg="lightgreen")

def disable_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state="disabled")

def enable_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state="normal")

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn...")
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="SystemButtonFace", state="normal")

# --- GUI Setup ---

win = tk.Tk()
win.title("Tic-Tac-Toe")

players = ["X", "O"]
player = random.choice(players)

label = tk.Label(win, text=player + " turn...", font=("consolas", 20))
label.pack(side="top")

restart_btn = tk.Button(win, text="Restart", font=("consolas", 14), command=new_game)
restart_btn.pack(side="top")

frame = tk.Frame(win)
frame.pack()

buttons = [[None, None, None] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(
            frame, text="", font=("consolas", 20), width=10, height=5,
            command=lambda row=i, col=j: next_turn(row, col)
        )
        buttons[i][j].grid(row=i, column=j)

win.mainloop()
