import tkinter as tk
from tkinter import scrolledtext
import time
import threading

# Simple rule-based responses
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello there! 👋 How can I assist you?"
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm doing great! 😄"
    elif "your name" in user_input:
        return "I'm ChatPy — your Python chatbot assistant!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day! 👋"
    else:
        return "Sorry, I didn't understand that. Can you rephrase? 🤔"

# GUI class
class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("💬 ChatPy - Python Chatbot")
        self.root.geometry("500x600")
        self.root.config(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Helvetica", 12))
        self.chat_area.place(x=20, y=20, width=460, height=450)
        self.chat_area.config(state=tk.DISABLED)

        self.entry = tk.Entry(self.root, font=("Helvetica", 14), bg="#ffffff")
        self.entry.place(x=20, y=490, width=350, height=40)
        self.entry.bind("<Return>", lambda event: self.send_message())

        self.send_button = tk.Button(self.root, text="Send", font=("Helvetica", 12), bg="#0084ff", fg="white",
                                     command=self.send_message)
        self.send_button.place(x=380, y=490, width=100, height=40)

        self.label = tk.Label(self.root, text="Chat with your Python Assistant 🤖", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
        self.label.place(x=90, y=550)

    def send_message(self):
        user_message = self.entry.get().strip()
        if user_message == "":
            return

        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, "You: " + user_message + "\n", "user")
        self.chat_area.tag_config("user", foreground="#3333cc")

        self.entry.delete(0, tk.END)
        self.chat_area.config(state=tk.DISABLED)

        # Use threading for delay effect
        threading.Thread(target=self.bot_response_with_delay, args=(user_message,)).start()

    def bot_response_with_delay(self, user_input):
        time.sleep(0.5)
        bot_response = get_bot_response(user_input)
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, "Bot: " + bot_response + "\n\n", "bot")
        self.chat_area.tag_config("bot", foreground="#009933")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()
