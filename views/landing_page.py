from PyQt6 import QtCore, QtGui, QtWidgets
from controllers.data_controller import DataController
from data.data_loader.Load_Data import PCComponentScraper


class Ui_LandingPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.header_text = QtWidgets.QLabel(self.centralwidget)
        self.header_text.setObjectName("header_text")
        self.header_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.header_text)
        self.addSpace(20)

        self.grey_text = QtWidgets.QLabel(self.centralwidget)
        self.grey_text.setObjectName("grey_text")
        self.grey_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.grey_text)
        self.addSpace(20)

        # Create a horizontal layout for buttons
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setSpacing(20)  # Add spacing between buttons
        
        self.build_btn = QtWidgets.QPushButton(self.centralwidget)
        self.build_btn.setObjectName("build_btn")
        self.build_btn.setFixedSize(200, 50)
        self.button_layout.addWidget(self.build_btn, alignment=QtCore.Qt.AlignmentFlag.AlignRight)

        self.reload_db_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reload_db_btn.setObjectName("reload_db_btn")
        self.reload_db_btn.setFixedSize(200, 50)
        self.button_layout.addWidget(self.reload_db_btn, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        self.main_layout.addLayout(self.button_layout)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1205, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addSpace(self, s):
        self.main_layout.setSpacing(s)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header_text.setText(_translate("MainWindow", "Pick Parts. Build Your PC.\n"
                                                          "Compare and Share"))
        self.header_text.adjustSize()

        self.build_btn.setText(_translate("MainWindow", "Start Your Build"))
        self.build_btn.adjustSize()

        self.reload_db_btn.setText(_translate("MainWindow", "Reload Database"))
        self.reload_db_btn.adjustSize()

        self.grey_text.setText(_translate("MainWindow", "We provide part-selection and compatibility guidance for\n"
                                                       "do-it-yourself computer builders"))
        self.grey_text.adjustSize()


class LandingPage(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget):
        super(LandingPage, self).__init__()
        self.ui = Ui_LandingPage()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        
        # Initialize data controller and scraper
        self.data_controller = DataController()
        self.scraper = PCComponentScraper()

        # Connect button signals to slots
        self.ui.build_btn.clicked.connect(self.go_to_choosing_parts)
        self.ui.reload_db_btn.clicked.connect(self.reload_database)

        # Apply stylesheet
        try:
            with open("./style/landing_page_style.qss", "r") as file:
                qss = file.read()
                self.setStyleSheet(qss)
        except FileNotFoundError:
            print("QSS file not found. Make sure the path is correct.")
        
    def go_to_choosing_parts(self):
        choosing_parts_page = self.stacked_widget.widget(3)
        main_window = self.stacked_widget.window()  # Access the main window
        
        # Set the main window size to match ChoosingPartsPage
        main_window.resize(choosing_parts_page.size())
        self.stacked_widget.setCurrentWidget(choosing_parts_page)
    
    def reload_database(self):
        print("Reloading database...")
        self.scraper.scrape_all()
        self.data_controller.store_all_data()
        print("Database reloaded successfully.")
        self.go_to_choosing_parts()
