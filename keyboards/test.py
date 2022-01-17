
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.callbackdatas import testing

testing_kb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Edit Name', callback_data=testing.new(
                                              button1='button1')),
                                          InlineKeyboardButton(text='Edit Description', callback_data=testing.new(
                                              button1='button2'))
                                      ],
                                      [
                                          InlineKeyboardButton(text='Edit About', callback_data=testing.new(
                                              button1='button3')),
                                          InlineKeyboardButton(text='Edit Botpic', callback_data=testing.new(
                                              button1='button4'))
                                      ],
                                      [
                                          InlineKeyboardButton(text='Edit Commands', callback_data=testing.new(
                                              button1='button5')),
                                          InlineKeyboardButton(text='<<Back to Bot', callback_data=testing.new(
                                              button1='button6'))
                                      ]
                                  ]
                                  )