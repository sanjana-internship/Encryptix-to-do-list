import tkinter as tk
from tkinter import messagebox
import json
import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        engine.say(f"Task added: {task}")
        engine.runAndWait()
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a task
def delete_task():
    try:
        task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(task_index)
        tasks_listbox.delete(task_index)
        engine.say(f"Task deleted: {task}")
        engine.runAndWait()
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to save tasks to a file
def save_tasks():
    tasks = tasks_listbox.get(0, tasks_listbox.size())
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    engine.say("Tasks saved.")
    engine.runAndWait()

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                tasks_listbox.insert(tk.END, task)
        engine.say("Tasks loaded.")
        engine.runAndWait()
    except FileNotFoundError:
        engine.say("No saved tasks found.")
        engine.runAndWait()

# Function to recognize speech and add task
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        engine.say("Please say the task.")
        engine.runAndWait()
        audio = recognizer.listen(source)

        try:
            task = recognizer.recognize_google(audio)
            tasks_listbox.insert(tk.END, task)
            engine.say(f"Task added: {task}")
            engine.runAndWait()
        except sr.UnknownValueError:
            messagebox.showwarning("Warning", "Sorry, I did not understand the task.")
        except sr.RequestError:
            messagebox.showwarning("Warning", "Sorry, speech service is not available.")

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

# Create frames
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

list_frame = tk.Frame(root)
list_frame.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Add widgets to input frame
task_entry = tk.Entry(input_frame, width=30, font=("Arial", 14))
task_entry.grid(row=0, column=0, padx=5, pady=5)

add_task_btn = tk.Button(input_frame, text="Add Task", command=add_task, font=("Arial", 12))
add_task_btn.grid(row=0, column=1, padx=5, pady=5)

speech_task_btn = tk.Button(input_frame, text="Speak Task", command=recognize_speech, font=("Arial", 12))
speech_task_btn.grid(row=0, column=2, padx=5, pady=5)

# Add widgets to list frame
tasks_listbox = tk.Listbox(list_frame, width=45, height=15, font=("Arial", 12))
tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH, pady=5)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

tasks_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_listbox.yview)

# Add widgets to button frame
delete_task_btn = tk.Button(button_frame, text="Delete Task", command=delete_task, font=("Arial", 12))
delete_task_btn.grid(row=0, column=0, padx=5, pady=5)

save_tasks_btn = tk.Button(button_frame, text="Save Tasks", command=save_tasks, font=("Arial", 12))
save_tasks_btn.grid(row=0, column=1, padx=5, pady=5)

load_tasks_btn = tk.Button(button_frame, text="Load Tasks", command=load_tasks, font=("Arial", 12))
load_tasks_btn.grid(row=0, column=2, padx=5, pady=5)

# Load tasks when the application starts
load_tasks()

# Run the application
root.mainloop()
