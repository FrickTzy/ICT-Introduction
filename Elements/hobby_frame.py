from .frames import FrameElements
from tkinter import Label, Frame
from .settings import BG_COLOR, TXT_COLOR, title_font, norm_font
from .logos import HobbyImg

TXT_X = 240
IMG_X = 50
IMG_Y_DIF = 123
TXT_Y_DIF = 124
TXT_PAD = 30


class TextImage:
    def __init__(self, frame):
        self.main_header = Label(frame, text="My Hobbies", background=BG_COLOR, fg=TXT_COLOR,
                                 font=title_font(frame))
        self.self_info_frame = Frame(frame, bg=BG_COLOR, width=650, height=600)
        self.info = Hobbies(self.self_info_frame)


class Hobbies:
    def __init__(self, frame):
        self.logos = HobbyImg()
        self.first_info = Label(frame, text="1. Drawing", bg=BG_COLOR, fg="white", font=norm_font(frame))
        self.second_info = Label(frame, text="2. Playing Games", bg=BG_COLOR, fg="white", font=norm_font(frame))
        self.third_info = Label(frame, text="3. Watching Anime", bg=BG_COLOR, fg="white", font=norm_font(frame))
        self.draw_img = Label(frame, image=self.logos.draw_img, bg=BG_COLOR)
        self.osu_img = Label(frame, image=self.logos.osu_img, bg=BG_COLOR)
        self.anime_img = Label(frame, image=self.logos.anime_img, bg=BG_COLOR)
        self.place_info()
        self.place_img()

    def place_info(self):
        self.first_info.place(x=TXT_X, y=TXT_PAD)
        self.second_info.place(x=TXT_X, y=TXT_PAD + TXT_Y_DIF)
        self.third_info.place(x=TXT_X, y=TXT_PAD + TXT_Y_DIF * 2)

    def place_img(self):
        self.draw_img.place(x=IMG_X, y=0)
        self.osu_img.place(x=IMG_X, y=IMG_Y_DIF)
        self.anime_img.place(x=IMG_X, y=IMG_Y_DIF * 2)


class HobbyFrame:
    def __init__(self, tab_nb):
        self.info_frame = FrameElements.make_tab_frame(tab_nb)
        self.text_images = TextImage(self.info_frame)
        self.place_elements()

    def place_elements(self):
        self.text_images.main_header.place(x=240, y=438)
        self.text_images.self_info_frame.place(x=78, y=530)
