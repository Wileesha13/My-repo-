import tkinter as tk
from tkinter import scrolledtext
import subprocess


def execute_command():
    command = entry.get().strip()
    
    if command.lower() == "clear":
        # Clear the terminal output
        terminal_output.delete(1.0, tk.END)
        entry.delete(0, tk.END)  # Clear the entry
    elif command.lower() == 'exit':
        root.destroy()
        
    elif command:  
        try:
            
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                
                terminal_output.insert(tk.END, f"> {command}\n", "command")
                terminal_output.insert(tk.END, result.stdout, "output")
                terminal_output.insert(tk.END, f"Task Executed\n", "executed")
            else:
                
                terminal_output.insert(tk.END, f"> {command}\n", "command")
                terminal_output.insert(tk.END, result.stderr, "error")
            terminal_output.see(tk.END)  
        except Exception as e:
            terminal_output.insert(tk.END, f"Error: {e}\n", "error")
            
        entry.delete(0, tk.END)  


root = tk.Tk()
root.title("Custom LLMOS")
root.geometry("1000x600")


terminal_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 10), bg="black", fg="white")
terminal_output.pack(expand=True, fill=tk.BOTH)

terminal_output.tag_config("command", foreground="white")
terminal_output.tag_config("output", foreground="white")
terminal_output.tag_config("error", foreground="red")
terminal_output.tag_config("executed", foreground="green")


input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X)


prompt_label = tk.Label(input_frame, text=">", font=("Courier", 10), bg="gray", fg="black")
prompt_label.pack(side=tk.LEFT)


entry = tk.Entry(input_frame, font=("Courier", 10), bg="gray", fg="black")
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry.bind("<Return>", lambda event: execute_command())


root.mainloop()
