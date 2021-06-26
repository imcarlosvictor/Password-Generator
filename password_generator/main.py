import sys
from PySide6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Password Generator')
        self.setGeometry(400, 500, 450, 550)
        self.setLayout(qtw.QVBoxLayout())
        self.contents()

        self.show()

    def contents(self):
        """Add all buttons"""

        container = qtw.QWidget()  # Create widget
        container.setLayout(qtw.QGridLayout())

        # ------------------[Widgets]----------------------
        # Display
        display = qtw.QLineEdit()

        # Slider
        pw_length = qtw.QSlider()
        pw_length.setRange(0, 15)
        pw_length.tickInterval()

        # CheckBox
        uppercase = qtw.QCheckBox('Include Uppercase')
        lowercase = qtw.QCheckBox('Include Lowercase')
        numbers = qtw.QCheckBox('Include Numbers')
        symbols = qtw.QCheckBox('Include Symbols')

        # ------------------[Layout]----------------------
        container.layout().addWidget(display, 0, 0, 1, 4)
        container.layout().addWidget(pw_length, 1, 0, 1, 4)
        container.layout().addWidget(uppercase, 2, 0, 1, 4)
        container.layout().addWidget(lowercase, 3, 0, 1, 4)
        container.layout().addWidget(numbers, 4, 0, 1, 4)
        container.layout().addWidget(symbols, 5, 0, 1, 4)

        # Add widget to main widget
        self.layout().addWidget(container)


    def generate_pw(self):
        pass


def main():
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
