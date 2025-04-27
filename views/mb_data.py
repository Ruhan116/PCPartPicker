import sqlite3

from PyQt6 import QtCore, QtGui, QtWidgets

from models.component_selection_manager import ComponentSelectionManager


class Ui_MBPage(object):
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
        
        # Motherboard Tab
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        
        # Motherboard Table
        self.table = QtWidgets.QTableWidget(parent=self.tab)
        self.table.setGeometry(QtCore.QRect(10, 60, 1231, 431))
        self.table.setStyleSheet("font: 10pt \"Arial\";")
        self.table.setObjectName("table")
        self.table.setColumnCount(7)  # 6 columns for data + 1 for "Add" button column
        self.table.setRowCount(0)
        
        # Set up table headers
        headers = ["id", "Name", "Size", "Socket", "Chipset", "Price", "Action"]
        for i, header in enumerate(headers):
            item = QtWidgets.QTableWidgetItem()
            item.setText(header)
            self.table.setHorizontalHeaderItem(i, item)
        
        # Label for Search
        self.label_2 = QtWidgets.QLabel(parent=self.tab)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 450, 41))
        self.label_2.setStyleSheet("font: 20pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        
        # Filter Text Box
        self.count_filter_txt = QtWidgets.QSpinBox(parent=self.tab)
        self.count_filter_txt.setGeometry(QtCore.QRect(520, 10, 111, 41))
        self.count_filter_txt.setObjectName("count_filter_txt")
        
        # Search Button
        self.search_btn = QtWidgets.QPushButton(parent=self.tab)
        self.search_btn.setGeometry(QtCore.QRect(650, 10, 151, 41))
        self.search_btn.setObjectName("search_btn")
        self.search_btn.setText("Search")
        self.search_btn.clicked.connect(self.load_motherboard_data)
        
        # Search Bar for Keyword Search
        self.keyword_search_input = QtWidgets.QLineEdit(self.tab)
        self.keyword_search_input.setGeometry(QtCore.QRect(820, 10, 261, 41))
        self.keyword_search_input.setPlaceholderText("Search by keyword...")
        self.keyword_search_input.setObjectName("keyword_search_input")

        self.keyword_search_btn = QtWidgets.QPushButton(self.tab)
        self.keyword_search_btn.setGeometry(QtCore.QRect(1100, 10, 141, 41))
        self.keyword_search_btn.setText("Search")
        self.keyword_search_btn.setObjectName("keyword_search_btn")
        self.keyword_search_btn.clicked.connect(self.search_by_keyword)
        
        # Adding tab
        self.tabWidget.addTab(self.tab, "Motherboard Details")
        
        # Label for Main Title
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1301, 101))
        self.label.setStyleSheet("font: 75 30pt \"Arial\"; font-weight: bold; color: rgb(255, 255, 255); background-color: #555579;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("Choose A Motherboard")
        
        # Refresh Button
        self.refresh_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(1120, 670, 141, 31))
        self.refresh_btn.setStyleSheet("font: 14pt \"Arial\";")
        self.refresh_btn.setObjectName("refresh_btn")
        self.refresh_btn.setText("Refresh")
        self.refresh_btn.clicked.connect(self.load_motherboard_data)
        
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Motherboard Options"))
        
        # Set table headers with translations
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Size"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Socket"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Chipset"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Price"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Action"))
        
        self.label_2.setText(_translate("MainWindow", "Search Motherboards by Size:"))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Motherboard Details"))
        self.label.setText(_translate("MainWindow", "Choose A Motherboard"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.back_btn.setText(_translate("MainWindow", "Back"))

    def load_motherboard_data(self):
        count_value = self.count_filter_txt.value()

        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        if count_value > 0:
            cursor.execute("SELECT * FROM Motherboard WHERE Count <= ?", (count_value,))
        else:
            cursor.execute("SELECT * FROM Motherboard")

        rows = cursor.fetchall()
        self.populate_table(rows)
        connection.close()
        
        connection.close()
        
    def search_by_keyword(self):
        keyword = self.keyword_search_input.text().strip()

        if not keyword:
            connection = sqlite3.connect("data/database/database.sqlite")
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Motherboard")
            rows = cursor.fetchall()
            self.populate_table(rows)
            connection.close()
            return

        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Motherboard WHERE Name LIKE ? OR Size LIKE ? OR Price LIKE ? OR id LIKE ? OR Socket LIKE ? OR Chipset LIKE ?", ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
        rows = cursor.fetchall()
        self.populate_table(rows)
        connection.close()  
        
    def handle_add_button(self, row):
        motherboard_name = self.table.item(row, 1).text()
        self.manager.set_component_name("Motherboard", motherboard_name)
        print(f"Motherboard selected with Name: {motherboard_name}")

    def populate_table(self, rows):
        self.table.setRowCount(len(rows))

        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))

            add_button = QtWidgets.QPushButton("Add")
            add_button.setStyleSheet("font-family: Arial;")
            add_button.clicked.connect(lambda _, r=row_num: self.handle_add_button(r))
            self.table.setCellWidget(row_num, 6, add_button)
class MBPage(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget, manager: ComponentSelectionManager):
        super(MBPage, self).__init__()
        self.ui = Ui_MBPage()
        self.ui.manager = manager
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.load_motherboard_data()
        # Back button functionality
        self.ui.back_btn.clicked.connect(self.go_back)

    def go_back(self):
        self.stacked_widget.setCurrentIndex(3)
