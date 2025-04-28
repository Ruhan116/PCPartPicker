import sqlite3
from PyQt6 import QtCore, QtWidgets
from models.component_selection_manager import ComponentSelectionManager


class Ui_MBPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1299, 768)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Title Label
        self.label = QtWidgets.QLabel("Choose A Motherboard", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1301, 101))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font: 75 30pt 'Arial'; font-weight: bold; color: white; background-color: #555579;")

        # Tab Widget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 120, 1251, 541))
        self.tabWidget.setStyleSheet("font: 16pt 'Arial';")

        # Motherboard Details Tab
        self.tab = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab, "Motherboard Details")

        # Table
        self.table = QtWidgets.QTableWidget(self.tab)
        self.table.setGeometry(QtCore.QRect(10, 60, 1231, 431))
        self.table.setColumnCount(8)
        self.table.setStyleSheet("font: 10pt 'Arial';")
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Size", "Socket", "Chipset", "Price", "Action", "Edit"])

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
        self.refresh_btn.clicked.connect(self.load_motherboard_data)

        self.back_btn = QtWidgets.QPushButton("Back", self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(30, 670, 141, 31))
        self.back_btn.setStyleSheet("font: 14pt 'Arial';")

    def load_motherboard_data(self):
        """Load motherboard data based on the selected sorting option and CPU socket."""
        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        # Get the selected CPU from the ComponentSelectionManager
        selected_cpu = self.manager.get_component_name("CPU")

        # Determine the sorting option
        if self.sort_ascending.isChecked():
            base_query = """
            SELECT id, Name, Size, Socket, Chipset, Price
            FROM Motherboard
            WHERE Socket = ? OR ? IS NULL
            ORDER BY CAST(REPLACE(Price, '$', '') AS REAL) ASC
            """
        elif self.sort_descending.isChecked():
            base_query = """
            SELECT id, Name, Size, Socket, Chipset, Price
            FROM Motherboard
            WHERE Socket = ? OR ? IS NULL
            ORDER BY CAST(REPLACE(Price, '$', '') AS REAL) DESC
            """
        else:  # Default to "Relevant"
            base_query = """
            SELECT id, Name, Size, Socket, Chipset, Price
            FROM Motherboard
            WHERE Socket = ? OR ? IS NULL
            """

        # If a CPU is selected, retrieve its socket
        if selected_cpu:
            cursor.execute("SELECT Socket FROM CPU WHERE Name = ?", (selected_cpu,))
            cpu_socket = cursor.fetchone()
            if cpu_socket:
                cpu_socket = cpu_socket[0]
            else:
                cpu_socket = None
        else:
            cpu_socket = None

        # Execute the query with the CPU socket filter
        cursor.execute(base_query, (cpu_socket, cpu_socket))
        rows = cursor.fetchall()
        connection.close()

        self.populate_table(rows)

    def search_by_keyword(self):
        """Search motherboard data by keyword."""
        keyword = self.keyword_search_input.text().strip()

        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        if keyword:
            like_pattern = f"%{keyword}%"
            query = """
            SELECT id, Name, Size, Socket, Chipset, Price
            FROM Motherboard
            WHERE Name LIKE ? OR Size LIKE ? OR Socket LIKE ? OR Chipset LIKE ?
            """
            cursor.execute(query, (like_pattern, like_pattern, like_pattern, like_pattern))
        else:
            self.load_motherboard_data()  # Reload data with the current sorting option
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
            self.table.setCellWidget(row_num, 6, add_button)

            edit_button = QtWidgets.QPushButton("Edit")
            edit_button.setStyleSheet("font-family: Arial;")
            edit_button.clicked.connect(lambda _, r=row_num: self.handle_edit_button(r))
            self.table.setCellWidget(row_num, 7, edit_button)

    def handle_add_button(self, row):
        motherboard_name = self.table.item(row, 1).text()
        self.manager.set_component_name("Motherboard", motherboard_name)
        print(f"'Add' button clicked for Motherboard Name: {motherboard_name}")

    def handle_edit_button(self, row):
        id_ = self.table.item(row, 0).text()
        name = self.table.item(row, 1).text()
        size = self.table.item(row, 2).text()
        socket = self.table.item(row, 3).text()
        chipset = self.table.item(row, 4).text()
        price = self.table.item(row, 5).text()

        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Edit Motherboard Details")
        dialog.resize(400, 400)

        layout = QtWidgets.QFormLayout(dialog)

        name_edit = QtWidgets.QLineEdit(name)
        size_edit = QtWidgets.QLineEdit(size)
        socket_edit = QtWidgets.QLineEdit(socket)
        chipset_edit = QtWidgets.QLineEdit(chipset)
        price_edit = QtWidgets.QLineEdit(price)

        layout.addRow("Name:", name_edit)
        layout.addRow("Size:", size_edit)
        layout.addRow("Socket:", socket_edit)
        layout.addRow("Chipset:", chipset_edit)
        layout.addRow("Price:", price_edit)

        save_btn = QtWidgets.QPushButton("Save")
        save_btn.clicked.connect(lambda: self.save_edit(dialog, id_, name_edit.text(), size_edit.text(), socket_edit.text(), chipset_edit.text(), price_edit.text()))
        layout.addWidget(save_btn)

        dialog.exec()

    def save_edit(self, dialog, id_, name, size, socket, chipset, price):
        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE Motherboard
            SET Name = ?, Size = ?, Socket = ?, Chipset = ?, Price = ?
            WHERE id = ?
        """, (name, size, socket, chipset, price, id_))

        connection.commit()
        connection.close()

        dialog.accept()
        self.load_motherboard_data()


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