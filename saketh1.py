import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        # Set the background color to purple
        self.root.configure(bg="#301934")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(root, bg="white")
        self.task_entry.pack(pady=50)
        
        self.add_button = tk.Button(root, text="Add", command=self.add_task, bg="orange", fg="white")
        self.add_button.pack()
        
        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_tasks, bg="orange", fg="white")
        self.clear_button.pack()
        
        self.task_listbox = tk.Listbox(root, bg="white")
        self.task_listbox.pack(pady=10)
        
        self.delete_button = tk.Button(root, text="Delete", command=self.delete_task, bg="orange", fg="white")
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.task_listbox.delete(index)

    def clear_tasks(self):
        self.tasks = []
        self.task_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
