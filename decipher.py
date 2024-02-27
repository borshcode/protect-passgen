# This is decipher v. 1.0
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from random import choice, randint
import sys


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
    password = encipher(result)
    
    return password, result


def print_help():
    print('''
python decipher.py [option]
-E Encipher
-D Decipher
--passgen Password Generator
-h Help
--help Help''')
mode = ''

#PyQt5
def decipher_mode():
    global mode
    decipher_mode_btn.setDisabled(True)
    encipher_mode_btn.setEnabled(True)
    passgen_mode_btn.setEnabled(True)
    ok_btn.setEnabled(True)
    code_le.hide()
    mode = 'decipher'


def encipher_mode():
    global mode
    decipher_mode_btn.setEnabled(True)
    encipher_mode_btn.setDisabled(True)
    passgen_mode_btn.setEnabled(True)
    ok_btn.setEnabled(True)
    code_le.hide()
    mode  = 'encipher'


def passgen_mode():
    global mode
    decipher_mode_btn.setEnabled(True)
    encipher_mode_btn.setEnabled(True)
    passgen_mode_btn.setDisabled(True)
    ok_btn.setEnabled(True)
    code_le.show()
    mode = 'passgen'


def ok_handler():
    global mode
    if input_le.text() == '':
        output_le.setText('Введите данные!')
        return
    if mode == 'decipher':
        data = decipher(input_le.text())
        output_le.setText(data)
    elif mode == 'encipher':
        data = encipher(input_le.text())
        output_le.setText(data)
    elif mode == 'passgen':
        password, code = pass_gen(int(input_le.text()))
        code_le.setText(code)
        output_le.setText(password)


app = QApplication([])
main_wdg = QWidget()
main_wdg.setWindowTitle('Passgen v.0.2')
main_wdg.resize(200, 100)

decipher_mode_btn = QPushButton('Decipher')
encipher_mode_btn = QPushButton('Encipher')
passgen_mode_btn = QPushButton('PassGen')

input_le = QLineEdit()
input_le.setPlaceholderText('Input:')

output_le = QLineEdit()
output_le.setPlaceholderText('Output:')
output_le.setReadOnly(True)

code_le = QLineEdit()
code_le.setPlaceholderText('Password:')
code_le.setReadOnly(True)
code_le.hide()

ok_btn = QPushButton('Ok!')
ok_btn.setDisabled(True)

main_line = QHBoxLayout()
v1_line = QVBoxLayout()
v2_line = QVBoxLayout()

v1_line.addWidget(decipher_mode_btn, alignment=Qt.AlignCenter)
v1_line.addWidget(encipher_mode_btn, alignment=Qt.AlignCenter)
v1_line.addWidget(passgen_mode_btn, alignment=Qt.AlignCenter)

v2_line.addWidget(input_le, alignment=Qt.AlignCenter)
v2_line.addWidget(code_le, alignment=Qt.AlignCenter)
v2_line.addWidget(output_le,alignment=Qt.AlignCenter)
v2_line.addWidget(ok_btn, alignment=Qt.AlignCenter)

main_line.addLayout(v1_line)
main_line.addLayout(v2_line)
main_wdg.setLayout(main_line)


decipher_mode_btn.clicked.connect(decipher_mode)
encipher_mode_btn.clicked.connect(encipher_mode)
passgen_mode_btn.clicked.connect(passgen_mode)
ok_btn.clicked.connect(ok_handler)

main_wdg.show()
app.exec_()

