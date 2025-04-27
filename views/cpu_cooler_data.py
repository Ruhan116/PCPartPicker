import sqlite3

from PyQt6 import QtCore, QtGui, QtWidgets

from models.component_selection_manager import ComponentSelectionManager


class Ui_CPUCoolerPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 800)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title Label
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(0, 0, 1300, 80))
        self.title_label.setStyleSheet("font: bold 28pt 'Arial'; color: white; background-color: #555579;")
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setText("Choose A CPU Cooler")

        # Search Text and Button
        self.search_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.search_input.setGeometry(QtCore.QRect(30, 90, 400, 40))
        self.search_input.setPlaceholderText("Search by keyword...")
        self.search_input.setStyleSheet("font: 14pt 'Arial';")

        self.search_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(450, 90, 120, 40))
        self.search_button.setText("Search")
        self.search_button.setStyleSheet("font: 14pt 'Arial';")
        self.search_button.clicked.connect(self.search_cpu_coolers)

        # Table Widget
        self.table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.table.setGeometry(QtCore.QRect(30, 150, 1240, 500))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Socket", "Price", "Action"])
        self.table.setStyleSheet("font: 12pt 'Arial';")
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

        # Refresh and Back Buttons
        self.refresh_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(1130, 670, 140, 40))
        self.refresh_button.setText("Refresh")
        self.refresh_button.setStyleSheet("font: 14pt 'Arial';")
        self.refresh_button.clicked.connect(self.load_cpu_cooler_data)

        self.back_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(30, 670, 140, 40))
        self.back_button.setText("Back")
        self.back_button.setStyleSheet("font: 14pt 'Arial';")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CPU Cooler Options"))

    def load_cpu_cooler_data(self):
        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM CPU_Coolers")
        rows = cursor.fetchall()
        self.populate_table(rows)

        connection.close()

    def search_cpu_coolers(self):
        keyword = self.search_input.text().strip()
        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        query = "SELECT * FROM CPU_Coolers WHERE Name LIKE ? OR Socket LIKE ? OR id LIKE ? OR Price LIKE ?"
        cursor.execute(query, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
        rows = cursor.fetchall()
        self.populate_table(rows)

        connection.close()

    def populate_table(self, rows):
        self.table.setRowCount(0)

        for row_data in rows:
            row_number = self.table.rowCount()
            self.table.insertRow(row_number)

            for col_number, data in enumerate(row_data):
                self.table.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))

            # Add "Add" button
            add_button = QtWidgets.QPushButton("Add")
            add_button.setStyleSheet("font: 12pt 'Arial';")
            add_button.clicked.connect(lambda _, r=row_number: self.handle_add_button(r))
            self.table.setCellWidget(row_number, 4, add_button)

    def handle_add_button(self, row):
        cpu_cooler_name = self.table.item(row, 1).text()
        self.manager.set_component_name("CPU_Cooler", cpu_cooler_name)
        print(f"'Add' button clicked for CPU Cooler: {cpu_cooler_name}")


class CPUCoolerPage(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget, manager: ComponentSelectionManager):
        super().__init__()
        self.ui = Ui_CPUCoolerPage()
        self.ui.manager = manager
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget

        # Load data initially
        self.ui.load_cpu_cooler_data()

        # Back button action
        self.ui.back_button.clicked.connect(self.go_back)

    def go_back(self):
        self.stacked_widget.setCurrentIndex(3)
