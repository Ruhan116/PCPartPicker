from PyQt6 import QtCore, QtGui, QtWidgets
from controllers.data_controller import DataController
from data.data_loader.Load_Data import PCComponentScraper


class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(1280, 720)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        Dashboard.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=Dashboard)
        self.centralwidget.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 60, 321, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(780, 50, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(57, 62, 70);\n"
"color: rgb(238, 238, 238);")
        self.pushButton.setObjectName("pushButton")
        Dashboard.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Dashboard)
        self.statusbar.setObjectName("statusbar")
        Dashboard.setStatusBar(self.statusbar)

        self.retranslateUi(Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)

    def retranslateUi(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Dashboard.setWindowTitle(_translate("Dashboard", "MainWindow"))
        self.label_2.setText(_translate("Dashboard", "Do you want to reload the database?"))
        self.pushButton.setText(_translate("Dashboard", "Reload"))



class LoadDatabase(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget):
            super(LoadDatabase, self).__init__()
            self.ui = Ui_Dashboard()
            self.ui.setupUi(self)

            # Store references to the stacked widget and auth controller
            self.stacked_widget = stacked_widget
            self.data_controller = DataController()
            self.scraper = PCComponentScraper()


            self.ui.pushButton.clicked.connect(self.reload_database)
    
    def reload_database(self):
        self.scraper.scrape_all()
        self.data_controller.store_all_data()
         
    
