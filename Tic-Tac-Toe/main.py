import tkinter as tk
import random

def next_turn(row, col):
    global player    
    print(f"Pressed: ({row}, {col}) | Player: {player}")

    if buttons[row][col]['text'] == "" and check_winner() is False:
        buttons[row][col]['text'] = player
        result = check_winner()
        if result == True:
            label.config(text=player + " Won...!")
        elif result == "Tie":
            label.config(text="Tied...!")
        else:
            player = players[1] if player == players[0] else players[0]
            label.config(text=player + " turn...!")
def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return True
    for j in range(3):
        if buttons[0][j]['text'] == buttons[1][j]['text'] == buttons[2][j]['text'] != "":
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            return True
    elif buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
            return True
    elif empty_spaces() is False:
        return "Tie"
def empty_spaces():
    space = 9
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] != "":
                space -= 1
    if space == 0:
        return False
    else: return True
def new_game():
    pass

win = tk.Tk()
win.title("Tic-Tac-Toe")

players = ["X", "O"]
player = random.choice(players)

label = tk.Label(win, text=player + " turn...!", font=("consolas", 20))
label.pack(side='top')

restart_btn = tk.Button(win, text="Restart", width=5, height=2, command=new_game)
restart_btn.pack(side='top')

frame = tk.Frame(win)
frame.pack(side='top')

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(frame, text="", font=("consolas", 20), width=10, height=5, command= lambda row=i, col=j: next_turn(row, col))
        buttons[i][j].grid(row=i, column=j)
win.mainloop()
