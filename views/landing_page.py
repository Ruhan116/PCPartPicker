from PyQt6 import QtCore, QtGui, QtWidgets


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

        self.build_btn = QtWidgets.QPushButton(self.centralwidget)
        self.build_btn.setObjectName("build_btn")
        self.build_btn.setFixedSize(200, 50)
        self.main_layout.addWidget(self.build_btn)
        self.main_layout.setAlignment(self.build_btn, QtCore.Qt.AlignmentFlag.AlignCenter)

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

        self.grey_text.setText(_translate("MainWindow", "We provide part-selection and compatibility guidance for\n"
                                                       "do-it-yourself computer builders"))
        self.grey_text.adjustSize()


class LandingPage(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget):
        super(LandingPage, self).__init__()
        self.ui = Ui_LandingPage()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.build_btn.clicked.connect(self.go_to_choosing_parts)
        try:
            with open("./style/landing_page_style.qss", "r") as file:
                qss = file.read()
                self.setStyleSheet(qss)
        except FileNotFoundError:
            print("QSS file not found. Make sure the path is correct.")
        # self.ui.build_btn.clicked.connect(self.go_to_build_page)
        
    def go_to_choosing_parts(self):
        choosing_parts_page = self.stacked_widget.widget(3)
        main_window = self.stacked_widget.window()  # Access the main window
        
        # Set the main window size to match ChoosingPartsPage
        main_window.resize(choosing_parts_page.size())
        self.stacked_widget.setCurrentWidget(choosing_parts_page)
        
