from tkinter import StringVar, ttk


class Variables:
    def __init__(self):
        self.song_name = StringVar()
        self.lang = StringVar()
        self.lang_result = StringVar()
        self.style = ttk.Style()
