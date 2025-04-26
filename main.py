import sys

from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon

from controllers.auth_controller import AuthController
from models.component_selection_manager import \
    ComponentSelectionManager  # Import the manager
from models.Session import Session
from views.case_data import CasePage
from views.choosing_parts_page import ChoosingPartsPage
from views.cpu_cooler_data import CPUCoolerPage
from views.cpu_data import CPUPage
from views.dashboard import LoadDatabase
from views.gpu_data import GPUPage
from views.hdd_data import HDDPage
from views.landing_page import LandingPage
from views.login_main import LogInWindow
from views.mb_data import MBPage
from views.monitor_data import MonitorPage
from views.psu_data import PSUPage
from views.ram_data import RAMPage
from views.signup_main import SignUpWindow
from views.ssd_data import SSDPage


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setFixedSize(1280, 720)
        self.setWindowTitle("PC Part Picker")
        self.setWindowIcon(QIcon("assets/logo.png"))
        # Initialize the ComponentSelectionManager
        self.component_manager = ComponentSelectionManager()

        # Initialize the authentication controller
        self.auth_controller = AuthController()

        # Create the stacked widget for scene management
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Create instances of LogInWindow and SignUpWindow
        self.login_window = LogInWindow(self.stacked_widget, self.auth_controller)
        self.signup_window = SignUpWindow(self.stacked_widget, self.auth_controller)
        self.landing_page = LandingPage(self.stacked_widget)
        self.choosing_parts_page = ChoosingPartsPage(self.stacked_widget, self.component_manager)  # Pass manager
        self.cpu_page = CPUPage(self.stacked_widget, self.component_manager)  # Pass manager
        self.gpu_page = GPUPage(self.stacked_widget, self.component_manager)  # Pass manager
        self.hdd_page = HDDPage(self.stacked_widget, self.component_manager) # Pass manager
        self.mb_page = MBPage(self.stacked_widget, self.component_manager )# Pass manager
        self.psu_page = PSUPage(self.stacked_widget, self.component_manager) # Pass manager
        self.ram_page = RAMPage(self.stacked_widget, self.component_manager) # Pass manager
        self.ssd_page = SSDPage(self.stacked_widget, self.component_manager) # Pass manager
        self.monitor_page = MonitorPage(self.stacked_widget, self.component_manager) # Pass manager
        self.cpu_cooler_page = CPUCoolerPage(self.stacked_widget, self.component_manager) # Pass manager
        self.case_page = CasePage(self.stacked_widget, self.component_manager)
        self.dashboard = LoadDatabase(self.stacked_widget)

        # Add screens to the stacked widget
        self.stacked_widget.addWidget(self.login_window)  # Index 0
        self.stacked_widget.addWidget(self.signup_window)  # Index 1
        self.stacked_widget.addWidget(self.landing_page)   # Index 2
        self.stacked_widget.addWidget(self.choosing_parts_page)  # Index 3
        self.stacked_widget.addWidget(self.cpu_page)  # Index 4
        self.stacked_widget.addWidget(self.gpu_page)  # Index 5
        self.stacked_widget.addWidget(self.hdd_page)  # Index 6
        self.stacked_widget.addWidget(self.mb_page)  # Index 7
        self.stacked_widget.addWidget(self.psu_page)  # Index 8
        self.stacked_widget.addWidget(self.ram_page)  # Index 9
        self.stacked_widget.addWidget(self.ssd_page)  # Index 10
        self.stacked_widget.addWidget(self.dashboard)  # Index 11
        self.stacked_widget.addWidget(self.monitor_page) # Index 12
        self.stacked_widget.addWidget(self.cpu_cooler_page) # Index 13
        self.stacked_widget.addWidget(self.case_page) # Index 14

        # Set the initial screen to the login window
        self.stacked_widget.setCurrentWidget(self.login_window)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    session = Session()
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
