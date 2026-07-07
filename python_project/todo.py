import tkinter as tk
from tkinter import messagebox

tasks = []

# Function to update the listbox
def update_listbox():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

# Add task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Delete selected task
def delete_task():
    selected = task_list.curselection()
    if selected:
        task_index = selected[0]
        tasks.pop(task_index)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Mark task as done
def mark_done():
    selected = task_list.curselection()
    if selected:
        task_index = selected[0]
        task = tasks[task_index]
        if not task.startswith("✅ "):
            tasks[task_index] = "✅ " + task
            update_listbox()
    else:
        messagebox.showinfo("Info", "Select a task to mark as done.")

# GUI setup
root = tk.Tk()
root.title("📝 To-Do List App")
root.geometry("400x400")
root.resizable(False, False)

# Widgets
title = tk.Label(root, text="My To-Do List", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

task_entry = tk.Entry(root, font=("Helvetica", 12))
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

task_list = tk.Listbox(root, height=10, width=50, font=("Helvetica", 12))
task_list.pack(pady=10)

done_button = tk.Button(root, text="Mark as Done", width=15, command=mark_done)
done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

# Run the app
root.mainloop()
