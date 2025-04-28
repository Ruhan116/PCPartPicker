import sqlite3

from PyQt6 import QtCore, QtGui, QtWidgets

from models.component_selection_manager import ComponentSelectionManager


class CPUCoolerEditDialog(QtWidgets.QDialog):
    def __init__(self, parent, row_data, save_callback):
        super().__init__(parent)
        self.setWindowTitle("Edit CPU Cooler")
        self.resize(400, 300)
        self.save_callback = save_callback

        layout = QtWidgets.QVBoxLayout()

        self.name_input = QtWidgets.QLineEdit(self)
        self.name_input.setPlaceholderText("Name")
        self.name_input.setText(row_data[1])

        self.socket_input = QtWidgets.QLineEdit(self)
        self.socket_input.setPlaceholderText("Socket")
        self.socket_input.setText(row_data[2])

        self.price_input = QtWidgets.QLineEdit(self)
        self.price_input.setPlaceholderText("Price")
        self.price_input.setText(str(row_data[3]))

        self.save_button = QtWidgets.QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_changes)

        layout.addWidget(QtWidgets.QLabel("Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QtWidgets.QLabel("Socket:"))
        layout.addWidget(self.socket_input)
        layout.addWidget(QtWidgets.QLabel("Price:"))
        layout.addWidget(self.price_input)
        layout.addStretch()
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_changes(self):
        name = self.name_input.text().strip()
        socket = self.socket_input.text().strip()
        price = self.price_input.text().strip()

        if not name or not socket or not price:
            QtWidgets.QMessageBox.warning(self, "Validation Error", "All fields are required.")
            return

        self.save_callback(name, socket, price)
        self.accept()


class Ui_CPUCoolerPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 800)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(0, 0, 1300, 80))
        self.title_label.setStyleSheet("font: bold 28pt 'Arial'; color: white; background-color: #555579;")
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setText("Choose A CPU Cooler")

        self.search_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.search_input.setGeometry(QtCore.QRect(30, 90, 400, 40))
        self.search_input.setPlaceholderText("Search by keyword...")
        self.search_input.setStyleSheet("font: 14pt 'Arial';")

        self.search_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(450, 90, 120, 40))
        self.search_button.setText("Search")
        self.search_button.setStyleSheet("font: 14pt 'Arial';")
        self.search_button.clicked.connect(self.search_cpu_coolers)

        self.table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.table.setGeometry(QtCore.QRect(30, 150, 1240, 500))
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Socket", "Price", "Action", "Edit"])
        self.table.setStyleSheet("font: 12pt 'Arial';")
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

        self.refresh_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(1130, 670, 140, 40))
        self.refresh_button.setText("Refresh")
        self.refresh_button.setStyleSheet("font: 14pt 'Arial';")
        self.refresh_button.clicked.connect(self.load_cpu_cooler_data)

        self.back_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(30, 670, 140, 40))
        self.back_button.setText("Back")
        self.back_button.setStyleSheet("font: 14pt 'Arial';")

        # Sort by Price Label
        self.sort_label = QtWidgets.QLabel("Sort by Price:", self.centralwidget)
        self.sort_label.setGeometry(QtCore.QRect(600, 90, 120, 40))
        self.sort_label.setStyleSheet("font: 14pt 'Arial';")

        # Radio Buttons for Sorting
        self.sort_relevant = QtWidgets.QRadioButton("Relevant", self.centralwidget)
        self.sort_relevant.setGeometry(QtCore.QRect(730, 90, 100, 40))
        self.sort_relevant.setChecked(True)  # Default selection

        self.sort_ascending = QtWidgets.QRadioButton("Ascending", self.centralwidget)
        self.sort_ascending.setGeometry(QtCore.QRect(840, 90, 100, 40))

        self.sort_descending = QtWidgets.QRadioButton("Descending", self.centralwidget)
        self.sort_descending.setGeometry(QtCore.QRect(950, 90, 100, 40))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.connection = sqlite3.connect("data/database/database.sqlite")  # Persistent connection

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CPU Cooler Options"))

    def load_cpu_cooler_data(self):
        """Load CPU cooler data based on the selected sorting option."""
        cursor = self.connection.cursor()

        # Determine the sorting option
        if self.sort_ascending.isChecked():
            query = """
            SELECT id, Name, Socket, Price
            FROM CPU_Coolers
            ORDER BY CAST(REPLACE(Price, '$', '') AS REAL) ASC
            """
        elif self.sort_descending.isChecked():
            query = """
            SELECT id, Name, Socket, Price
            FROM CPU_Coolers
            ORDER BY CAST(REPLACE(Price, '$', '') AS REAL) DESC
            """
        else:  # Default to "Relevant"
            query = """
            SELECT id, Name, Socket, Price
            FROM CPU_Coolers
            """

        cursor.execute(query)
        rows = cursor.fetchall()
        self.populate_table(rows)

    def search_cpu_coolers(self):
        keyword = self.search_input.text().strip()
        cursor = self.connection.cursor()
        query = "SELECT * FROM CPU_Coolers WHERE Name LIKE ? OR Socket LIKE ? OR id LIKE ? OR Price LIKE ?"
        cursor.execute(query, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
        rows = cursor.fetchall()
        self.populate_table(rows)

    def populate_table(self, rows):
        self.table.setRowCount(0)

        for row_data in rows:
            row_number = self.table.rowCount()
            self.table.insertRow(row_number)

            for col_number, data in enumerate(row_data):
                self.table.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))

            add_button = QtWidgets.QPushButton("Add")
            add_button.setStyleSheet("font: 12pt 'Arial';")
            add_button.clicked.connect(lambda _, r=row_data: self.handle_add_button(r))
            self.table.setCellWidget(row_number, 4, add_button)

            edit_button = QtWidgets.QPushButton("Edit")
            edit_button.setStyleSheet("font: 12pt 'Arial';")
            edit_button.clicked.connect(lambda _, r=row_data: self.handle_edit_button(r))
            self.table.setCellWidget(row_number, 5, edit_button)

    def handle_add_button(self, row_data):
        cpu_cooler_name = row_data[1]
        self.manager.set_component_name("CPU_Cooler", cpu_cooler_name)
        print(f"'Add' button clicked for CPU Cooler: {cpu_cooler_name}")

    def handle_edit_button(self, row_data):
        def save_changes(name, socket, price):
            cursor = self.connection.cursor()
            query = "UPDATE CPU_Coolers SET Name = ?, Socket = ?, Price = ? WHERE id = ?"
            cursor.execute(query, (name, socket, price, row_data[0]))
            self.connection.commit()
            self.load_cpu_cooler_data()
            QtWidgets.QMessageBox.information(None, "Success", "CPU Cooler updated successfully.")

        edit_dialog = CPUCoolerEditDialog(None, row_data, save_changes)
        edit_dialog.exec()


class CPUCoolerPage(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget, manager: ComponentSelectionManager):
        super().__init__()
        self.ui = Ui_CPUCoolerPage()
        self.ui.manager = manager
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget

        self.ui.load_cpu_cooler_data()

        self.ui.back_button.clicked.connect(self.go_back)

    def go_back(self):
        self.stacked_widget.setCurrentIndex(3)
