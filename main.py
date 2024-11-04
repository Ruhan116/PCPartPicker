import sys
from PyQt6 import QtWidgets
from views.login_main import LogInWindow
from views.signup_main import SignUpWindow
from controllers.auth_controller import AuthController
from views.dashboard import LoadDatabase


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setFixedSize(1280, 720)
        

        # Initialize the authentication controller
        self.auth_controller = AuthController()

        # Create the stacked widget for scene management
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Create instances of LogInWindow and SignUpWindow
        self.login_window = LogInWindow(self.stacked_widget, self.auth_controller)
        self.signup_window = SignUpWindow(self.stacked_widget, self.auth_controller)
        self.dashboard = LoadDatabase(self.stacked_widget)

        # Add both screens to the stacked widget
        self.stacked_widget.addWidget(self.login_window)  # Index 0
        self.stacked_widget.addWidget(self.signup_window)  # Index 1
        self.stacked_widget.addWidget(self.dashboard) #Index 2

        # Set the initial screen to the login window
        self.stacked_widget.setCurrentWidget(self.login_window)
        


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
