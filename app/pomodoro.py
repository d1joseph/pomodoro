# Huy's pomodoro timer
import time
import tkinter as tk

# test window
class Pomodoro(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    
    def create_widgets(self):
        # application title 
        self.title = tk.Label(text="Huy's Pomodoro")
        self.title.pack(side="top")

        # test button
        self.hello_world_btn = tk.Button(text="Click me.")
        self.hello_world_btn["command"] = self.say_hi
        self.hello_world_btn.pack()

        # quit application button
        self.quit = tk.Button(self, text="Quit", fg="blue", command=self.master.destroy)
        self.quit.pack(side="bottom")

    # app functions    
    def say_hi(self):
        print("Hello world, is it me you're looking for?")


if __name__ == "__main__":
    root = tk.Tk()
    app = Pomodoro(master=root)
    app.mainloop()
