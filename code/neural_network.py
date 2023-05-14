from learning import learning
from testing import test
import PySimpleGUI as sg
def neural_network ():
  # обрабатываем нажатие на кнопку
  # что будет внутри окна
  # первым описываем кнопку и сразу указываем размер шрифта
  layout = [
    [sg.Input(key='-INPUT_TR-')],
    [sg.Input(key='-INPUT_VL-')],
    [sg.Input(key='-OUTPUT-')],
    # затем делаем текст
    [sg.Button('Обучить нейронную сеть', enable_events=True, key='-DO_LEARN-', font='Helvetica 16')],
    [sg.Text('Результат:', size=(20, 1), key='-text-', font='Helvetica 16')],

    [sg.Input(key='-INPUT_TS-')],
    [sg.Input(key='-INPUT_M-')],
    # затем делаем текст
    [sg.Button('Протестировать нейронную сеть', enable_events=True, key='-DO_TEST-', font='Helvetica 16')],
    [sg.Text('Результат:', size=(50, 1), key='-text1-', font='Helvetica 12')]]
  # рисуем окно
  window = sg.Window('Нейронная сеть', layout, size=(450, 350))

  # запускаем основной бесконечный цикл
  while True:
    # получаем события, произошедшие в окне
    event, values = window.read()
    # если нажали на крестик
    if event in (sg.WIN_CLOSED, 'Exit'):
      # выходим из цикла
      break
    # если нажали на кнопку
    if event == '-DO_LEARN-':
      train_dir = values['-INPUT_TR-']
      val_dir = values['-INPUT_VL-']
      where_to_save = values['-OUTPUT-']
      # запускаем связанную функцию
      learning (train_dir, val_dir, where_to_save)
      text_elem = window['-text-']
      text_elem.update("Результат: Обучение завершено.")

    if event == '-DO_TEST-':
      test_dir = values['-INPUT_TS-']
      model_adr = values['-INPUT_M-']
      str = test(test_dir, model_adr)
      text_elem = window['-text1-']
      text_elem.update("Результат: {}.".format(str))

  # закрываем окно и освобождаем используемые ресурсы
  window.close()

  return 0