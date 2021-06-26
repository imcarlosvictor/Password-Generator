import sys
from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Qt


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(300, 500, 400, 450)
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
        display.font().setPointSize(32)
        display.setPlaceholderText("password")

        # Slider
        pw_length = qtw.QSlider(Qt.Horizontal)
        pw_length.setRange(0, 15)
        pw_length.tickInterval()

        # CheckBox
        chkbox_uppercase = qtw.QCheckBox()
        chkbox_lowercase = qtw.QCheckBox()
        chkbox_numbers = qtw.QCheckBox()
        chkbox_symbols = qtw.QCheckBox()

        # Labels
        lbl_uppercase = qtw.QLabel("Include Uppercase")
        lbl_lowercase = qtw.QLabel("Include Lowercase")
        lbl_numbers = qtw.QLabel("Include Numbers")
        lbl_symbols = qtw.QLabel("Include Symbols")

        # Buddy
        lbl_uppercase.setBuddy(chkbox_uppercase)
        lbl_lowercase.setBuddy(chkbox_lowercase)
        lbl_numbers.setBuddy(chkbox_numbers)
        lbl_symbols.setBuddy(chkbox_symbols)

        # Button
        btn_generate = qtw.QPushButton(
            "Create Password", clicked=lambda: self.generate_pw()
        )

        # ------------------[Layout]----------------------
        container.layout().addWidget(display, 0, 0, 1, 4)
        container.layout().addWidget(pw_length, 1, 0, 1, 4)

        container.layout().addWidget(lbl_uppercase, 2, 0, 1, 3)
        container.layout().addWidget(chkbox_uppercase, 2, 4)

        container.layout().addWidget(lbl_lowercase, 3, 0, 1, 3)
        container.layout().addWidget(chkbox_lowercase, 3, 4)

        container.layout().addWidget(lbl_numbers, 4, 0, 1, 3)
        container.layout().addWidget(chkbox_numbers, 4, 4)

        container.layout().addWidget(lbl_symbols, 5, 0, 1, 3)
        container.layout().addWidget(chkbox_symbols, 5, 4)

        container.layout().addWidget(btn_generate, 6, 0, 1, 3)

        # Add widget to main widget
        self.layout().addWidget(container)

    def generate_pw(self):
        pass


def main():
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
