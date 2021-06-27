import sys
import string
import random

from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6 import QtCore


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(400, 500, 400, 500)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.contents()

        self.pw_params = ""

        self.show()

    def contents(self):
        """Add all buttons"""

        container = QtWidgets.QWidget()  # Create widget
        container.setLayout(QtWidgets.QGridLayout())

        # ------------------[Widgets]----------------------
        # Display
        self.display = QtWidgets.QLineEdit()
        self.display.font().setPointSize(32)
        self.display.setPlaceholderText("password")

        # Slider
        self.sld_pw_length = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.sld_pw_length.setValue(4)
        self.sld_pw_length.setRange(4, 16)
        self.sld_pw_length.setTickInterval(4)
        self.sld_pw_length.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sld_pw_length.setSingleStep(1)

        # Displaying Slider value
        self.sld_value = self.sld_pw_length.sliderPosition()
        self.sld_pw_length_val = QtWidgets.QLabel()
        QtCore.QObject.connect(
            self.sld_pw_length,
            QtCore.SIGNAL("valueChanged(int)"),
            self.update_slider_value,
        )

        # CheckBox
        self.chkbox_uppercase = QtWidgets.QCheckBox()
        self.chkbox_lowercase = QtWidgets.QCheckBox()
        self.chkbox_numbers = QtWidgets.QCheckBox()
        self.chkbox_symbols = QtWidgets.QCheckBox()

        # Labels
        lbl_length = QtWidgets.QLabel("Length:")
        lbl_min_length = QtWidgets.QLabel("4")
        lbl_max_length = QtWidgets.QLabel("16")
        lbl_uppercase = QtWidgets.QLabel("Include Uppercase")
        lbl_lowercase = QtWidgets.QLabel("Include Lowercase")
        lbl_numbers = QtWidgets.QLabel("Include Numbers")
        lbl_symbols = QtWidgets.QLabel("Include Symbols")

        # Buddy
        lbl_uppercase.setBuddy(self.chkbox_uppercase)
        lbl_lowercase.setBuddy(self.chkbox_lowercase)
        lbl_numbers.setBuddy(self.chkbox_numbers)
        lbl_symbols.setBuddy(self.chkbox_symbols)

        # Button
        btn_generate = QtWidgets.QPushButton(
            "Generate Password", clicked=lambda: self.generate_pw()
        )

        # ------------------[Layout]----------------------
        container.layout().addWidget(self.display, 0, 0, 1, 5)

        container.layout().addWidget(lbl_length, 1, 0, 1, 2)
        container.layout().addWidget(self.sld_pw_length_val, 1, 3)

        container.layout().addWidget(lbl_min_length, 2, 0)
        container.layout().addWidget(self.sld_pw_length, 2, 1, 1, 4)
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

    def update_slider_value(self):
        """Updates the value of the slider everytime it's moved."""

        self.sld_pw_length_val.setText(str(self.sld_value))

    def generate_pw(self):
        """Generates a password that satisfies the user's criteria."""

        if self.chkbox_uppercase.isChecked():
            self.pw_params += string.ascii_uppercase

        if self.chkbox_lowercase.isChecked():
            self.pw_params += string.ascii_lowercase

        if self.chkbox_numbers.isChecked():
            self.pw_params += string.digits

        if self.chkbox_symbols.isChecked():
            self.pw_params += string.punctuation

        # Create a password from the parameters
        # randrange
        password = random.sample(self.pw_params, 8)
        password = ''.join(password)

        # Display password
        self.display.setText(password)


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
