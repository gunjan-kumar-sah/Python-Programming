import tkinter as tk
from tkinter import filedialog, messagebox
import fitz  # PyMuPDF
import nltk
import sqlite3
import datetime, threading

# SQLite setup
conn = sqlite3.connect('study_system.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS flashcards(id INTEGER PRIMARY KEY, question TEXT, answer TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY, task TEXT, due TEXT)')
conn.commit()

# PDF summarizer
def summarize_pdf(path):
    doc = fitz.open(path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    sents = nltk.sent_tokenize(full_text)
    # longest 5 sentences as summary
    return "\n".join(sorted(sents, key=len, reverse=True)[:5])

# Q&A (naive search)
notes_text = ""
def ask_question(q):
    best = max(nltk.sent_tokenize(notes_text), key=lambda s: nltk.edit_distance(q.lower(), s.lower()))
    return best

# GUI
class SmartStudyApp:
    def __init__(self, root):
        self.root = root
        root.title("📚 Smart Study System")
        root.geometry("800x600")

        # Widgets
        self.txt = tk.Text(root)
        self.txt.pack(fill=tk.BOTH, expand=1)

        frm = tk.Frame(root)
        frm.pack(fill=tk.X)
        tk.Button(frm, text="Upload & Summarize PDF", command=self.upload_pdf).pack(side=tk.LEFT)
        tk.Button(frm, text="Ask Question", command=self.ask_win).pack(side=tk.LEFT)
        tk.Button(frm, text="Add Flashcard", command=self.flashcard_win).pack(side=tk.LEFT)
        tk.Button(frm, text="Add To-Do", command=self.todo_win).pack(side=tk.LEFT)

    def upload_pdf(self):
        global notes_text
        path = filedialog.askopenfilename(filetypes=[("PDF files","*.pdf")])
        if path:
            summary = summarize_pdf(path)
            notes_text = fitz.open(path).get_text()  # full text
            self.txt.delete(1.0, tk.END)
            self.txt.insert(tk.END, "📝 Summary:\n"+ summary)

    def ask_win(self):
        q = tk.simpledialog.askstring("Ask", "Enter your question:")
        if q:
            ans = ask_question(q)
            messagebox.showinfo("Answer", ans)

    def flashcard_win(self):
        win = tk.Toplevel(self.root)
        tk.Label(win, text="Question").pack(); q = tk.Entry(win, width=50); q.pack()
        tk.Label(win, text="Answer").pack(); a = tk.Entry(win, width=50); a.pack()
        def save():
            c.execute("INSERT INTO flashcards(question,answer) VALUES(?,?)",(q.get(),a.get()))
            conn.commit(); win.destroy()
        tk.Button(win, text="Save", command=save).pack()

    def todo_win(self):
        win = tk.Toplevel(self.root)
        tk.Label(win, text="Task").pack(); t = tk.Entry(win, width=50); t.pack()
        tk.Label(win, text="Due (YYYY-MM-DD HH:MM)").pack(); d = tk.Entry(win, width=50); d.pack()
        def save_todo():
            c.execute("INSERT INTO todos(task,due) VALUES(?,?)",(t.get(),d.get()))
            conn.commit(); win.destroy()
        tk.Button(win, text="Add To-Do", command=save_todo).pack()
        threading.Thread(target=self.check_todos).start()

    def check_todos(self):
        while True:
            now = datetime.datetime.now()
            for row in c.execute("SELECT id,task,due FROM todos"):
                tid, task, due = row
                due_dt = datetime.datetime.strptime(due, "%Y-%m-%d %H:%M")
                if 0 <= (due_dt - now).total_seconds() < 60:
                    messagebox.showinfo("Reminder", f"To-Do due: {task}")
                    c.execute("DELETE FROM todos WHERE id=?", (tid,))
                    conn.commit()
            threading.Event().wait(60)

if __name__ == "__main__":
    root = tk.Tk()
    nltk.download('punkt')
    app = SmartStudyApp(root)
    root.mainloop()
    conn.close()
