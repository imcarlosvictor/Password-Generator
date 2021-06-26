import sys
import string
import random

from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Qt


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(400, 500, 400, 500)
        self.setLayout(qtw.QVBoxLayout())
        self.contents()

        self.pw_params = ''

        self.show()

    def contents(self):
        """Add all buttons"""

        container = qtw.QWidget()  # Create widget
        container.setLayout(qtw.QGridLayout())

        # ------------------[Widgets]----------------------
        # Display
        self.display = qtw.QLineEdit()
        self.display.font().setPointSize(32)
        self.display.setPlaceholderText("password")

        # Slider
        self.sldr_pw_length = qtw.QSlider(Qt.Horizontal)
        self.sldr_pw_length.setValue(10)
        self.sldr_pw_length.setRange(4, 16)
        self.sldr_pw_length.setTickInterval(4)
        self.sldr_pw_length.setSingleStep(1)
        self.sldr_pw_length.setTickPosition(qtw.QSlider.TicksBelow)

        lbl_length = qtw.QLabel('Length:')
        self.sldr_pw_length_val = qtw.QLabel()
        lbl_min_length = qtw.QLabel('4')
        lbl_max_length = qtw.QLabel('16')

        # CheckBox
        self.chkbox_uppercase = qtw.QCheckBox()
        self.chkbox_lowercase = qtw.QCheckBox()
        self.chkbox_numbers = qtw.QCheckBox()
        self.chkbox_symbols = qtw.QCheckBox()

        # Labels
        lbl_uppercase = qtw.QLabel("Include Uppercase")
        lbl_lowercase = qtw.QLabel("Include Lowercase")
        lbl_numbers = qtw.QLabel("Include Numbers")
        lbl_symbols = qtw.QLabel("Include Symbols")

        # Buddy
        lbl_uppercase.setBuddy(self.chkbox_uppercase)
        lbl_lowercase.setBuddy(self.chkbox_lowercase)
        lbl_numbers.setBuddy(self.chkbox_numbers)
        lbl_symbols.setBuddy(self.chkbox_symbols)

        # Button
        btn_generate = qtw.QPushButton(
            "Create Password", clicked=lambda: self.generate_pw()
        )

        # ------------------[Layout]----------------------
        container.layout().addWidget(self.display, 0, 0, 1, 5)

        container.layout().addWidget(lbl_length, 1, 0)
        container.layout().addWidget(self.sldr_pw_length_val, 1, 2)

        container.layout().addWidget(lbl_min_length, 2, 0)
        container.layout().addWidget(self.sldr_pw_length, 2, 1, 1, 4)
        container.layout().addWidget(lbl_max_length, 2, 5)

        container.layout().addWidget(lbl_uppercase, 3, 0, 1, 3)
        container.layout().addWidget(self.chkbox_uppercase, 3, 5)

        container.layout().addWidget(lbl_lowercase, 4, 0, 1, 3)
        container.layout().addWidget(self.chkbox_lowercase, 4, 5)

        container.layout().addWidget(lbl_numbers, 5, 0, 1, 3)
        container.layout().addWidget(self.chkbox_numbers, 5, 5)

        container.layout().addWidget(lbl_symbols, 6, 0, 1, 3)
        container.layout().addWidget(self.chkbox_symbols, 6, 5)

        container.layout().addWidget(btn_generate, 7, 0, 1, 5)

        # Add widget to main widget
        self.layout().addWidget(container)

    def generate_pw(self):
        """Generates a password that satisfies the user's criteria."""

        if self.chkbox_uppercase.isChecked():
            self.pw_params += string.ascii_uppercase

        if self.chkbox_lowercase.isChecked():
            self.pw_params += string.ascii_lowercase

        if self.chkbox_digits.isChecked():
            self.pw_params += string.digits

        if self.chkbox_symbols.isChecked():
            self.pw_params += string.punctuation

        # Create a password from the parameters
        # randrange
        password = random.randrange(self.pw_length.value())




def main():
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
