from Elements import *
from Backend import music


class LogoChange:
    switch: str = ""
    vol_repeat: str
    scale_on = False

    @classmethod
    def change_song_name(cls, var: bool = False):
        if var:
            main.variables.song_name.set(music.set_song_title())
        else:
            if music.switch != cls.switch:
                main.variables.song_name.set(music.set_song_title())
                cls.switch = music.switch
                main.window.update()

    @staticmethod
    def change_logo():
        if music.play:
            main.buttons.pause_button.config(image=main.logos.pause_image)
        else:
            main.buttons.pause_button.config(image=main.logos.play_image)

    @classmethod
    def change_vol(cls):
        music.change_volume(main.misc.volume_scale.get())
        cls.vol_repeat = main.window.after(10, cls.change_vol)

    @classmethod
    def show_scale(cls, event=None):
        if cls.scale_on:
            main.misc.volume_scale.place_forget()
            cls.scale_on = False
            main.window.unbind("<Up>")
            main.window.unbind("<Down>")
            main.window.after_cancel(cls.vol_repeat)
        else:
            main.misc.volume_scale.place(x=210, y=-1)
            cls.scale_on = True
            main.window.bind("<Up>", lambda eventz: main.misc.volume_scale.set(main.misc.volume_scale.get() + 0.1))
            main.window.bind("<Down>", lambda eventz: main.misc.volume_scale.set(main.misc.volume_scale.get() - 0.1))
            cls.change_vol()

    @classmethod
    def shortcuts(cls):
        main.window.bind("<Right>", lambda event: [music.change_music(main.window, True),
                                                   cls.change_song_name(True), cls.change_logo()], )
        main.window.bind("<Left>", lambda event: [music.change_music(main.window, False),
                                                  cls.change_song_name(True), cls.change_logo()], )
        main.window.bind("<space>", lambda event: [music.play_music(),
                                                   cls.change_logo()])

    @classmethod
    def idle_executions(cls):
        main.window.after(6, lambda: [music.que(), cls.change_song_name(), cls.idle_executions()])


class Main(Window):
    def __init__(self):
        super().__init__("Arnoco Introduction")
        self.logos = Logos()
        self.variables = Variables()
        self.style_config()
        self.tabs = Tabs(self.window, self.variables.style)
        self.frames = FrameElements(self)
        self.misc = MiscElements(self.frames, self, Main)
        self.buttons = ButtonElements(self, music, LogoChange)
        self.labels = LabelElements(self)
        self.set_var()

    def set_var(self):
        self.variables.song_name.set(music.set_song_title())
        self.misc.volume_scale.set(0.8)

    def style_config(self):
        self.variables.style.theme_use("default")

        self.variables.style.layout("TNotebook", [])
        self.variables.style.configure("TNotebook", background="#2b0342",
                                       tabmargins=0, borderwidth=0, highlightthickness=0, highlightcolor="#2b0342")
        self.variables.style.configure("TNotebook", background="#2b0342", tabposition='w')
        self.variables.style.configure("TNotebook.Tab", borderwidth=0,
                                       highlightthickness=0, background="#2b0342", highlightcolor="#2b0342")
        self.variables.style.map("TNotebook.Tab", background=[("selected", "#6f5ee0")])
        self.variables.style.configure("TNotebook.Tab", focuscolor="#6f5ee0", borderwidth=0, highlightthickness=0,
                                       background="#2b0342", foreground="white", bordercolor="#2b0342",
                                       highlightcolor="#2b0342", font=("Calibri", 12))
        self.variables.style.configure("TNotebook.Tab", width=20, padding=[10, 5], justify="center")

    def place_elements(self):
        self.labels.song_title.place(x=0, y=1)
        self.frames.top_frame.place(x=0, y=0)
        self.frames.music_frame.place(x=680, y=12)
        self.labels.logo_label.place(x=-32, y=-51)
        self.buttons.next_button.place(x=99, y=22)
        self.buttons.prev_button.place(x=20, y=22)
        self.buttons.pause_button.place(x=61, y=22)
        self.buttons.volume_button.place(x=250, y=-9)
        self.tabs.tab_nb.place(x=0, y=-330)

    @staticmethod
    def background_executions():
        music.music()
        LogoChange.shortcuts()
        LogoChange.idle_executions()

    def run(self):
        self.place_elements()
        self.background_executions()
        self.window.mainloop()


if __name__ == "__main__":
    main = Main()
    main.run()
