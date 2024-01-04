from tkinter import Label


class LabelElements:
    def __init__(self, main_cls):
        self.song_title = self.make_song_title(main_cls.frames, main_cls.variables)
        self.logo_label = self.make_logo_label(main_cls, main_cls.frames)
        self.result_label = self.make_result_label(main_cls)

    @staticmethod
    def make_song_title(frames, variables) -> Label:
        return Label(frames.music_frame, textvariable=variables.song_name, bg="#2b0342", fg="white",
                     font=("Ariel", 15),
                     width=14,
                     anchor="n")

    @staticmethod
    def make_logo_label(self, frames) -> Label:
        return Label(frames.top_frame, image=self.logos.logo_image, bg="#2b0342")

    @staticmethod
    def make_result_label(self):
        return Label(self.window,
                     width=96,
                     height=5,
                     borderwidth=3,
                     relief="solid",
                     text="Translating",
                     fg="#757575",
                     )
