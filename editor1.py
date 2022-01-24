#editor1.py
from tkinter import *
class Editor:
    def __init__(self):
        self.fenster = Tk()
        self.fenster.title("Texteditor Nr.1")
        self.text = Text(self.fenster,
                         width=40, height=20,
                         wrap=WORD,
                         font=('Arial', 10))
        self.text.pack()
        self.fenster.mainloop()

editor = Editor()
