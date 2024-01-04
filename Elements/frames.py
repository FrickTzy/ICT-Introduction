from tkinter import Frame


class FrameElements:
    def __init__(self, main_cls):
        self.top_frame = self.make_top_frame(main_cls)
        self.music_frame = self.make_music_frame(self.top_frame)

    @staticmethod
    def make_top_frame(self) -> Frame:
        return Frame(self.window, bg="#2b0342", width=1000, height=93)

    @staticmethod
    def make_music_frame(top_frame) -> Frame:
        return Frame(top_frame, width=400, height=100, bg="#2b0342")

    @staticmethod
    def make_tab_frame(tab_nb) -> Frame:
        return Frame(tab_nb, width=600, height=500, bg="#6f5ee0")
