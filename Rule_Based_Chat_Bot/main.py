import tkinter as tk
import tkinter.font as tkf
from bot_logic import bot_logic

window = tk.Tk()
window.title("CHAT-BOT 🤖")
window.geometry("500x600")
window.config(bg="#181818")

font = tkf.Font(family="consolas", size=14, weight="bold")

label = tk.Label(window, text="ChatBuddy", font=font, bg="#34495e", fg="white", pady=10)
label.pack(fill=tk.BOTH)

chat = tk.Text(window, bg="#303030", fg="white", font=font, state=tk.DISABLED)
chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat.tag_config("> ", font=("bahnschrift", 14, "bold"))

usr_entry = tk.Entry(window, font=font, bg="white", fg="black")
usr_entry.pack(padx=10, pady=10, fill=tk.X)

logic = bot_logic(usr_entry, chat, tk)

btn_frame = tk.Frame(window, bg="#181818")
btn_frame.pack(pady=(10, 20))
send_btn = tk.Button(btn_frame, text="Send", bg="#2e9aa5", fg="white", font=font, command=logic.send_response)
send_btn.pack(side=tk.LEFT, padx=5)
hist_btn = tk.Button(btn_frame, text="History", bg="#2e9aa5", fg="white", font=font, command=logic.chat_his)
hist_btn.pack(side=tk.LEFT, padx=5)
clear_button = tk.Button(window, text="Clear Chat", command=logic.clear_chat, bg="#e74c3c", fg="white")
clear_button.pack(pady=(0, 10))
window.mainloop()