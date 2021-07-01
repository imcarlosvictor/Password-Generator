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
        self.setGeometry(3000, 500, 400, 500)
        self.setLayout(QtWidgets.QVBoxLayout())
        # self.layout().setContentsMargins(0, 0, 0, 0)

        # Add Contents
        self.add_display()
        self.add_slider()
        self.add_checkboxes()
        self.add_button()

        self.pw_params = ""

        self.show()

    def add_display(self):
        """Creates display."""

        container = QtWidgets.QWidget()
        container.setLayout(QtWidgets.QHBoxLayout())
        container.layout().setContentsMargins(0, 0, 0, 0)

        # Display
        self.display = QtWidgets.QLineEdit()
        self.display.font().setPointSize(32)
        self.display.setPlaceholderText("password")

        container.layout().addWidget(self.display)

        self.layout().addWidget(container)

    def add_slider(self):
        """Creates slider"""

        container = QtWidgets.QWidget()
        container.setLayout(QtWidgets.QHBoxLayout())
        container.layout().setContentsMargins(0, 0, 0, 0)

        # Slider
        self.sld_pw_length = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.sld_pw_length.setValue(0)
        self.sld_pw_length.setRange(0, 16)
        self.sld_pw_length.setTickInterval(4)
        self.sld_pw_length.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sld_pw_length.setSingleStep(1)

        # Displaying Slider value
        self.sld_pw_length.valueChanged.connect(self.update_slider_value)

        # Labels
        lbl_minimum = QtWidgets.QLabel('0')
        lbl_maximum = QtWidgets.QLabel('16')

        container.layout().addWidget(lbl_minimum)
        container.layout().addWidget(self.sld_pw_length)
        container.layout().addWidget(lbl_maximum)

        self.layout().addWidget(container)

    def add_checkboxes(self):
        """Add all buttons"""

        container = QtWidgets.QWidget()  # Create widget
        container.setLayout(QtWidgets.QGridLayout())

        # ------------------[Widgets]----------------------
        # CheckBox
        self.chkbox_uppercase = QtWidgets.QCheckBox()
        self.chkbox_lowercase = QtWidgets.QCheckBox()
        self.chkbox_numbers = QtWidgets.QCheckBox()
        self.chkbox_symbols = QtWidgets.QCheckBox()

        # Labels
        lbl_length = QtWidgets.QLabel("Password length:")
        self.sld_pw_length_val = QtWidgets.QLabel('')
        lbl_uppercase = QtWidgets.QLabel("Include Uppercase")
        lbl_lowercase = QtWidgets.QLabel("Include Lowercase")
        lbl_numbers = QtWidgets.QLabel("Include Numbers")
        lbl_symbols = QtWidgets.QLabel("Include Symbols")

        # Buddy
        lbl_uppercase.setBuddy(self.chkbox_uppercase)
        lbl_lowercase.setBuddy(self.chkbox_lowercase)
        lbl_numbers.setBuddy(self.chkbox_numbers)
        lbl_symbols.setBuddy(self.chkbox_symbols)

        # ------------------[Layout]----------------------
        container.layout().addWidget(lbl_length, 0, 0, 1, 3)
        container.layout().addWidget(self.sld_pw_length_val, 0, 5)

        container.layout().addWidget(lbl_uppercase, 1, 0, 1, 3)
        container.layout().addWidget(self.chkbox_uppercase, 1, 5)

        container.layout().addWidget(lbl_lowercase, 2, 0, 1, 3)
        container.layout().addWidget(self.chkbox_lowercase, 2, 5)

        container.layout().addWidget(lbl_numbers, 3, 0, 1, 3)
        container.layout().addWidget(self.chkbox_numbers, 3, 5)

        container.layout().addWidget(lbl_symbols, 4, 0, 1, 3)
        container.layout().addWidget(self.chkbox_symbols, 4, 5)

        # Add widget to main widget
        self.layout().addWidget(container)

    def add_button(self):
        """Adds button."""
 
        container = QtWidgets.QWidget()
        container.setLayout(QtWidgets.QHBoxLayout())

        # Button
        btn_generate_pw = QtWidgets.QPushButton(
            "Generate Password", clicked=lambda: self.generate_password()
        )

        container.layout().addWidget(btn_generate_pw)

        self.layout().addWidget(container)

    def update_slider_value(self):
        """Updates the value of the slider everytime it's moved."""

        self.sld_value = self.sld_pw_length.value()
        self.sld_pw_length_val.setText(str(self.sld_value))

    def generate_password(self):
        """Generates a password that satisfies the user's criteria."""

        if self.chkbox_uppercase.isChecked():
            self.pw_params += string.ascii_uppercase

        if self.chkbox_lowercase.isChecked():
            self.pw_params += string.ascii_lowercase

        if self.chkbox_numbers.isChecked():
            self.pw_params += string.digits

        if self.chkbox_symbols.isChecked():
            self.pw_params += string.punctuation

        try:
            # Create a password from the parameters
            password = random.sample(self.pw_params, self.sld_value)
            password = "".join(password)

            # Display password
            self.display.setText(password)
        except AttributeError:
            self.display.setText('Password length required.')
        except ValueError:
            self.display.setText('Enter parameters for password.')

        # Reset parameters
        self.pw_params = ''


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
