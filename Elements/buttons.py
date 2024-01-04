from tkinter import Button


class ButtonElements:
    def __init__(self, main_cls, music, logo_change):
        self.pause_button = self.make_pause_button(main_cls, music, logo_change)
        self.next_button = self.make_next_button(main_cls, music, logo_change)
        self.prev_button = self.make_prev_button(main_cls, music, logo_change)
        self.volume_button = self.make_volume_button(main_cls, logo_change)

    @staticmethod
    def make_pause_button(self, music, logo_change) -> Button:
        return Button(self.frames.music_frame,
                      image=self.logos.pause_image,
                      command=lambda: [music.play_music(),
                                       logo_change.change_logo()],
                      bg="#2b0342",
                      bd=0,
                      activebackground="#2b0342", )

    @staticmethod
    def make_next_button(self, music, logo_change) -> Button:
        return Button(self.frames.music_frame,
                      image=self.logos.next_image,
                      command=lambda: [music.change_music(self.window, True),
                                       logo_change.change_song_name(True), logo_change.change_logo()],
                      bg="#2b0342",
                      bd=0,
                      activebackground="#2b0342",
                      )

    @staticmethod
    def make_prev_button(self, music, logo_change) -> Button:
        return Button(self.frames.music_frame,
                      image=self.logos.previous_image,
                      command=lambda: [music.change_music(self.window, False),
                                       logo_change.change_song_name(True), logo_change.change_logo()],
                      bg="#2b0342",
                      bd=0,
                      activebackground="#2b0342",
                      )

    @staticmethod
    def make_volume_button(self, logo_change) -> Button:
        return Button(self.frames.music_frame,
                      image=self.logos.volume_image,
                      command=logo_change.show_scale,
                      bg="#2b0342",
                      bd=0,
                      activebackground="#2b0342", )
