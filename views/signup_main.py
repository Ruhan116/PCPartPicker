from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import re

from controllers.auth_controller import AuthController

class Ui_SignUp(object):
    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.resize(1280, 720)
        
        # Set the font for the whole window
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        SignUp.setFont(font)

        # Create the central widget and set background color
        self.centralwidget = QtWidgets.QWidget(parent=SignUp)
        self.centralwidget.setStyleSheet("background-color: rgb(34, 40, 49)")
        self.centralwidget.setObjectName("centralwidget")

        # Create the login background widget with rounded corners
        self.login_background = QtWidgets.QWidget(parent=self.centralwidget)
        self.login_background.setGeometry(QtCore.QRect(440, 60, 391, 541))
        self.login_background.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                             "border-radius: 25px;\ncolor: black;")
        self.login_background.setObjectName("login_background")

        # Title text for the sign-up window
        self.login_text = QtWidgets.QLabel(parent=self.login_background)
        self.login_text.setGeometry(QtCore.QRect(140, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(24)
        self.login_text.setFont(font)
        self.login_text.setStyleSheet("color: black;")
        self.login_text.setObjectName("login_text")

        # Email label and input field
        self.email_text = QtWidgets.QLabel(parent=self.login_background)
        self.email_text.setGeometry(QtCore.QRect(50, 80, 101, 21))
        font.setPointSize(18)
        self.email_text.setFont(font)
        self.email_text.setStyleSheet("color: black;")
        self.email_text.setObjectName("email_text")

        self.email_input = QtWidgets.QLineEdit(parent=self.login_background)
        self.email_input.setGeometry(QtCore.QRect(50, 110, 301, 41))
        self.email_input.setStyleSheet("border: 1px solid rgb(0, 173, 181);\n"
                                       "border-radius: 12px;\ncolor: black;")
        self.email_input.setObjectName("email_input")

        # Username label and input field
        self.username_text_2 = QtWidgets.QLabel(parent=self.login_background)
        self.username_text_2.setGeometry(QtCore.QRect(50, 170, 101, 21))
        self.username_text_2.setFont(font)
        self.username_text_2.setStyleSheet("color: black;")
        self.username_text_2.setObjectName("username_text_2")

        self.username_input_2 = QtWidgets.QLineEdit(parent=self.login_background)
        self.username_input_2.setGeometry(QtCore.QRect(50, 200, 301, 41))
        self.username_input_2.setStyleSheet("border: 1px solid rgb(0, 173, 181);\n"
                                            "border-radius: 12px;\ncolor: black;")
        self.username_input_2.setObjectName("username_input_2")

        # Password label and input field (masked)
        self.password_text_2 = QtWidgets.QLabel(parent=self.login_background)
        self.password_text_2.setGeometry(QtCore.QRect(50, 250, 101, 21))
        self.password_text_2.setFont(font)
        self.password_text_2.setStyleSheet("color: black;")
        self.password_text_2.setObjectName("password_text_2")

        self.password_input_2 = QtWidgets.QLineEdit(parent=self.login_background)
        self.password_input_2.setGeometry(QtCore.QRect(50, 280, 301, 41))
        self.password_input_2.setStyleSheet("border: 1px solid rgb(0, 173, 181);\n"
                                            "border-radius: 12px;\ncolor: black;")
        self.password_input_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Mask input
        self.password_input_2.setObjectName("password_input_2")

        # Confirm Password label and input field (masked)
        self.password_text = QtWidgets.QLabel(parent=self.login_background)
        self.password_text.setGeometry(QtCore.QRect(50, 340, 231, 21))
        self.password_text.setFont(font)
        self.password_text.setStyleSheet("color: black;")
        self.password_text.setObjectName("password_text")

        self.password_input = QtWidgets.QLineEdit(parent=self.login_background)
        self.password_input.setGeometry(QtCore.QRect(50, 370, 301, 41))
        self.password_input.setStyleSheet("border: 1px solid rgb(0, 173, 181);\n"
                                          "border-radius: 12px;\ncolor: black;")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Mask input
        self.password_input.setObjectName("password_input")

        # Validation message box (red text)
        self.message_box = QtWidgets.QLabel(parent=self.login_background)
        self.message_box.setGeometry(QtCore.QRect(50, 420, 301, 31))
        self.message_box.setStyleSheet("color: red; text-align: center;")
        self.message_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.message_box.setObjectName("message_box")
        self.message_box.setText("")  # Initially empty

        # Sign Up button
        self.signup_button = QtWidgets.QPushButton(parent=self.login_background)
        self.signup_button.setGeometry(QtCore.QRect(50, 480, 301, 41))
        self.signup_button.setFont(QtGui.QFont("Calibri Light", 12))
        self.signup_button.setStyleSheet("background-color: rgb(0, 173, 181);\n"
                                         "border-radius: 12px;\n"
                                         "color: rgb(238, 238, 238)\n")
        self.signup_button.setObjectName("signup_button")

        # Set the central widget and status bar
        SignUp.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=SignUp)
        self.statusbar.setObjectName("statusbar")
        SignUp.setStatusBar(self.statusbar)

        # Translation for labels
        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "MainWindow"))
        self.login_text.setText(_translate("SignUp", "Sign Up"))
        self.password_text_2.setText(_translate("SignUp", "Password"))
        self.password_text.setText(_translate("SignUp", "Confirm Password"))
        self.signup_button.setText(_translate("SignUp", "Sign Up"))
        self.email_text.setText(_translate("SignUp", "Email"))
        self.username_text_2.setText(_translate("SignUp", "Username"))



class SignUpWindow(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget, auth_controller):
        super(SignUpWindow, self).__init__()
        self.ui = Ui_SignUp()
        self.ui.setupUi(self)

        # Store references to the stacked widget and auth controller
        self.stacked_widget = stacked_widget
        self.auth_controller = AuthController()

        # Connect the sign-up button to the handle_signup method
        self.ui.signup_button.clicked.connect(self.handle_signup)

    def handle_signup(self):
        username = self.ui.username_input_2.text()
        email = self.ui.email_input.text()
        password = self.ui.password_input.text()
        confirm_password = self.ui.password_input_2.text()

        # Validate email format
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        if not re.match(email_pattern, email):
                QMessageBox.warning(self, "Invalid Email", "Please enter a valid email in the format xxxx@xxxx.com.")
                return  # Exit the method to allow the user to reenter details

        # Validate password length
        if len(password) < 8:
                QMessageBox.warning(self, "Weak Password", "Password must be at least 8 characters long.")
                return

        # Check if passwords match
        if password != confirm_password:
                QMessageBox.warning(self, "Password Mismatch", "Passwords do not match. Please reenter them.")
                return

        # Attempt sign-up using AuthController
        if self.auth_controller.sign_up(username, email, password, confirm_password):
                QMessageBox.information(self, "Success", "Sign-up successful!")
                self.goto_login()  # Optionally, navigate to the login screen
        else:
                QMessageBox.critical(self, "Failure", "Failed to sign up. Username or email may already exist.")


    def goto_login(self):
        # Switch to the login screen in the stacked widget
        self.stacked_widget.setCurrentWidget(self.stacked_widget.widget(0))  # Assuming login screen is at index 0
