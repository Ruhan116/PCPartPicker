import sqlite3
from PyQt6 import QtCore, QtWidgets
from models.component_selection_manager import ComponentSelectionManager


class Ui_HDDPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1299, 768)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Title Label
        self.label = QtWidgets.QLabel("Choose A HDD", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1301, 101))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font: 75 30pt 'Arial'; font-weight: bold; color: white; background-color: #555579;")

        # Tab Widget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 120, 1251, 541))
        self.tabWidget.setStyleSheet("font: 16pt 'Arial';")

        # HDD Details Tab
        self.tab = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab, "HDD Details")

        # Table
        self.table = QtWidgets.QTableWidget(self.tab)
        self.table.setGeometry(QtCore.QRect(10, 60, 1231, 431))
        self.table.setColumnCount(7)
        self.table.setStyleSheet("font: 10pt 'Arial';")
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Size", "RPM", "Price", "Action", "Edit"])

        # Sort by Price Label
        self.sort_label = QtWidgets.QLabel("Sort by Price:", self.tab)
        self.sort_label.setGeometry(QtCore.QRect(10, 10, 100, 41))
        self.sort_label.setStyleSheet("font: 14pt 'Arial';")

        # Radio Buttons for Sorting
        self.sort_relevant = QtWidgets.QRadioButton("Relevant", self.tab)
        self.sort_relevant.setGeometry(QtCore.QRect(120, 10, 120, 41))
        self.sort_relevant.setChecked(True)  # Default selection

        self.sort_ascending = QtWidgets.QRadioButton("Ascending", self.tab)
        self.sort_ascending.setGeometry(QtCore.QRect(260, 10, 120, 41))

        self.sort_descending = QtWidgets.QRadioButton("Descending", self.tab)
        self.sort_descending.setGeometry(QtCore.QRect(400, 10, 120, 41))

        # Keyword Search
        self.keyword_search_input = QtWidgets.QLineEdit(self.tab)
        self.keyword_search_input.setGeometry(QtCore.QRect(820, 10, 261, 41))
        self.keyword_search_input.setPlaceholderText("Search by keyword...")

        self.keyword_search_btn = QtWidgets.QPushButton("Search", self.tab)
        self.keyword_search_btn.setGeometry(QtCore.QRect(1100, 10, 141, 41))
        self.keyword_search_btn.clicked.connect(self.search_by_keyword)

        # Refresh and Back Buttons
        self.refresh_btn = QtWidgets.QPushButton("Refresh", self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(1120, 670, 141, 31))
        self.refresh_btn.setStyleSheet("font: 14pt 'Arial';")
        self.refresh_btn.clicked.connect(self.load_hdd_data)

        self.back_btn = QtWidgets.QPushButton("Back", self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(30, 670, 141, 31))
        self.back_btn.setStyleSheet("font: 14pt 'Arial';")

    def load_hdd_data(self):
        """Load HDD data based on the selected sorting option."""
        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        # Determine the sorting option
        if self.sort_ascending.isChecked():
            query = """
            SELECT id, Name, Size, RPM, Price
            FROM HDD
            ORDER BY CAST(REPLACE(Price, '$', '') AS REAL) ASC
            """
        elif self.sort_descending.isChecked():
            query = """
            SELECT id, Name, Size, RPM, Price
            FROM HDD
            ORDER BY CAST(REPLACE(Price, '$', '') AS REAL) DESC
            """
        else:  # Default to "Relevant"
            query = """
            SELECT id, Name, Size, RPM, Price
            FROM HDD
            """

        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()

        self.populate_table(rows)

    def search_by_keyword(self):
        """Search HDD data by keyword."""
        keyword = self.keyword_search_input.text().strip()

        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        if keyword:
            like_pattern = f"%{keyword}%"
            query = """
            SELECT id, Name, Size, RPM, Price
            FROM HDD
            WHERE Name LIKE ? OR Size LIKE ? OR RPM LIKE ? OR Price LIKE ?
            """
            cursor.execute(query, (like_pattern, like_pattern, like_pattern, like_pattern))
        else:
            self.load_hdd_data()  # Reload data with the current sorting option
            return

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
            self.table.setCellWidget(row_num, 5, add_button)

            edit_button = QtWidgets.QPushButton("Edit")
            edit_button.setStyleSheet("font-family: Arial;")
            edit_button.clicked.connect(lambda _, r=row_num: self.handle_edit_button(r))
            self.table.setCellWidget(row_num, 6, edit_button)

    def handle_add_button(self, row):
        hdd_name = self.table.item(row, 1).text()
        self.manager.set_component_name("HDD", hdd_name)
        print(f"'Add' button clicked for HDD Name: {hdd_name}")

    def handle_edit_button(self, row):
        id_ = self.table.item(row, 0).text()
        name = self.table.item(row, 1).text()
        size = self.table.item(row, 2).text()
        rpm = self.table.item(row, 3).text()
        price = self.table.item(row, 4).text()

        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Edit HDD Details")
        dialog.resize(400, 400)

        layout = QtWidgets.QFormLayout(dialog)

        name_edit = QtWidgets.QLineEdit(name)
        size_edit = QtWidgets.QLineEdit(size)
        rpm_edit = QtWidgets.QLineEdit(rpm)
        price_edit = QtWidgets.QLineEdit(price)

        layout.addRow("Name:", name_edit)
        layout.addRow("Size:", size_edit)
        layout.addRow("RPM:", rpm_edit)
        layout.addRow("Price:", price_edit)

        save_btn = QtWidgets.QPushButton("Save")
        save_btn.clicked.connect(lambda: self.save_edit(dialog, id_, name_edit.text(), size_edit.text(), rpm_edit.text(), price_edit.text()))
        layout.addWidget(save_btn)

        dialog.exec()

    def save_edit(self, dialog, id_, name, size, rpm, price):
        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE HDD
            SET Name = ?, Size = ?, RPM = ?, Price = ?
            WHERE id = ?
        """, (name, size, rpm, price, id_))

        connection.commit()
        connection.close()

        dialog.accept()
        self.load_hdd_data()


class HDDPage(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget, manager: ComponentSelectionManager):
        super(HDDPage, self).__init__()
        self.ui = Ui_HDDPage()
        self.ui.manager = manager
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.load_hdd_data()

        # Back button functionality
        self.ui.back_btn.clicked.connect(self.go_back)

    def go_back(self):
        self.stacked_widget.setCurrentIndex(3)