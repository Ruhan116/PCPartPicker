import sqlite3

from PyQt6 import QtCore, QtGui, QtWidgets

from models.component_selection_manager import ComponentSelectionManager


class EditDialog(QtWidgets.QDialog):
    def __init__(self, id_, name, size, price, parent=None):
        super(EditDialog, self).__init__(parent)
        self.setWindowTitle("Edit Case")
        self.resize(300, 200)

        self.id = id_

        layout = QtWidgets.QVBoxLayout()

        self.name_input = QtWidgets.QLineEdit(name)
        self.size_input = QtWidgets.QLineEdit(size)
        self.price_input = QtWidgets.QLineEdit(price)

        layout.addWidget(QtWidgets.QLabel("Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QtWidgets.QLabel("Size:"))
        layout.addWidget(self.size_input)
        layout.addWidget(QtWidgets.QLabel("Price:"))
        layout.addWidget(self.price_input)

        self.save_btn = QtWidgets.QPushButton("Save")
        self.save_btn.clicked.connect(self.save_changes)
        layout.addWidget(self.save_btn)

        self.setLayout(layout)

    def save_changes(self):
        new_name = self.name_input.text()
        new_size = self.size_input.text()
        new_price = self.price_input.text()

        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE Cases SET Name = ?, Size = ?, Price = ? WHERE id = ?
        """, (new_name, new_size, new_price, self.id))
        connection.commit()
        connection.close()

        self.accept()


class Ui_CasePage(object):
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

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.setup_case_details_tab()

        self.tabWidget.addTab(self.tab, "Case Details")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "Edit Details")

    def setup_case_details_tab(self):
        self.table = QtWidgets.QTableWidget(self.tab)
        self.table.setGeometry(QtCore.QRect(10, 110, 1231, 381))
        self.table.setStyleSheet("font: 10pt 'Arial';")
        self.table.setObjectName("table")
        self.table.setColumnCount(6)
        self.table.setRowCount(0)
        headers = ["id", "Name", "Size", "Price", "Add", "Edit"]
        self.table.setHorizontalHeaderLabels(headers)

        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 500, 41))
        self.label_2.setStyleSheet("font: 20pt 'Arial';")
        self.label_2.setObjectName("label_2")

        # Sort by Price Label
        self.sort_label = QtWidgets.QLabel("Sort by Price:", self.tab)
        self.sort_label.setGeometry(QtCore.QRect(10, 60, 100, 41))
        self.sort_label.setStyleSheet("font: 14pt 'Arial';")

        # Radio Buttons for Sorting
        self.sort_relevant = QtWidgets.QRadioButton("Relevant", self.tab)
        self.sort_relevant.setGeometry(QtCore.QRect(120, 60, 120, 41))
        self.sort_relevant.setChecked(True)  # Default selection

        self.sort_ascending = QtWidgets.QRadioButton("Ascending", self.tab)
        self.sort_ascending.setGeometry(QtCore.QRect(260, 60, 120, 41))

        self.sort_descending = QtWidgets.QRadioButton("Descending", self.tab)
        self.sort_descending.setGeometry(QtCore.QRect(400, 60, 120, 41))

        self.count_filter_txt = QtWidgets.QSpinBox(self.tab)
        self.count_filter_txt.setGeometry(QtCore.QRect(520, 10, 111, 41))
        self.count_filter_txt.setObjectName("count_filter_txt")

        self.search_btn = QtWidgets.QPushButton(self.tab)
        self.search_btn.setGeometry(QtCore.QRect(650, 10, 151, 41))
        self.search_btn.setObjectName("search_btn")
        self.search_btn.clicked.connect(self.load_case_data)

        self.keyword_search_input = QtWidgets.QLineEdit(self.tab)
        self.keyword_search_input.setGeometry(QtCore.QRect(820, 10, 261, 41))
        self.keyword_search_input.setPlaceholderText("Search by Name...")
        self.keyword_search_input.setObjectName("keyword_search_input")

        self.keyword_search_btn = QtWidgets.QPushButton(self.tab)
        self.keyword_search_btn.setGeometry(QtCore.QRect(1100, 10, 141, 41))
        self.keyword_search_btn.setText("Search")
        self.keyword_search_btn.setObjectName("keyword_search_btn")
        self.keyword_search_btn.clicked.connect(self.search_by_keyword)

    def setup_footer(self, MainWindow):
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(1120, 670, 141, 31))
        self.refresh_btn.setStyleSheet("font: 14pt 'Arial';")
        self.refresh_btn.setObjectName("refresh_btn")
        self.refresh_btn.clicked.connect(self.load_case_data)

        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(30, 670, 141, 31))
        self.back_btn.setStyleSheet("font: 14pt 'Arial';")
        self.back_btn.setObjectName("back_btn")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1299, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Case Options"))
        self.label.setText(_translate("MainWindow", "Choose A Case"))
        self.label_2.setText(_translate("MainWindow", "Search by count ≤ : "))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Case Details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Edit Details"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.back_btn.setText(_translate("MainWindow", "Back"))

    def load_case_data(self):
        """Load case data based on the selected sorting option."""
        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        # Determine the sorting option
        if self.sort_ascending.isChecked():
            query = """
            SELECT id, Name, Size, Price
            FROM Cases
            ORDER BY CAST(REPLACE(Price, '$', '') AS REAL) ASC
            """
        elif self.sort_descending.isChecked():
            query = """
            SELECT id, Name, Size, Price
            FROM Cases
            ORDER BY CAST(REPLACE(Price, '$', '') AS REAL) DESC
            """
        else:  # Default to "Relevant"
            query = """
            SELECT id, Name, Size, Price
            FROM Cases
            """

        cursor.execute(query)
        rows = cursor.fetchall()
        self.populate_table(rows)
        connection.close()

    def search_by_keyword(self):
        keyword = self.keyword_search_input.text().strip()

        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        if keyword:
            cursor.execute("""
                SELECT * FROM Cases WHERE Name LIKE ? OR Size LIKE ? OR Price LIKE ? OR id LIKE ?
            """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
        else:
            cursor.execute("SELECT * FROM Cases")

        rows = cursor.fetchall()
        self.populate_table(rows)
        connection.close()

    def populate_table(self, rows):
        self.table.setRowCount(len(rows))

        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data[:4]):
                self.table.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))

            add_button = QtWidgets.QPushButton("Add")
            add_button.setStyleSheet("font-family: Arial;")
            add_button.clicked.connect(lambda _, r=row_num: self.handle_add_button(r))
            self.table.setCellWidget(row_num, 4, add_button)

            edit_button = QtWidgets.QPushButton("Edit")
            edit_button.setStyleSheet("font-family: Arial;")
            edit_button.clicked.connect(lambda _, r=row_num: self.handle_edit_button(r))
            self.table.setCellWidget(row_num, 5, edit_button)

    def handle_add_button(self, row):
        case_name = self.table.item(row, 1).text()
        self.manager.set_component_name("Case", case_name)
        print(f"'Add' button clicked for Case Name: {case_name}")

    def handle_edit_button(self, row):
        id_ = self.table.item(row, 0).text()
        name = self.table.item(row, 1).text()
        size = self.table.item(row, 2).text()
        price = self.table.item(row, 3).text()

        dialog = EditDialog(id_, name, size, price)
        if dialog.exec():
            self.load_case_data()


class CasePage(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget, manager: ComponentSelectionManager):
        super(CasePage, self).__init__()
        self.ui = Ui_CasePage()
        self.ui.manager = manager
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget

        self.ui.load_case_data()

        self.ui.back_btn.clicked.connect(self.go_back)

    def go_back(self):
        self.stacked_widget.setCurrentIndex(3)