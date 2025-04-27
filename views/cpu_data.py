import sqlite3

from PyQt6 import QtCore, QtGui, QtWidgets

from models.component_selection_manager import ComponentSelectionManager


class Ui_CPUPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1299, 768)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Title Label
        self.label = QtWidgets.QLabel("Choose A CPU", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1301, 101))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font: 75 30pt 'Arial'; font-weight: bold; color: white; background-color: #555579;")

        # Tab Widget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 120, 1251, 541))
        self.tabWidget.setStyleSheet("font: 16pt 'Arial';")

        # CPU Details Tab
        self.tab = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab, "CPU Details")

        # Table
        self.table = QtWidgets.QTableWidget(self.tab)
        self.table.setGeometry(QtCore.QRect(10, 60, 1231, 431))
        self.table.setColumnCount(9)
        self.table.setStyleSheet("font: 10pt 'Arial';")
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Socket", "Clock Speed", "Turbo Speed", "Cores", "Threads", "Price", "Action"])

        # Count Filter
        self.label_2 = QtWidgets.QLabel("Search CPUs with Count ≤", self.tab)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 450, 41))
        self.label_2.setStyleSheet("font: 20pt 'Arial';")

        self.count_filter_txt = QtWidgets.QSpinBox(self.tab)
        self.count_filter_txt.setGeometry(QtCore.QRect(520, 10, 111, 41))
        self.count_filter_txt.setMaximum(99999)

        self.search_btn = QtWidgets.QPushButton("Search", self.tab)
        self.search_btn.setGeometry(QtCore.QRect(650, 10, 151, 41))
        self.search_btn.clicked.connect(self.load_cpu_data)

        # Keyword Search
        self.keyword_search_input = QtWidgets.QLineEdit(self.tab)
        self.keyword_search_input.setGeometry(QtCore.QRect(820, 10, 261, 41))
        self.keyword_search_input.setPlaceholderText("Search by keyword...")

        self.keyword_search_btn = QtWidgets.QPushButton("Search", self.tab)
        self.keyword_search_btn.setGeometry(QtCore.QRect(1100, 10, 141, 41))
        self.keyword_search_btn.clicked.connect(self.search_by_keyword)

        # Edit Details Tab (empty)
        self.tab_2 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_2, "Edit Details")

        # Refresh and Back Buttons
        self.refresh_btn = QtWidgets.QPushButton("Refresh", self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(1120, 670, 141, 31))
        self.refresh_btn.setStyleSheet("font: 14pt 'Arial';")
        self.refresh_btn.clicked.connect(self.load_cpu_data)

        self.back_btn = QtWidgets.QPushButton("Back", self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(30, 670, 141, 31))
        self.back_btn.setStyleSheet("font: 14pt 'Arial';")

    def load_cpu_data(self):
        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        count_value = self.count_filter_txt.value()

        if count_value > 0:
            cursor.execute("SELECT id, Name, Socket, Clock_Speed, Turbo_Speed, Cores, Threads, Price FROM CPU WHERE Count <= ?", (count_value,))
        else:
            cursor.execute("SELECT id, Name, Socket, Clock_Speed, Turbo_Speed, Cores, Threads, Price FROM CPU")

        rows = cursor.fetchall()
        connection.close()

        self.populate_table(rows)

    def search_by_keyword(self):
        keyword = self.keyword_search_input.text().strip()

        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        if keyword:
            like_pattern = f"%{keyword}%"
            cursor.execute("""
                SELECT id, Name, Socket, Clock_Speed, Turbo_Speed, Cores, Threads, Price
                FROM CPU
                WHERE Name LIKE ? OR Socket LIKE ? OR Price LIKE ? OR id LIKE ? 
                OR Clock_Speed LIKE ? OR Turbo_Speed LIKE ? OR Cores LIKE ? OR Threads LIKE ?
            """, (like_pattern, like_pattern, like_pattern, like_pattern, like_pattern, like_pattern, like_pattern, like_pattern))
        else:
            cursor.execute("SELECT id, Name, Socket, Clock_Speed, Turbo_Speed, Cores, Threads, Price FROM CPU")

        rows = cursor.fetchall()
        connection.close()

        self.populate_table(rows)

    def populate_table(self, rows):
        self.table.setRowCount(len(rows))

        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))

            add_button = QtWidgets.QPushButton("Add")
            add_button.setStyleSheet("font-family: Arial;")
            add_button.clicked.connect(lambda _, r=row_num: self.handle_add_button(r))
            self.table.setCellWidget(row_num, 8, add_button)

    def handle_add_button(self, row):
        cpu_name = self.table.item(row, 1).text()
        self.manager.set_component_name("CPU", cpu_name)
        print(f"'Add' button clicked for CPU Name: {cpu_name}")


class CPUPage(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget, manager: ComponentSelectionManager):
        super().__init__()
        self.ui = Ui_CPUPage()
        self.ui.manager = manager
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget

        self.ui.load_cpu_data()
        self.ui.back_btn.clicked.connect(self.go_back)

    def go_back(self):
        self.stacked_widget.setCurrentIndex(3)
