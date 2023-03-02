from main_creator_bots.markup_bots.markups_templates import MarkupsTemplates
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

class Markups(MarkupsTemplates):
    def __init__(self, JSON: dict):
        super().__init__(JSON)
        self.BUTTONS = []
        self.replyBUTTONS = []
    def MarkupsCreat(self):
        for page in range(len(self.DATA)):
            CURRENT = []
            for buttons_page in range(len(self.DATA[page])):
                CURRENT.append({
                    page + 1: KeyboardButton(self.DATA[page][buttons_page]['text']),
                })
            self.BUTTONS.append(CURRENT)

    def ReplyMarkupCreate(self):
        for page in range(len(self.BUTTONS)):
            self.replyBUTTONS.append(ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(*self.BUTTONS[page]))