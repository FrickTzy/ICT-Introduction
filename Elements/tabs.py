from tkinter import ttk, Tk
from .frames import FrameElements
from .info_frame import InfoFrame
from .hobby_frame import HobbyFrame
from .anime_frame import AnimeFrame


class Tabs:
    def __init__(self, window: Tk, style):
        self.tab_nb = ttk.Notebook(window, width=1000, height=1000)
        self.info_tab = InfoFrame(self.tab_nb)
        self.hobby_tab = HobbyFrame(self.tab_nb)
        self.fav_anime_tab = AnimeFrame(self.tab_nb)
        self.unbind()
        self.add_tab()

    def unbind(self):
        self.tab_nb.unbind("<Right>")
        self.tab_nb.unbind("<Left>")

    def add_tab(self):
        self.tab_nb.add(self.info_tab.info_frame, text="Personal Info")
        self.tab_nb.add(self.hobby_tab.info_frame, text="Hobbies")
        self.tab_nb.add(self.fav_anime_tab.info_frame, text="Favorite Anime")
