from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_LogIn(object):
    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(1280, 720)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        LogIn.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=LogIn)
        self.centralwidget.setStyleSheet("background-color: rgb(34, 40, 49)")
        self.centralwidget.setObjectName("centralwidget")
        self.login_background = QtWidgets.QWidget(parent=self.centralwidget)
        self.login_background.setGeometry(QtCore.QRect(440, 120, 391, 481))
        self.login_background.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                             "border-radius: 25px;\n")
        self.login_background.setObjectName("login_background")
        
        self.login_text = QtWidgets.QLabel(parent=self.login_background)
        self.login_text.setGeometry(QtCore.QRect(160, 60, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(24)
        self.login_text.setFont(font)
        self.login_text.setStyleSheet("color: black;\nfont-weight: bold;")
        self.login_text.setObjectName("login_text")

        self.username_input = QtWidgets.QLineEdit(parent=self.login_background)
        self.username_input.setGeometry(QtCore.QRect(50, 170, 301, 41))
        self.username_input.setStyleSheet("border: 1px solid rgb(0, 173, 181);\n"
                                          "border-radius: 12px;\ncolor: black;")
        self.username_input.setObjectName("username_input")

        self.username_text = QtWidgets.QLabel(parent=self.login_background)
        self.username_text.setGeometry(QtCore.QRect(50, 140, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(18)
        self.username_text.setFont(font)
        self.username_text.setStyleSheet("color: black;")
        self.username_text.setObjectName("username_text")

        self.password_input = QtWidgets.QLineEdit(parent=self.login_background)
        self.password_input.setGeometry(QtCore.QRect(50, 260, 301, 41))
        self.password_input.setStyleSheet("border: 1px solid rgb(0, 173, 181);\n"
                                          "border-radius: 12px;\ncolor: black;")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # This makes the password characters masked
        self.password_input.setObjectName("password_input")

        self.password_text = QtWidgets.QLabel(parent=self.login_background)
        self.password_text.setGeometry(QtCore.QRect(50, 230, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(18)
        self.password_text.setFont(font)
        self.password_text.setStyleSheet("color: black;")
        self.password_text.setObjectName("password_text")

        self.login_button = QtWidgets.QPushButton(parent=self.login_background)
        self.login_button.setGeometry(QtCore.QRect(50, 320, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(13)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("background-color: rgb(0, 173, 181);\n"
                                        "border-radius: 12px;\ncolor: rgb(238, 238, 238)\n")
        self.login_button.setObjectName("login_button")

        self.member_verif_text = QtWidgets.QLabel(parent=self.login_background)
        self.member_verif_text.setGeometry(QtCore.QRect(60, 370, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        self.member_verif_text.setFont(font)
        self.member_verif_text.setStyleSheet("color: black;")
        self.member_verif_text.setObjectName("member_verif_text")

        self.signup_button = QtWidgets.QPushButton(parent=self.login_background)
        self.signup_button.setGeometry(QtCore.QRect(290, 370, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        self.signup_button.setFont(font)
        self.signup_button.setStyleSheet("background-color: transparent;\n"
                                         "color: rgb(0, 173, 181);\n")
        self.signup_button.setObjectName("signup_button")

        LogIn.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=LogIn)
        self.statusbar.setObjectName("statusbar")
        LogIn.setStatusBar(self.statusbar)

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "MainWindow"))
        self.login_text.setText(_translate("LogIn", "Log In"))
        self.username_text.setText(_translate("LogIn", "Username"))
        self.password_text.setText(_translate("LogIn", "Password"))
        self.login_button.setText(_translate("LogIn", "Login"))
        self.member_verif_text.setText(_translate("LogIn", "Not a member?"))
        self.signup_button.setText(_translate("LogIn", "Sign Up"))

class LogInWindow(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget, auth_controller):
        super(LogInWindow, self).__init__()
        self.ui = Ui_LogIn()
        self.ui.setupUi(self)

        # Store references to the stacked widget and auth controller
        self.stacked_widget = stacked_widget
        self.auth_controller = auth_controller

        # Connect the buttons to their respective functions
        self.ui.login_button.clicked.connect(self.handle_login)
        self.ui.signup_button.clicked.connect(self.goto_signup)

    def handle_login(self):
        username = self.ui.username_input.text()
        print("Username Entered is " + username)
        password = self.ui.password_input.text()
        print("Password Entered is " + password)

        # Authenticate using AuthController
        if self.auth_controller.login(username, password):
            print("Logged in successfully")
            # Navigate to the main application screen here
            self.goto_dashboard()
        else:
            print("Failed to log in")

    def goto_signup(self):
        # Switch to the sign-up screen in the stacked widget
        self.stacked_widget.setCurrentWidget(self.stacked_widget.widget(1))  # sign-up screen is at index 1
    
    def goto_dashboard(self):
        self.stacked_widget.setCurrentWidget(self.stacked_widget.widget(2))
