import sqlite3

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SSDPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1299, 768)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Setup Tab Widget
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 120, 1251, 541))
        self.tabWidget.setStyleSheet("font: 16pt \"Arial\";")
        self.tabWidget.setObjectName("tabWidget")
        
        # SSD Tab
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        
        # SSD Table
        self.table = QtWidgets.QTableWidget(parent=self.tab)
        self.table.setGeometry(QtCore.QRect(10, 60, 1231, 431))
        self.table.setStyleSheet("font: 10pt \"Arial\";")
        self.table.setObjectName("table")
        self.table.setColumnCount(6)  # 5 columns for data + 1 for "Add" button column
        self.table.setRowCount(0)
        
        # Set up table headers
        headers = ["id", "Name", "Size", "Bus", "Format", "Action"]
        for i, header in enumerate(headers):
            item = QtWidgets.QTableWidgetItem()
            item.setText(header)
            self.table.setHorizontalHeaderItem(i, item)
        
        # Label for Search
        self.label_2 = QtWidgets.QLabel(parent=self.tab)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 661, 41))
        self.label_2.setStyleSheet("font: 20pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        
        # Filter Text Box
        self.size_filter_txt = QtWidgets.QSpinBox(parent=self.tab)
        self.size_filter_txt.setGeometry(QtCore.QRect(700, 10, 111, 41))
        self.size_filter_txt.setObjectName("size_filter_txt")
        
        # Search Button
        self.search_btn = QtWidgets.QPushButton(parent=self.tab)
        self.search_btn.setGeometry(QtCore.QRect(830, 10, 231, 41))
        self.search_btn.setObjectName("search_btn")
        self.search_btn.setText("Search")
        self.search_btn.clicked.connect(self.load_ssd_data)
        
        # Adding tab
        self.tabWidget.addTab(self.tab, "SSD Details")
        
        # Label for Main Title
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1301, 101))
        self.label.setStyleSheet("font: 75 30pt \"Arial\"; font-weight: bold; color: rgb(255, 255, 255); background-color: #555579;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("Choose SSD")
        
        # Refresh Button
        self.refresh_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(1120, 670, 141, 31))
        self.refresh_btn.setStyleSheet("font: 14pt \"Arial\";")
        self.refresh_btn.setObjectName("refresh_btn")
        self.refresh_btn.setText("Refresh")
        self.refresh_btn.clicked.connect(self.load_ssd_data)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1299, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SSD Options"))
        
        # Set table headers with translations
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Size"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Bus"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Format"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Action"))
        
        self.label_2.setText(_translate("MainWindow", "Search SSD by Size:"))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "SSD Details"))
        self.label.setText(_translate("MainWindow", "Choose SSD"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))

    def load_ssd_data(self):
        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM SSD")
        rows = cursor.fetchall()
        
        self.table.setRowCount(len(rows))
        
        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))
            
            add_button = QtWidgets.QPushButton("Add")
            add_button.setStyleSheet("font-family: Arial;")
            add_button.clicked.connect(lambda _, r=row_num: self.handle_add_button(r))
            self.table.setCellWidget(row_num, len(row_data), add_button)
        
        connection.close()
        
    def handle_add_button(self, row):
        ssd_name = self.table.item(row, 1).text()
        print(f"'Add' button clicked for SSD: {ssd_name}")

class SSDPage(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget):
        super(SSDPage, self).__init__()
        self.ui = Ui_SSDPage()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.load_ssd_data() 
