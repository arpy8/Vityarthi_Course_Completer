import PySimpleGUI as psg


def test_app():
    psg.set_options(font=('Arial Bold', 12))
    psg.theme('DarkBrown4')
    layout = [
        [psg.Text('Select modules')],
        [psg.Checkbox('Module 01', key=0), psg.Checkbox('Module 02', key=1)],
        [psg.Checkbox('Module 03', key=2), psg.Checkbox('Module 04', key=3)],
        [psg.Checkbox('Module 05', key=4), psg.Checkbox('Module 06', key=5)],
        [psg.Checkbox('Module 07', key=6), psg.Checkbox('Module 08', key=7)],
        [psg.Checkbox('Module 09', key=8), psg.Checkbox('Module 10', key=9)],
        [psg.Checkbox('Module 11', key=10), psg.Checkbox('Module 12', key=11)],
        [psg.OK(), psg.Cancel()]
    ]

    window = psg.Window('Vityarthi_Crack', layout, icon="logo.ico")
    event, values = window.read()
    response = values
    modules_selected = []
    for i in range(12):
        if response[i]:
            modules_selected.append(i)
    window.close()
    return modules_selected

