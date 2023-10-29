import json
from datetime import datetime



def load_options(filename):
    with open(filename, 'r') as f:
        operations = json.load(f)
        return operations


def last_five_operations(opiratons):
    abv = []
    for opiration in opiratons:
        if opiration.get('state') == 'EXECUTED':
            abv.append(opiration)

    last_five = sorted(abv, key=lambda opiration:opiration['date'], reverse=True)[0:5]
    return last_five


def date_form(date_str):
    date_object = datetime.strptime(date_str, '%Y-%m-%d')

    return date_object.strftime('%d.%m.%Y')


def anonimus(number):
    if 'Счет' in number:
        anon_number = number[:5] + '**' + number[-4:]

    elif 'none' in number:
        return 'none'

    else:
        anon_number = number[:-16] + number[-16:-12] + ' ' + number[-12:-10] + '** **** ' + number[-4:]

    return anon_number

def opirations_form(opiration):
    form_date = date_form(opiration['date'][:10])
    description = opiration['description']
    from_opiration = opiration.get('from', 'none')
    to_opiration = opiration['to']
    amount = opiration['operationAmount']['amount']
    name = opiration['operationAmount']['currency']['name']
    anonim_from = anonimus(from_opiration)
    anonim_to = anonimus(to_opiration)

    return (f'{form_date} {description}\n'
            f'{anonim_from} -> {anonim_to}\n'
            f'{amount} {name}\n')

def prin_operations(five):
    five_list = []
    for fives in five:
        five_list.append(opirations_form(fives))
    return five_list