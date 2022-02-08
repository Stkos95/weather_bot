from loader import dp
from aiogram import types
import requests
import json
from data.config import token_quiz, link_quiz
from FSM.states import QuizGame
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
import random
class Questions:
    def __init__(self, question, correct_answer, incorrect_answer):
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answer = incorrect_answer


def quiz(amount='10', difficulty='easy',type='boolean'):
    return requests.get(url=link_quiz, params=locals()).json()

@dp.callback_query_handler(text='quiz', state=None)
async def quizing(call: types.CallbackQuery, state: FSMContext):
    question_data = quiz()
    questions_bank = []
    for i in question_data["results"]:
        new_question = Questions(i['question'],i['correct_answer'],i['incorrect_answers'][0])
        questions_bank.append(new_question)

    await call.answer()

    await QuizGame.quiz_1.set()
    async with state.proxy() as data:
        data['number'] = 0
        data['score'] = 0
        data['question_bank'] = questions_bank

        question = data['question_bank'][data['number']].question
        correct_answer = data['question_bank'][data['number']].correct_answer
        incorrect_answer = data['question_bank'][data['number']].incorrect_answer
        await call.message.answer('Ты решил играть!!')
        await call.message.answer(text=f'{question}({correct_answer})', reply_markup=InlineKeyboardMarkup(row_width=2,
                                                                                     inline_keyboard=[
                                                                                         [
                                                                                             InlineKeyboardButton(text=correct_answer, callback_data='correct'),
                                                                                             InlineKeyboardButton(text=incorrect_answer, callback_data='incorrect')
                                                                                         ]
                                                                                     ]))

@dp.callback_query_handler(text='incorrect',state=QuizGame.quiz_1)
async def quiz_answers(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    switch_kb = random.randint(1,2)
    async with state.proxy() as data:
        if data['number'] < len(data['question_bank'])-1:
            data['number'] +=1
            await call.message.answer(f'Вы ответили НЕПРАВИЛЬНО\n'
                                  f'Ваш счет {data["score"]}/{data["number"]}')
            question = data['question_bank'][data['number']].question
            correct_answer = data['question_bank'][data['number']].correct_answer
            incorrect_answer = data['question_bank'][data['number']].incorrect_answer
            await call.message.answer(text=f'{question}({correct_answer})', reply_markup=InlineKeyboardMarkup(row_width=2,
                                                                                                              inline_keyboard=[
                                                                                                                  [
                                                                                                                      InlineKeyboardButton(
                                                                                                                          text=correct_answer,
                                                                                                                          callback_data='correct'),
                                                                                                                      InlineKeyboardButton(
                                                                                                                          text=incorrect_answer,
                                                                                                                          callback_data='incorrect')
                                                                                                                  ]
                                                                                                              ] if switch_kb ==1 else [
                                                                                                                  [
                                                                                                                      InlineKeyboardButton(
                                                                                                                          text=incorrect_answer,
                                                                                                                          callback_data='incorrect'),
                                                                                                                      InlineKeyboardButton(
                                                                                                                          text=correct_answer,
                                                                                                                          callback_data='correct')
                                                                                                                  ]
                                                                                                              ] ))
            await call.message.edit_reply_markup(reply_markup=None)
        else:
            await call.message.answer('Вы завершили викторину!')
            await state.finish()






@dp.callback_query_handler(text='correct',state=QuizGame.quiz_1)
async def quiz_answers(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    switch_kb = random.randint(1,2)
    async with state.proxy() as data:
        if data['number'] < len(data['question_bank'])-1:
            data['number'] += 1
            data['score'] += 1
            await call.message.answer(f'Вы ответили правильно\n'
                                  f'Ваш счет {data["score"]}/{data["number"]}')
            question = data['question_bank'][data['number']].question
            correct_answer = data['question_bank'][data['number']].correct_answer
            incorrect_answer = data['question_bank'][data['number']].incorrect_answer
            await call.message.answer(text=f'{question}({correct_answer})', reply_markup=InlineKeyboardMarkup(row_width=2,
                                                                                                              inline_keyboard=[
                                                                                                                  [
                                                                                                                      InlineKeyboardButton(
                                                                                                                          text=correct_answer,
                                                                                                                          callback_data='correct'),
                                                                                                                      InlineKeyboardButton(
                                                                                                                          text=incorrect_answer,
                                                                                                                          callback_data='incorrect')
                                                                                                                  ]
                                                                                                              ] if switch_kb ==1 else [
                                                                                                                  [
                                                                                                                      InlineKeyboardButton(
                                                                                                                          text=incorrect_answer,
                                                                                                                          callback_data='incorrect'),
                                                                                                                      InlineKeyboardButton(
                                                                                                                          text=correct_answer,
                                                                                                                          callback_data='correct')
                                                                                                                  ]
                                                                                                              ] ))
            await call.message.edit_reply_markup(reply_markup=None)
        else:
            await call.message.answer('Вы завершили викторину!')
            await state.finish()







