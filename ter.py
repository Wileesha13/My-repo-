import tkinter as tk
from tkinter import scrolledtext
import subprocess
# Use a pipeline as a high-level helper
from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="nvidia/Llama-3.1-Nemotron-70B-Instruct-HF")
pipe(messages)
# Function to execute the command and display output
def execute_command():
    command = entry.get().strip()
    
    if command.lower() == "clear":
        # Clear the terminal output
        terminal_output.delete(1.0, tk.END)
        entry.delete(0, tk.END)  # Clear the entry
    elif command.lower() == 'exit':
        root.destroy()
        
    elif command:  # Ensure the command is not empty
        try:
            # Execute the command
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            # Show the output or error
            if result.returncode == 0:
                # Normal output in white color
                terminal_output.insert(tk.END, f"> {command}\n", "command")
                terminal_output.insert(tk.END, result.stdout, "output")
                terminal_output.insert(tk.END, f"Task Executed\n", "executed")
            else:
                # Error output in red color
                terminal_output.insert(tk.END, f"> {command}\n", "command")
                terminal_output.insert(tk.END, result.stderr, "error")
            terminal_output.see(tk.END)  # Auto scroll to the end
        except Exception as e:
            terminal_output.insert(tk.END, f"Error: {e}\n", "error")
            
        entry.delete(0, tk.END)  # Clear the entry

# Create the main application window
root = tk.Tk()
root.title("Windows Terminal Emulator")
root.geometry("1000x600")

# Frame for the terminal output
terminal_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 10), bg="black", fg="white")
terminal_output.pack(expand=True, fill=tk.BOTH)

# Define tags for different text colors
terminal_output.tag_config("command", foreground="white")
terminal_output.tag_config("output", foreground="white")
terminal_output.tag_config("error", foreground="red")
terminal_output.tag_config("executed", foreground="green")

# Frame to hold the ">" symbol and the Entry widget
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X)

# Label for the ">" symbol
prompt_label = tk.Label(input_frame, text=">", font=("Courier", 10), bg="gray", fg="black")
prompt_label.pack(side=tk.LEFT)

# Entry widget for typing commands
entry = tk.Entry(input_frame, font=("Courier", 10), bg="gray", fg="black")
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry.bind("<Return>", lambda event: execute_command())  # Bind Enter key to run the command

# Run the Tkinter event loop
root.mainloop()
