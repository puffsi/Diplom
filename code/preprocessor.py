from delete_background import delete_background
from face_remove import face_remove
import PySimpleGUI as sg

def preprocessor ():
    # обрабатываем нажатие на кнопку
    # что будет внутри окна
    # первым описываем кнопку и сразу указываем размер шрифта
    layout = [
        [sg.Text('Путь к изображению:', size=(50, 1), key='-text-', font='Helvetica 12')],
        [sg.Input(key='-INPUT-')],
        [sg.Text('Куда сохранить:', size=(50, 1), key='-text-', font='Helvetica 12')],
        [sg.Input(key='-OUTPUT-')],
        # затем делаем текст
        [sg.Button('Удалить фон', enable_events=True, key='-DO_BG-', font='Helvetica 16')],
        # затем делаем текст
        [sg.Button('Удалить лицо', enable_events=True, key='-DO_FACE-', font='Helvetica 16')]]
    # рисуем окно
    window = sg.Window('Препроцессор', layout, size=(350, 280))

    # запускаем основной бесконечный цикл
    while True:
        # получаем события, произошедшие в окне
        event, values = window.read()
        # если нажали на крестик
        if event in (sg.WIN_CLOSED, 'Exit'):
            # выходим из цикла
            break
        # если нажали на кнопку
        if event == '-DO_BG-':
            input_path = values['-INPUT-']
            output_path = values['-OUTPUT-']
            print(input_path)
            # запускаем связанную функцию
            delete_background(input_path, output_path)
        if event == '-DO_FACE-':
            input_path = values['-INPUT-']
            output_path = values['-OUTPUT-']
            face_remove(input_path, output_path)

    # закрываем окно и освобождаем используемые ресурсы
    window.close()
    return 0