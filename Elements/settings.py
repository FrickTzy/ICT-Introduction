from tkinter.font import Font


def title_font(window):
    return Font(
        family="Calibri",
        size=47,
        weight="bold",
        underline=False
    )


def norm_font(window):
    return Font(
        family="Arial",
        size=18,
        weight="bold",
    )


BG_COLOR: str = "#6f5ee0"
TXT_COLOR: str = "#2b0342"
