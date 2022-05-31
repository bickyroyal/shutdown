import os
import tkinter as tk


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("280x100")
        self.resizable(0, 0)
        self.title("Schedule shutdown")

        frame = tk.Frame(self)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(frame, text="Shutdown after").pack(side=tk.LEFT)

        self.entry = tk.Entry(frame, width=6)
        self.entry.pack(side=tk.LEFT, padx=4)
        self.entry.focus()
        
        tk.Label(frame, text="minutes").pack(side=tk.LEFT)

        self.bind("<Return>", self.confirm)
        self.bind("<Escape>", self.cancel)

    def confirm(self, _):
        os.system("shutdown -a > nul 2>&1")
        try:
            seconds = abs(int(self.entry.get())) * 60
        except (ValueError, TypeError):
            self.entry.delete(0, tk.END)
        else:
            os.system(f"shutdown -s -t {seconds} > nul 2>&1")
            self.destroy()
    
    def cancel(self, _):
        os.system("shutdown -a > nul 2>&1")
        self.destroy()


if __name__ == "__main__":
    App().mainloop()
