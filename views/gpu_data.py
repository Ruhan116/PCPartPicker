import sqlite3

from PyQt6 import QtCore, QtGui, QtWidgets

from models.component_selection_manager import ComponentSelectionManager


class Ui_GPUPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1299, 768)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.setup_header()
        self.setup_tab_widget()
        self.setup_footer(MainWindow)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setup_header(self):
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1301, 101))
        self.label.setStyleSheet("font: 75 30pt 'Arial'; font-weight: bold; color: white; background-color: #555579;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

    def setup_tab_widget(self):
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 120, 1251, 541))
        self.tabWidget.setStyleSheet("font: 16pt 'Arial';")
        self.tabWidget.setObjectName("tabWidget")

        # Tab 1 - GPU Details
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.setup_gpu_details_tab()

        self.tabWidget.addTab(self.tab, "GPU Details")

        # Tab 2 - Edit Details (currently empty)
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "Edit Details")

    def setup_gpu_details_tab(self):
        # Table
        self.table = QtWidgets.QTableWidget(self.tab)
        self.table.setGeometry(QtCore.QRect(10, 110, 1231, 381))
        self.table.setStyleSheet("font: 10pt 'Arial';")
        self.table.setObjectName("table")
        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        headers = ["id", "Name", "Series", "VRAM", "TDP","Price", "Action"]
        self.table.setHorizontalHeaderLabels(headers)

        # Label
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 500, 41))
        self.label_2.setStyleSheet("font: 20pt 'Arial';")
        self.label_2.setObjectName("label_2")

        # SpinBox for Memory Filtering
        self.count_filter_txt = QtWidgets.QSpinBox(self.tab)
        self.count_filter_txt.setGeometry(QtCore.QRect(520, 10, 111, 41))
        self.count_filter_txt.setObjectName("count_filter_txt")

        # Button for Memory-based Search
        self.search_btn = QtWidgets.QPushButton(self.tab)
        self.search_btn.setGeometry(QtCore.QRect(650, 10, 151, 41))
        self.search_btn.setObjectName("search_btn")
        self.search_btn.clicked.connect(self.load_gpu_data)

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

    def setup_footer(self, MainWindow):
        # Refresh Button
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(1120, 670, 141, 31))
        self.refresh_btn.setStyleSheet("font: 14pt 'Arial';")
        self.refresh_btn.setObjectName("refresh_btn")
        self.refresh_btn.clicked.connect(self.load_gpu_data)

        # Back Button
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(30, 670, 141, 31))
        self.back_btn.setStyleSheet("font: 14pt 'Arial';")
        self.back_btn.setObjectName("back_btn")

        # Menubar and Statusbar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1299, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GPU Options"))
        self.label.setText(_translate("MainWindow", "Choose A GPU"))
        self.label_2.setText(_translate("MainWindow", "Search by Memory ≥ : "))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "GPU Details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Edit Details"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.back_btn.setText(_translate("MainWindow", "Back"))

    def load_gpu_data(self):
        count_value = self.count_filter_txt.value()

        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        if count_value > 0:
            cursor.execute("SELECT * FROM GPU WHERE Count <= ?", (count_value,))
        else:
            cursor.execute("SELECT * FROM GPU")

        rows = cursor.fetchall()
        self.populate_table(rows)
        connection.close()

    def search_by_keyword(self):
        keyword = self.keyword_search_input.text().strip()

        if not keyword:
            connection = sqlite3.connect("data/database/database.sqlite")
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM GPU")
            rows = cursor.fetchall()
            self.populate_table(rows)
            connection.close()
            return

        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM GPU WHERE Name LIKE ? OR Series LIKE ? OR Price LIKE ? OR id LIKE ? OR VRAM LIKE ? OR TDP LIKE ?", ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
        rows = cursor.fetchall()
        self.populate_table(rows)
        connection.close()

    def populate_table(self, rows):
        self.table.setRowCount(len(rows))
        self.table.setColumnCount(7)

        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))

            add_button = QtWidgets.QPushButton("Add")
            add_button.setStyleSheet("font-family: Arial;")
            add_button.clicked.connect(lambda _, r=row_num: self.handle_add_button(r))
            self.table.setCellWidget(row_num, 6, add_button)

    def handle_add_button(self, row):
        gpu_name = self.table.item(row, 1).text()
        self.manager.set_component_name("GPU", gpu_name)
        print(f"'Add' button clicked for GPU Name: {gpu_name}")


class GPUPage(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget, manager: ComponentSelectionManager):
        super(GPUPage, self).__init__()
        self.ui = Ui_GPUPage()
        self.ui.manager = manager
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget

        self.ui.load_gpu_data()

        self.ui.back_btn.clicked.connect(self.go_back)

    def go_back(self):
        self.stacked_widget.setCurrentIndex(3)  # Assuming the index 3 refers to the previous page
