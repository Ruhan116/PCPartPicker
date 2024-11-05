from PyQt6 import QtCore, QtGui, QtWidgets

from controllers.auth_controller import AuthController


class Ui_SignUp(object):
    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.resize(1280, 720)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        SignUp.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=SignUp)
        self.centralwidget.setStyleSheet("background-color: rgb(34, 40, 49)")
        self.centralwidget.setObjectName("centralwidget")
        self.login_background = QtWidgets.QWidget(parent=self.centralwidget)
        self.login_background.setGeometry(QtCore.QRect(440, 60, 391, 541))
        self.login_background.setStyleSheet("background-color: rgb(238, 238, 238);\n"
"border-radius: 25px;\ncolor: black;\n"
"")
        self.login_background.setObjectName("login_background")
        self.login_text = QtWidgets.QLabel(parent=self.login_background)
        self.login_text.setGeometry(QtCore.QRect(140, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.login_text.setFont(font)
        self.login_text.setStyleSheet("color: black;\n")
        self.login_text.setObjectName("login_text")
        self.password_input_2 = QtWidgets.QLineEdit(parent=self.login_background)
        self.password_input_2.setGeometry(QtCore.QRect(50, 280, 301, 41))
        self.password_input_2.setStyleSheet("border: 1px solid rgb(0, 173, 181);\n"
"border-radius: 12px;\ncolor: black;")
        self.password_input_2.setObjectName("password_input_2")
        self.password_text_2 = QtWidgets.QLabel(parent=self.login_background)
        self.password_text_2.setGeometry(QtCore.QRect(50, 250, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.password_text_2.setFont(font)
        self.password_text_2.setStyleSheet("color: black;")
        self.password_text_2.setObjectName("password_text_2")
        self.password_input = QtWidgets.QLineEdit(parent=self.login_background)
        self.password_input.setGeometry(QtCore.QRect(50, 370, 301, 41))
        self.password_input.setStyleSheet("border: 1px solid rgb(0, 173, 181);\n"
"border-radius: 12px;\ncolor: black;")
        self.password_input.setObjectName("password_input")
        self.password_text = QtWidgets.QLabel(parent=self.login_background)
        self.password_text.setGeometry(QtCore.QRect(50, 340, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.password_text.setFont(font)
        self.password_text.setStyleSheet("color: black;")
        self.password_text.setObjectName("password_text")
        self.signup_button = QtWidgets.QPushButton(parent=self.login_background)
        self.signup_button.setGeometry(QtCore.QRect(50, 440, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        self.signup_button.setFont(font)
        self.signup_button.setStyleSheet("background-color: rgb(0, 173, 181);\n"
"border-radius: 12px;\n"
"color: rgb(238, 238, 238)\n"
"")
        self.signup_button.setObjectName("signup_button")
        self.email_text = QtWidgets.QLabel(parent=self.login_background)
        self.email_text.setGeometry(QtCore.QRect(50, 80, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.email_text.setFont(font)
        self.email_text.setStyleSheet("color: black;")
        self.email_text.setObjectName("email_text")
        self.username_input_2 = QtWidgets.QLineEdit(parent=self.login_background)
        self.username_input_2.setGeometry(QtCore.QRect(50, 200, 301, 41))
        self.username_input_2.setStyleSheet("border: 1px solid rgb(0, 173, 181);\n"
"border-radius: 12px;\ncolor: black;")
        self.username_input_2.setObjectName("username_input_2")
        self.username_text_2 = QtWidgets.QLabel(parent=self.login_background)
        self.username_text_2.setGeometry(QtCore.QRect(50, 170, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.username_text_2.setFont(font)
        self.username_text_2.setStyleSheet("color: black;")
        self.username_text_2.setObjectName("username_text_2")
        self.email_input = QtWidgets.QLineEdit(parent=self.login_background)
        self.email_input.setGeometry(QtCore.QRect(50, 110, 301, 41))
        self.email_input.setStyleSheet("border: 1px solid rgb(0, 173, 181);\n"
"border-radius: 12px;\ncolor: black;")
        self.email_input.setObjectName("email_input")
        SignUp.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=SignUp)
        self.statusbar.setObjectName("statusbar")
        SignUp.setStatusBar(self.statusbar)

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
                print("Username Entered is " + username)
                email = self.ui.email_input.text()
                print("Email Entered is " + email)
                password = self.ui.password_input.text()
                print("Password Entered is " + password)
                confirm_password = self.ui.password_input_2.text()
                print("Password Re-entered is " + confirm_password)

                # Sign up using AuthController
                if self.auth_controller.sign_up(username, email, password, confirm_password):
                    print("Sign-up successful")
                    # Optionally, navigate back to the login screen upon successful sign-up
                    self.goto_login()
                else:
                    print("Failed to sign up")
                

        def goto_login(self):
                # Switch to the login screen in the stacked widget
                self.stacked_widget.setCurrentWidget(self.stacked_widget.widget(0))  # Assuming login screen is at index 0