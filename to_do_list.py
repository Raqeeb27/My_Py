import tkinter as tk
from tkinter import messagebox, simpledialog

# Function to add a task
def add_task():
    task = simpledialog.askstring("Add Task", "Enter task:")
    if task:
        listbox_tasks.insert(tk.END, task)

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to mark the selected task as completed
def mark_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END, f"{task} (Completed)")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

# Function to update the selected task
def update_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        new_task = simpledialog.askstring("Update Task", "Enter new task:", initialvalue=task)
        if new_task:
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, new_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Creating the main window
root = tk.Tk()
root.title("To-Do List")

# Creating the listbox to display tasks
listbox_tasks = tk.Listbox(root, height=15, width=50, selectmode=tk.SINGLE)
listbox_tasks.pack(pady=10)

# Creating the buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_add_task = tk.Button(frame_buttons, text="Add Task", command=add_task)
button_add_task.pack(side=tk.LEFT, padx=5)

button_update_task = tk.Button(frame_buttons, text="Update Task", command=update_task)
button_update_task.pack(side=tk.LEFT, padx=5)

button_mark_completed = tk.Button(frame_buttons, text="Mark Completed", command=mark_completed)
button_mark_completed.pack(side=tk.LEFT, padx=5)

button_delete_task = tk.Button(frame_buttons, text="Delete Task", command=delete_task)
button_delete_task.pack(side=tk.LEFT, padx=5)

button_exit = tk.Button(root, text="Exit", command=root.quit)
button_exit.pack(pady=10)

# Running the main loop
root.mainloop()
