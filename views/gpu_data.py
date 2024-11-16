import sqlite3

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GPUPage(object):
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
        
        # GPU Tab
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        
        # GPU Table
        self.table = QtWidgets.QTableWidget(parent=self.tab)
        self.table.setGeometry(QtCore.QRect(10, 60, 1231, 431))
        self.table.setStyleSheet("font: 10pt \"Arial\";")
        self.table.setObjectName("table")
        self.table.setColumnCount(6)  # 5 columns for data + 1 for "Add" button column
        self.table.setRowCount(0)
        
        # Set up table headers
        headers = ["id", "Name", "Series", "VRAM", "TDP", "Action"]
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
        self.count_filter_txt = QtWidgets.QSpinBox(parent=self.tab)
        self.count_filter_txt.setGeometry(QtCore.QRect(700, 10, 111, 41))
        self.count_filter_txt.setObjectName("count_filter_txt")
        
        # Search Button
        self.search_btn = QtWidgets.QPushButton(parent=self.tab)
        self.search_btn.setGeometry(QtCore.QRect(830, 10, 231, 41))
        self.search_btn.setObjectName("search_btn")
        self.search_btn.setText("Search")
        self.search_btn.clicked.connect(self.load_gpu_data)
        
        # Adding tab
        self.tabWidget.addTab(self.tab, "GPU Details")
        
        # Label for Main Title
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1301, 101))
        self.label.setStyleSheet("font: 75 30pt \"Arial\"; font-weight: bold; color: rgb(255, 255, 255); background-color: #555579;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("Choose A GPU")
        
        # Refresh Button
        self.refresh_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(1120, 670, 141, 31))
        self.refresh_btn.setStyleSheet("font: 14pt \"Arial\";")
        self.refresh_btn.setObjectName("refresh_btn")
        self.refresh_btn.setText("Refresh")
        self.refresh_btn.clicked.connect(self.load_gpu_data)
        
        # Back button
        self.back_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(30, 670, 141, 31))
        self.back_btn.setStyleSheet("font: 14pt \"Arial\";")
        self.back_btn.setObjectName("back_btn")
        self.back_btn.setText("Back")
        
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
        MainWindow.setWindowTitle(_translate("MainWindow", "GPU Options"))
        
        # Set table headers with translations
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Series"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "VRAM"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TDP"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Action"))
        
        self.label_2.setText(_translate("MainWindow", "Search GPUs with TDP lower or equal to:"))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "GPU Details"))
        self.label.setText(_translate("MainWindow", "Choose A GPU"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.back_btn.setText(_translate("MainWindow", "Back"))

    def load_gpu_data(self):
        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM GPU")
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
        gpu_name = self.table.item(row, 1).text()
        print(f"'Add' button clicked for GPU: {gpu_name}")

class GPUPage(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget):
        super(GPUPage, self).__init__()
        self.ui = Ui_GPUPage()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.load_gpu_data()
        # Back button functionality
        self.ui.back_btn.clicked.connect(self.go_back)
        
    def go_back(self):
        self.stacked_widget.setCurrentIndex(3)
