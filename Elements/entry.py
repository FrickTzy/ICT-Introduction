from tkinter import Entry


class EntryElements:
    def __init__(self, main_cls, language):
        self.input_entry = self.make_input_entry(main_cls)
        self.bind_entry(language)

    @staticmethod
    def make_input_entry(self) -> Entry:
        return Entry(self.window,
                     bg="white",
                     font=("Calibri", 50),
                     width=27,
                     borderwidth=3,
                     relief="solid",
                     )

    def bind_entry(self, language) -> None:
        self.input_entry.bind("<Return>", language.translate_result)
