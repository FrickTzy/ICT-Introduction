from tkinter import PhotoImage


class Logos:
    def __init__(self):
        self.logo_image = PhotoImage(file="Images\\Arnoco Logo.png")
        self.pause_image = PhotoImage(file="Images\\PauseButton.png")
        self.play_image = PhotoImage(file="Images\\PlayButton.png")
        self.next_image = PhotoImage(file="Images\\NextButton.png")
        self.previous_image = PhotoImage(file="Images\\PreviousButtonz.png")
        self.volume_image = PhotoImage(file="Images\\Volume.png")


class HobbyImg:
    def __init__(self):
        self.osu_img = PhotoImage(file="Images\\Osu.png")
        self.anime_img = PhotoImage(file="Images\\Animez.png")
        self.draw_img = PhotoImage(file="Images\\Drawing.png")


class AnimeImg:
    def __init__(self):
        self.spy_family_img = PhotoImage(file="Images\\Spy_x_Family.png")
        self.one_piece_img = PhotoImage(file="Images\\One Piece.png")
        self.angel_rotten_img = PhotoImage(file="Images\\AngelRotten.png")
        self.beelzebub_img = PhotoImage(file="Images\\Beel.png")


class PicImg:
    def __init__(self):
        self.pic = PhotoImage(file="Images\\Self_img.png")

