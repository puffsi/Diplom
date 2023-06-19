import cv2
from horizontal_flip import horizontal_flip
from color_change import color_change
import PySimpleGUI as sg

def augmentation():
    # обрабатываем нажатие на кнопку
    # что будет внутри окна
    # первым описываем кнопку и сразу указываем размер шрифта
    layout = [
        [sg.Text('Путь к изображению:', size=(50, 1), key='-text-', font='Helvetica 12')],
        [sg.Input(key='-INPUT-')],
        [sg.Text('Куда сохранить:', size=(50, 1), key='-text-', font='Helvetica 12')],
        [sg.Input(key='-OUTPUT-')],
        # затем делаем текст
        [sg.Button('Отразить по горизотали', enable_events=True, key='-DO_FLIP-', font='Helvetica 16')],
        [sg.Text('Параметры цветовых характеристик:', size=(50, 1), key='-text-', font='Helvetica 12')],
        [sg.Text('Яркость (от 0 до 1):', size=(50, 1), key='-text-', font='Helvetica 12')],
        [sg.Input(key='-INPUTB-')],
        [sg.Text('Констраст (от 0 до 1):', size=(50, 1), key='-text-', font='Helvetica 12')],
        [sg.Input(key='-INPUTC-')],
        [sg.Text('Насыщеность (от 0 до 1):', size=(50, 1), key='-text-', font='Helvetica 12')],
        [sg.Input(key='-INPUTS-')],
        [sg.Text('Оттенок: (от 0 до 0.5):', size=(50, 1), key='-text-', font='Helvetica 12')],
        [sg.Input(key='-INPUTH-')],
        # затем делаем текст
        [sg.Button('Изменить цветовые хар-ки', enable_events=True, key='-DO_COLOUR-', font='Helvetica 16')]]
    # рисуем окно
    window = sg.Window('Аугментатор', layout, size=(350, 500))

    # запускаем основной бесконечный цикл
    while True:
        # получаем события, произошедшие в окне
        event, values = window.read()
        # если нажали на крестик
        if event in (sg.WIN_CLOSED, 'Exit'):
            # выходим из цикла
            break
        # если нажали на кнопку
        if event == '-DO_FLIP-':
            input_path = values['-INPUT-']
            output_path = values['-OUTPUT-']
            print(input_path)
            # запускаем связанную функцию
            horizontal_flip(input_path, output_path)
        if event == '-DO_COLOUR-':
            input_path = values['-INPUT-']
            b = values ['-INPUTB-']
            c = values ['-INPUTC-']
            s = values ['-INPUTS-']
            h = values ['-INPUTH-']
            output_path = values['-OUTPUT-']
            color_change(input_path, output_path, b,c,s,h)

    # закрываем окно и освобождаем используемые ресурсы
    window.close()
    return 0