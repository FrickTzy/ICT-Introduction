from .frames import FrameElements
from tkinter import Label, Frame
from .settings import BG_COLOR, TXT_COLOR, title_font, norm_font
from .logos import PicImg

TXT_X = 300
TXT_Y_DIF = 80
TXT_Y_START = 35


class TextImage:
    def __init__(self, frame):
        self.main_header = Label(frame, text="Arnoco, Kurt Justine", background=BG_COLOR, fg=TXT_COLOR,
                                 font=title_font(frame))
        self.self_info_frame = Frame(frame, bg=BG_COLOR, width=650, height=600)
        self.info = Info(self.self_info_frame)


class Info:
    def __init__(self, frame):
        self.img = PicImg()
        self.first_info = Label(frame, text="-  You can call me Arnoco", bg=BG_COLOR, fg="white", font=norm_font(frame))
        self.second_info = Label(frame, text="-  I'm 15 years old", bg=BG_COLOR, fg="white", font=norm_font(frame))
        self.third_info = Label(frame, text="-  I want to become a Software \nEngineer                             ",
                                bg=BG_COLOR, fg="white", font=norm_font(frame))
        self.photo = Label(frame, image=self.img.pic, bg=BG_COLOR)
        self.place_info()

    def place_info(self):
        self.first_info.place(x=TXT_X, y=TXT_Y_START)
        self.second_info.place(x=TXT_X, y=TXT_Y_START + TXT_Y_DIF)
        self.third_info.place(x=TXT_X, y=TXT_Y_START + TXT_Y_DIF * 2)
        self.photo.place(x=45, y=30)


class InfoFrame:
    def __init__(self, tab_nb):
        self.info_frame = FrameElements.make_tab_frame(tab_nb)
        self.text_images = TextImage(self.info_frame)
        self.place_elements()

    def place_elements(self):
        self.text_images.main_header.place(x=138, y=438)
        self.text_images.self_info_frame.place(x=70, y=540)

