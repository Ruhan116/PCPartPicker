from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ChoosingPartsPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Header Frame
        self.header_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.header_frame.setGeometry(QtCore.QRect(0, 0, 1280, 80))
        self.header_frame.setObjectName("header_frame")  # Dark background color

        # Header Text
        self.header_label = QtWidgets.QLabel(parent=self.header_frame)
        self.header_label.setGeometry(QtCore.QRect(0, 0, 1280, 80))
        self.header_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header_label.setObjectName("header_label")# White text color

        # Main Layout
        self.heading_text = QtWidgets.QWidget(parent=self.centralwidget)
        self.heading_text.setGeometry(QtCore.QRect(250, 120, 401, 481))
        self.heading_text.setObjectName("heading_text")

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.heading_text)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # Vertical Layouts for Labels and Buttons
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        # Label Layouts
        self.cpu_label = QtWidgets.QLabel(parent=self.heading_text)
        self.cpu_label.setObjectName("cpu_label")
        self.verticalLayout_7.addWidget(self.cpu_label)

        self.gpu_label = QtWidgets.QLabel(parent=self.heading_text)
        self.gpu_label.setObjectName("gpu_label")
        self.verticalLayout_7.addWidget(self.gpu_label)

        self.hdd_label = QtWidgets.QLabel(parent=self.heading_text)
        self.hdd_label.setObjectName("hdd_label")
        self.verticalLayout_7.addWidget(self.hdd_label)

        self.motherboard_label = QtWidgets.QLabel(parent=self.heading_text)
        self.motherboard_label.setObjectName("motherboard_label")
        self.verticalLayout_7.addWidget(self.motherboard_label)

        self.psu_label = QtWidgets.QLabel(parent=self.heading_text)
        self.psu_label.setObjectName("psu_label")
        self.verticalLayout_7.addWidget(self.psu_label)

        self.ram_label = QtWidgets.QLabel(parent=self.heading_text)
        self.ram_label.setObjectName("ram_label")
        self.verticalLayout_7.addWidget(self.ram_label)

        self.ssd_label = QtWidgets.QLabel(parent=self.heading_text)
        self.ssd_label.setObjectName("ssd_label")
        self.verticalLayout_7.addWidget(self.ssd_label)

        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        # Buttons Layout
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.cpu_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.cpu_button.setObjectName("cpu_button")
        self.verticalLayout_4.addWidget(self.cpu_button)

        self.gpu_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.gpu_button.setObjectName("gpu_button")
        self.verticalLayout_4.addWidget(self.gpu_button)

        self.hdd_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.hdd_button.setObjectName("hdd_button")
        self.verticalLayout_4.addWidget(self.hdd_button)

        self.motherboard_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.motherboard_button.setObjectName("motherboard_button")
        self.verticalLayout_4.addWidget(self.motherboard_button)

        self.psu_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.psu_button.setObjectName("psu_button")
        self.verticalLayout_4.addWidget(self.psu_button)

        self.ram_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.ram_button.setObjectName("ram_button")
        self.verticalLayout_4.addWidget(self.ram_button)

        self.ssd_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.ssd_button.setObjectName("ssd_button")
        self.verticalLayout_4.addWidget(self.ssd_button)

        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Choose Your PC Parts"))
        self.header_label.setText(_translate("MainWindow", "Choose Your Parts"))
        self.cpu_label.setText(_translate("MainWindow", "CPU"))
        self.gpu_label.setText(_translate("MainWindow", "GPU"))
        self.hdd_label.setText(_translate("MainWindow", "HDD"))
        self.motherboard_label.setText(_translate("MainWindow", "Motherboard"))
        self.psu_label.setText(_translate("MainWindow", "Power Supply"))
        self.ram_label.setText(_translate("MainWindow", "RAM"))
        self.ssd_label.setText(_translate("MainWindow", "SSD"))
        self.cpu_button.setText(_translate("MainWindow", "+ Choose a CPU"))
        self.gpu_button.setText(_translate("MainWindow", "+ Choose a GPU"))
        self.hdd_button.setText(_translate("MainWindow", "+ Choose an HDD"))
        self.motherboard_button.setText(_translate("MainWindow", "+ Choose a Motherboard"))
        self.psu_button.setText(_translate("MainWindow", "+ Choose a Power Supply"))
        self.ram_button.setText(_translate("MainWindow", "+ Choose a RAM"))
        self.ssd_button.setText(_translate("MainWindow", "+ Choose an SSD"))



class ChoosingPartsPage(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget):
        super(ChoosingPartsPage, self).__init__()
        self.ui = Ui_ChoosingPartsPage()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        try:
            with open("./style/choosing_parts_style.qss", "r") as file:
                qss = file.read()
                self.setStyleSheet(qss)
        except FileNotFoundError:
            print("QSS file not found. Make sure the path is correct.")
        self.setFixedSize(1280, 720)