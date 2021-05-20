# pomodoro timer widget package
import PySimpleGUI as sg
import time

# theme
sg.theme('DarkAmber')

# pysimplegui uses nested arrays to position elements absolutely
layout = [
    [sg.Text('timer widget')],
    [sg.Text('', size=(8, 2), font=('Arial', 20),
     justification='center', key='text')],
    [sg.Button('Pause', key='-RUN-PAUSE-', button_color=('white', '#001480')),
     sg.Button('Reset', key='-RESET-', button_color=('white', '#007339')),
     sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]
]

# timer window
window = sg.Window(
    'Running timer',
    layout,
    no_titlebar=True,
    auto_size_buttons=False,
    keep_on_top=True,
    grab_anywhere=True,
    element_padding=(0,0),
    finalize=True,
    element_justification='c',
    right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT
)


# convert time display to integers
def time_to_int():
    return int(round(time.time() * 100))


# timer variables
current_time, paused_time, paused = 0, 0, False
start_time = time_to_int()


# Event loop that listens to events and processes their values
while True:
    # --------- Read and update window ---------
    if not paused:
        event, values = window.read(timeout=10)
        current_time = time_to_int() - start_time
    else:
        event, values = window.read()

    # --------- Do button operations ---------
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-RESET-':
        paused_time = start_time = time_to_int()
        current_time = 0
    elif event == '-RUN-PAUSE-':
        paused = not paused
        if paused:
            paused_time = time_to_int()
        else:
            start_time = start_time + time_to_int() - paused_time

        # update button text based on timer state
        window['-RUN-PAUSE-'].update('Run' if paused else 'Pause')
    elif event == 'Edit me':
        sg.execute_editor(__file__)

    # --------- Timer display ---------
    window['text'].update('{:02d}:{:02d}.{:02d}'.format(
        (current_time // 100) // 60,
        (current_time // 100) % 60,
        current_time % 100
    ))

window.close()