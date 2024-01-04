from tkinter import Scale


class MiscElements:
    def __init__(self, frames, main_cls, main):
        self.volume_scale = self.make_volume_scale(frames)

    @staticmethod
    def make_volume_scale(frames) -> Scale:
        return Scale(frames.music_frame,
                     from_=1,
                     to=0,
                     length=70,
                     resolution=0.1,
                     fg="white",
                     background="#2b0342",
                     troughcolor="white",
                     bd=0,
                     highlightthickness=0,
                     sliderrelief='flat',
                     sliderlength=12
                     )
