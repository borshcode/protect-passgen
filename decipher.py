# This is decipher v. 0.1
from random import choice, randint


data = input().split(' ')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
           'w', 'x', 'y', 'z']

def encipher(input_data: list):
    result = ''
    i = 0
    for letter in input_data:
        i = 0
        for l in letters:
            if l == letter.lower():
                break
            else:
                i += 1
        if len(str(i+1)) == 1:
            result += '1'
            if letters[i].upper() == letter:
                result += '0'
            result += str(i+1)
        else:
            result += '2'
            if letters[i].upper() == letter:
                result += '0'
            result += str(i+1)
    return result


def decipher(input_data: list):
    input_data_int = []
    for data in input_data:
        input_data_int.append(int(data))

    result = ''
    symbol = ''

    id_num = 0
    nil = False
    i = 0

    while  True:
        try:
            i = id_num+1
            if input_data_int[id_num+1] == 0:
                i = id_num+2
                nil = True

            if input_data_int[id_num] == 1:
                symbol = letters[input_data_int[i] - 1]
                id_num = i + 1
            elif input_data_int[id_num] == 2:
                num = input_data[i] + input_data[i+1]
                symbol = letters[int(num) - 1]
                id_num = i + 2
            if nil:
                symbol = symbol.upper()
                nil = False
            result += symbol
        except IndexError:
            break
    return result


def pass_gen(count: int = 8):
    result = ''
    for i in range(count):
        symbol = choice(letters)
        up = randint(0, 1)

        if up:
            symbol = symbol.upper()
        
        result += symbol
    result += f'\n{encipher(result)}'
    
    return result



if data[0] == 'decipher':
    print(decipher(data[1]))
elif data[0] == 'encipher':
    print(encipher(data[1]))
elif data[0] == 'passgen':
    print(pass_gen(int(data[1])))
else:
    print('Данной команды не существует!')