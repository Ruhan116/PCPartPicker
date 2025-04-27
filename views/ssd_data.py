import sqlite3

from PyQt6 import QtCore, QtGui, QtWidgets

from models.component_selection_manager import ComponentSelectionManager


class Ui_SSDPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1299, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Setup Tab Widget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 120, 1251, 541))
        self.tabWidget.setStyleSheet("font: 16pt 'Arial';")
        self.tabWidget.setObjectName("tabWidget")

        # SSD Tab
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        # SSD Table
        self.table = QtWidgets.QTableWidget(self.tab)
        self.table.setGeometry(QtCore.QRect(10, 60, 1231, 431))
        self.table.setStyleSheet("font: 10pt 'Arial';")
        self.table.setObjectName("table")
        self.table.setColumnCount(8)  # 6 data + Action + Edit
        self.table.setRowCount(0)

        headers = ["id", "Name", "Size", "Bus", "Format", "Price", "Action", "Edit"]
        for i, header in enumerate(headers):
            item = QtWidgets.QTableWidgetItem()
            item.setText(header)
            self.table.setHorizontalHeaderItem(i, item)

        # Label for Search
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 450, 41))
        self.label_2.setStyleSheet("font: 20pt 'Arial';")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Search SSD by Size:")

        # Search Input
        self.keyword_search_input = QtWidgets.QLineEdit(self.tab)
        self.keyword_search_input.setGeometry(QtCore.QRect(820, 10, 261, 41))
        self.keyword_search_input.setPlaceholderText("Search by keyword...")
        self.keyword_search_input.setObjectName("keyword_search_input")

        self.keyword_search_btn = QtWidgets.QPushButton(self.tab)
        self.keyword_search_btn.setGeometry(QtCore.QRect(1100, 10, 141, 41))
        self.keyword_search_btn.setText("Search")
        self.keyword_search_btn.setObjectName("keyword_search_btn")
        self.keyword_search_btn.clicked.connect(self.search_by_keyword)

        self.tabWidget.addTab(self.tab, "SSD Details")

        # Main Title Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1301, 101))
        self.label.setStyleSheet(
            "font: 75 30pt 'Arial'; font-weight: bold; color: white; background-color: #555579;"
        )
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("Choose SSD")

        # Refresh Button
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(1120, 670, 141, 31))
        self.refresh_btn.setStyleSheet("font: 14pt 'Arial';")
        self.refresh_btn.setObjectName("refresh_btn")
        self.refresh_btn.setText("Refresh")
        self.refresh_btn.clicked.connect(self.load_ssd_data)

        # Back Button
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(30, 670, 141, 31))
        self.back_btn.setStyleSheet("font: 14pt 'Arial';")
        self.back_btn.setObjectName("back_btn")
        self.back_btn.setText("Back")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1299, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SSD Options"))

    def load_ssd_data(self):
        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()
        cursor.execute("SELECT id, Name, Size, Bus, Format, Price FROM SSD")
        rows = cursor.fetchall()
        connection.close()
        self.populate_table(rows)

    def handle_add_button(self, row):
        ssd_name = self.table.item(row, 1).text()
        self.manager.set_component_name("SSD", ssd_name)
        print(f"SSD selected: {ssd_name}")

    def search_by_keyword(self):
        keyword = self.keyword_search_input.text().strip()
        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        if keyword:
            like_pattern = f"%{keyword}%"
            cursor.execute(
                """
                SELECT id, Name, Size, Bus, Format, Price FROM SSD
                WHERE Name LIKE ? OR Size LIKE ? OR Bus LIKE ? OR Format LIKE ? OR Price LIKE ?
                """,
                (like_pattern, like_pattern, like_pattern, like_pattern, like_pattern)
            )
        else:
            cursor.execute("SELECT id, Name, Size, Bus, Format, Price FROM SSD")

        rows = cursor.fetchall()
        connection.close()
        self.populate_table(rows)

    def populate_table(self, rows):
        self.table.setRowCount(len(rows))
        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))

            # Add Button
            add_button = QtWidgets.QPushButton("Add")
            add_button.setStyleSheet("font-family: Arial;")
            add_button.clicked.connect(lambda _, r=row_num: self.handle_add_button(r))
            self.table.setCellWidget(row_num, 6, add_button)

            # Edit Button
            edit_button = QtWidgets.QPushButton("Edit")
            edit_button.setStyleSheet("font-family: Arial;")
            edit_button.clicked.connect(lambda _, r=row_num: self.handle_edit_btn(r))
            self.table.setCellWidget(row_num, 7, edit_button)

    def handle_edit_btn(self, row):
        id_ = self.table.item(row, 0).text()
        name = self.table.item(row, 1).text()
        size = self.table.item(row, 2).text()
        bus = self.table.item(row, 3).text()
        format_ = self.table.item(row, 4).text()
        price = self.table.item(row, 5).text()

        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Edit SSD Details")
        dialog.resize(400, 300)

        layout = QtWidgets.QFormLayout(dialog)

        name_edit = QtWidgets.QLineEdit(name)
        size_edit = QtWidgets.QLineEdit(size)
        bus_edit = QtWidgets.QLineEdit(bus)
        format_edit = QtWidgets.QLineEdit(format_)
        price_edit = QtWidgets.QLineEdit(price)

        layout.addRow("Name:", name_edit)
        layout.addRow("Size:", size_edit)
        layout.addRow("Bus:", bus_edit)
        layout.addRow("Format:", format_edit)
        layout.addRow("Price:", price_edit)

        save_button = QtWidgets.QPushButton("Save")
        save_button.clicked.connect(lambda: self.save_edit(dialog, id_, name_edit.text(), size_edit.text(), bus_edit.text(), format_edit.text(), price_edit.text()))
        layout.addRow(save_button)

        dialog.exec()

    def save_edit(self, dialog, id_, name, size, bus, format_, price):
        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()
        cursor.execute(
            """
            UPDATE SSD
            SET Name = ?, Size = ?, Bus = ?, Format = ?, Price = ?
            WHERE id = ?
            """,
            (name, size, bus, format_, price, id_)
        )
        connection.commit()
        connection.close()

        dialog.accept()
        self.load_ssd_data()


class SSDPage(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget, manager: ComponentSelectionManager):
        super(SSDPage, self).__init__()
        self.ui = Ui_SSDPage()
        self.ui.manager = manager
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.load_ssd_data()
        self.ui.back_btn.clicked.connect(self.go_back)

    def go_back(self):
        self.stacked_widget.setCurrentIndex(3)
