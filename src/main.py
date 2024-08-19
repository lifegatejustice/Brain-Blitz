import tkinter as tk

def start_game():
    root = tk.Tk()
    root.title("Brain Blitz")   

    
    welcome_label = tk.Label(root, text="Welcome to Brain Blitz!", font=("Poppins", 24))
    welcome_label.pack(pady=20)

    
    start_button = tk.Button(root, text="Start Game", command=start_game)
    start_button.pack(pady=10)

    
    root.mainloop()

if __name__ == "__main__":
    start_game()
