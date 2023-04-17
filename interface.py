import PySimpleGUI as psg


class App:

    def main_app(self):
        psg.set_options(font=('Arial Bold', 12))
        psg.theme('DarkBlack')
        layout = [
            [psg.Text('Select course')],
            [psg.Radio("Python Essentials", "gen", key='C1')],
            [psg.Radio("Fundamentals of AI and ML", "gen", key='C2')],
            [psg.Text('Select modules')],
            [psg.Checkbox('Module 01', key=0), psg.Checkbox('Module 02', key=1)],
            [psg.Checkbox('Module 03', key=2), psg.Checkbox('Module 04', key=3)],
            [psg.Checkbox('Module 05', key=4), psg.Checkbox('Module 06', key=5)],
            [psg.Checkbox('Module 07', key=6), psg.Checkbox('Module 08', key=7)],
            [psg.Checkbox('Module 09', key=8), psg.Checkbox('Module 10', key=9)],
            [psg.Checkbox('Module 11', key=10), psg.Checkbox('Module 12', key=11)],
            [psg.OK(), psg.Cancel()]
        ]

        window = psg.Window('crack', layout, icon="assets/logo.ico")
        event, values = window.read()
        response = values
        modules_selected = []
        course_selected = 0
        for i in range(12):
            try:
                if response[f"C{i}"]:
                    course_selected = i
            except KeyError:
                pass

            if response[i]:
                modules_selected.append(i)

        package = [course_selected, modules_selected]
        window.close()
        return package

