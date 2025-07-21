from db_management import chat_history
# bot_logic.py
class bot_logic:
    db = chat_history()
    def __init__(self, usr_in, chat, tk):
        self.usr_input = usr_in
        self.chat = chat
        self.tk = tk
        self.db = chat_history()
        
    def chat_response(self):
        if "hi" in self.usr_input.get():
            return "Hi 👋 what's on your mind"
        elif "hello" in self.usr_input.get():
            return "Hello 😊 there what's with this energy "
        else: return "Sorry 🥲 I didnt get that...! "

    def send_response(self):
        input = self.usr_input.get().lower()  
        self.chat.config(state=self.tk.NORMAL)
        self.chat.insert(self.tk.END, "\nYOU: " + input + "\n")
        self.db.ins("user", input)
        chat_res = self.chat_response() 
        self.chat.insert(self.tk.END, "> " + chat_res + "\n\n")
        self.db.ins("bot", chat_res)    
        self.chat.config(state=self.tk.DISABLED)
        self.usr_input.delete(0, self.tk.END)    
        
    def chat_his(self):
        rows = self.db.fetch()
        self.chat.config(state=self.tk.NORMAL)
        self.chat.insert(self.tk.END, "History:\n\n")
        for sender, msg in rows:
            self.chat.insert(self.tk.END, f"{sender}: {msg}\n")
        self.chat.config(state=self.tk.DISABLED)
        self.chat.see(self.tk.END)
        self.chat.delete(1.0, self.tk.END)
        
    def clear_chat(self):
        self.chat.config(state=self.tk.NORMAL) 
        self.chat.delete("1.0", self.tk.END)   
        self.chat.config(state=self.tk.DISABLED)  
