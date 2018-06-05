import toga
from toga.style import Pack
from toga.color import RED, BLUE
from toga.constants import COLUMN, ROW


class ExampleButtonApp(toga.App):
    def startup(self):
        # Window class
        #   Main window of the application with title and size
        self.main_window = toga.MainWindow(title=self.name, size=(500, 200))

        # Common style of the inner boxes
        style_inner_box = Pack(direction=ROW)

        # Button class
        #   Simple button with label and callback function called when
        #   hit the button
        button1 = toga.Button('Change Label', on_press=self.callback_label)

        # Button with label and enable option
        button2 = toga.Button('Disabled', enabled=False)

        # Button with label and style option
        button3 = toga.Button('Bigger', style=Pack(width=200))

        # Button with label and callback function called when
        #   hit the button
        button4 = toga.Button('Resize Window', on_press=self.callback_resize)

        # Box class
        # Container of components
        #   Add components for the first row of the outer box
        inner_box1 = toga.Box(
            style=style_inner_box,
            children=[
                button1,
                button2,
                button3,
                button4
            ]
        )

        # Button with label and margin style
        button5 = toga.Button('Far from home', style=Pack(padding=50))

        # Button with label and RGB color
        button6 = toga.Button('RGB : Fashion', style=Pack(background_color=RED))

        # Button with label and string color
        button7 = toga.Button('String : Fashion', style=Pack(background_color=BLUE))

        # Add components for the second row of the outer box
        inner_box2 = toga.Box(
            style=style_inner_box,
            children=[
                button5,
                button6,
                button7
            ]
        )

        # Button with serif font
        button8 = toga.Button(
            'Serif Font',
            style=Pack(font_family='serif', font_size=12.0)
        )

        button9 = toga.Button(
            'Sans Serif Font',
            style=Pack(font_family='sans-serif', font_size=15.0)
        )

        inner_box3 = toga.Box(
            style=style_inner_box,
            children=[
                button8,
                button9,
            ],
        )

        #  Create the outer box with 2 rows
        outer_box = toga.Box(
            style=Pack(direction=COLUMN, height=10),
            children=[inner_box1, inner_box2, inner_box3]
        )

        # Add the content on the main window
        self.main_window.content = outer_box

        # Show the main window
        self.main_window.show()

    def callback_label(self, button):
        # Some action when you hit the button
        #   In this case the label will change
        button.label = 'Magic!!'

    def callback_resize(self, button):
        # Some action when you hit the button
        #   In this case the window size will change
        self.main_window.size = (100, 100)


def main():
    # Application class
    #   App name and namespace
    app = ExampleButtonApp('Button', 'org.pybee.widgets.buttons')
    return app
