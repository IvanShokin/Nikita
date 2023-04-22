from json import load, dump
from pathlib import Path
from random import randint

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
# from vk_api.keyboard import VkKeyboard, VkKeyboardColor

TOKEN = 'dda4bbad0100bbce1899e2ab3a63e6ef4e54d3848eef2402566e3dd2efdbe3b613e2d2cca23efc945afb3'


def new_mess(user_id, mes_for_user, list_words_color=None):
    vk.method('messages.send',
              {'user_id': user_id,
               'message': mes_for_user,
               'random_id': randint(0, 1000000000),
               # 'keyboard': get_keyboard(list_words_color)
               }
              )


def save_user_info(user_id, data):
    with open(f'{user_id}.json', "w", encoding='utf-8') as file_user:
        dump(data, file_user)
        return data


def get_user_info(user_id):
    path = Path(f'{user_id}.json')
    if path.exists():
        with path.open("r", encoding='utf-8') as file_user:
            return load(file_user)
    else:
        return save_user_info(user_id, {'mess_counter': 0})


vk = vk_api.VkApi(token=TOKEN)

longpoll = VkLongPoll(vk)

with open('requests_response.json', 'r', encoding='utf-8') as file:
    requests_response = load(file)

print("Начали")
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id

        data = get_user_info(user_id)
        data['mess_counter'] += 1
        save_user_info(user_id, data)

        response = requests_response.get(event.text, 'Я не знаю такой команды. Я БОТ')
        response += f'\nВы написали нам {data["mess_counter"]} раз'
        new_mess(user_id, response)
