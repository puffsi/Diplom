import PySimpleGUI as sg
import augmentation
import neural_network
import preprocessor
import prediction

layout = [[sg.Button('Выполнить предобработку',enable_events=True, key='-PREPROCESSING-', font='Helvetica 16')],
        [sg.Button('Выполнить аугментацию',enable_events=True, key='-AUGMENTATION-', font='Helvetica 16')],
        [sg.Button('Обучить нейронную сеть',enable_events=True, key='-NEURAL_NETWORK-', font='Helvetica 16')],
        [sg.Button('Выполнить распознавание',enable_events=True, key='-RECOGNIZER-', font='Helvetica 16')],
        [sg.Text('Результат:', size=(25, 1), key='-text-', font='Helvetica 16')]]

window = sg.Window('Система', layout, size=(350,200))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-PREPROCESSING-':
        preprocessor.preprocessor()
    if event == '-AUGMENTATION-':
        augmentation.augmentation()
    if event == '-NEURAL_NETWORK-':
        neural_network.neural_network()
    if event == '-RECOGNIZER-':
        prediction.prediction()
window.close()