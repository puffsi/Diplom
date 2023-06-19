from predictor import predictior
import PySimpleGUI as sg
def prediction():
# обрабатываем нажатие на кнопку
    # что будет внутри окна
    # первым описываем кнопку и сразу указываем размер шрифта
    layout = [
        [sg.Text('Путь к изображению:', size=(50, 1), key='-text-', font='Helvetica 12')],
        [sg.Input(key='-INPUT-')],
        [sg.Text('Путь к нейронной сети:', size=(50, 1), key='-text-', font='Helvetica 12')],
        [sg.Input(key='-INPUT1-')],
        # затем делаем текст
        [sg.Button('Выполнить распознавание', enable_events=True, key='-DO_RG-', font='Helvetica 12')],
        [sg.Text('Распределение по стилям (office, everyday, sport, party):', size=(50, 1), key='-text-', font='Helvetica 12')],
        [sg.Text('', size=(60, 1), key='-text2-', font='Helvetica 12')]]

    # рисуем окно
    window = sg.Window('Распознаватель', layout, size=(700, 300))

    # запускаем основной бесконечный цикл
    while True:
        # получаем события, произошедшие в окне
        event, values = window.read()
        # если нажали на крестик
        if event in (sg.WIN_CLOSED, 'Exit'):
            # выходим из цикла
            break
        # если нажали на кнопку
        if event == '-DO_RG-':
            img_path = values['-INPUT-']
            model_adr = values['-INPUT1-']
            guess = predictior(img_path, model_adr)
            text_elem = window['-text2-']
            text_elem.update(" {}".format(guess))

    # закрываем окно и освобождаем используемые ресурсы
    window.close()
    return 0