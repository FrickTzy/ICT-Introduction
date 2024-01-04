from .frames import FrameElements
from tkinter import Label, Frame
from .settings import BG_COLOR, TXT_COLOR, title_font, norm_font
from .logos import AnimeImg

TXT_X = 140
TXT_X_DIF = 340
IMG_X = 0
IMG_2_X = 340
IMG_Y_DIF = 100
TXT_Y_DIF = 200
TXT_PAD = 60


class TextImage:
    def __init__(self, frame):
        self.main_header = Label(frame, text="My Favorite Anime", background=BG_COLOR, fg=TXT_COLOR,
                                 font=title_font(frame))
        self.underline = Label(frame, width=71, height=1, background=TXT_COLOR)
        self.self_info_frame = Frame(frame, bg=BG_COLOR, width=800, height=600)
        self.info = Anime(self.self_info_frame)


class Anime:
    def __init__(self, frame):
        self.logos = AnimeImg()
        self.first_info = Label(frame, text="1. Spy x Family", bg=BG_COLOR, fg="white", font=norm_font(frame))
        self.second_info = Label(frame, text="2. One Piece", bg=BG_COLOR, fg="white", font=norm_font(frame))
        self.third_info = Label(frame, text="3. Angel Next \nDoor       ", bg=BG_COLOR,
                                fg="white", font=norm_font(frame))
        self.fourth_info = Label(frame, text="4. Beelzebub", bg=BG_COLOR, fg="white", font=norm_font(frame))
        self.spy_family_img = Label(frame, image=self.logos.spy_family_img, bg=BG_COLOR)
        self.one_piece_img = Label(frame, image=self.logos.one_piece_img, bg=BG_COLOR)
        self.angel_rotten_img = Label(frame, image=self.logos.angel_rotten_img, bg=BG_COLOR)
        self.beelzebub_img = Label(frame, image=self.logos.beelzebub_img, bg=BG_COLOR)
        self.place_info()
        self.place_img()

    def place_info(self):
        self.first_info.place(x=TXT_X, y=TXT_PAD)
        self.second_info.place(x=TXT_X, y=TXT_PAD + TXT_Y_DIF)
        self.third_info.place(x=TXT_X + TXT_X_DIF, y=TXT_PAD)
        self.fourth_info.place(x=TXT_X + TXT_X_DIF, y=TXT_PAD + TXT_Y_DIF)

    def place_img(self):
        self.spy_family_img.place(x=IMG_X, y=0)
        self.one_piece_img.place(x=IMG_X, y=TXT_Y_DIF)
        self.angel_rotten_img.place(x=IMG_2_X, y=0)
        self.beelzebub_img.place(x=IMG_2_X, y=TXT_Y_DIF)


class AnimeFrame:
    def __init__(self, tab_nb):
        self.info_frame = FrameElements.make_tab_frame(tab_nb)
        self.text_images = TextImage(self.info_frame)
        self.place_elements()

    def place_elements(self):
        self.text_images.main_header.place(x=155, y=438)
        # self.text_images.underline.place(x=155, y=510)
        self.text_images.self_info_frame.place(x=85, y=525)
