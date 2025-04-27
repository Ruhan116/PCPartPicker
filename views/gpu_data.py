import sqlite3

from PyQt6 import QtCore, QtWidgets

from models.component_selection_manager import ComponentSelectionManager


class Ui_GPUPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1299, 768)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Header
        self.header_label = QtWidgets.QLabel("Choose A GPU", self.centralwidget)
        self.header_label.setGeometry(0, 0, 1300, 80)
        self.header_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header_label.setStyleSheet("font: bold 30pt Arial; color: white; background-color: #555579;")

        # Tabs
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setGeometry(30, 100, 1240, 540)
        self.tab_widget.setStyleSheet("font: 16pt Arial;")

        self.gpu_tab = QtWidgets.QWidget()
        self.tab_widget.addTab(self.gpu_tab, "GPU Details")

        # Search bar
        self.keyword_input = QtWidgets.QLineEdit(self.gpu_tab)
        self.keyword_input.setGeometry(570, 10, 300, 40)
        self.keyword_input.setPlaceholderText("Search by keyword...")

        self.keyword_search_btn = QtWidgets.QPushButton("Search", self.gpu_tab)
        self.keyword_search_btn.setGeometry(890, 10, 100, 40)
        self.keyword_search_btn.clicked.connect(self.search_by_keyword)

        # GPU Table
        self.table = QtWidgets.QTableWidget(self.gpu_tab)
        self.table.setGeometry(10, 70, 1220, 430)
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Series", "VRAM", "TDP", "Price", "Add", "Edit"])
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setStyleSheet("font: 11pt Arial;")

        # Footer Buttons
        self.refresh_btn = QtWidgets.QPushButton("Refresh", self.centralwidget)
        self.refresh_btn.setGeometry(1120, 670, 140, 40)
        self.refresh_btn.setStyleSheet("font: 14pt Arial;")
        self.refresh_btn.clicked.connect(self.load_gpu_data)
        
        self.back_btn = QtWidgets.QPushButton("Back", self.centralwidget)
        self.back_btn.setGeometry(30, 670, 140, 40)
        self.back_btn.setStyleSheet("font: 14pt Arial;")
        
        


    def load_gpu_data(self):
        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        cursor.execute("SELECT id, Name, Series, VRAM, TDP, Price FROM GPU")

        rows = cursor.fetchall()
        connection.close()

        self.populate_table(rows)
        
    def search_by_keyword(self):
        keyword = self.keyword_input.text().strip()

        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        if keyword:
            like_pattern = f"%{keyword}%"
            cursor.execute( """
            SELECT id, Name, Series, VRAM, TDP, Price FROM GPU
            WHERE Name LIKE ? OR Series LIKE ? OR VRAM LIKE ? OR TDP LIKE ? OR Price LIKE ?
            """, (like_pattern, like_pattern, like_pattern, like_pattern, like_pattern))
        else:
            cursor.execute("SELECT id, Name, Series, VRAM, TDP, Price FROM GPU")

        rows = cursor.fetchall()
        connection.close()

        self.populate_table(rows)

    def populate_table(self, rows):
        self.table.setRowCount(len(rows))

        for row_idx, row in enumerate(rows):
            for col_idx, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.table.setItem(row_idx, col_idx, item)

            # Add Button
            add_btn = QtWidgets.QPushButton("Add")
            add_btn.clicked.connect(lambda _, r=row_idx: self.handle_add_btn(r))
            self.table.setCellWidget(row_idx, 6, add_btn)

            # Edit Button
            edit_btn = QtWidgets.QPushButton("Edit")
            edit_btn.clicked.connect(lambda _, r=row_idx: self.handle_edit_btn(r))
            self.table.setCellWidget(row_idx, 7, edit_btn)

    def handle_add_btn(self, row):
        gpu_name = self.table.item(row, 1).text()
        self.manager.set_component_name("GPU", gpu_name)
        print(f"Selected GPU: {gpu_name}")

    def handle_edit_btn(self, row):
        id_ = self.table.item(row, 0).text()
        name = self.table.item(row, 1).text()
        series = self.table.item(row, 2).text()
        vram = self.table.item(row, 3).text()
        tdp = self.table.item(row, 4).text()
        price = self.table.item(row, 5).text()

        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Edit GPU Details")
        dialog.resize(400, 400)

        layout = QtWidgets.QFormLayout(dialog)

        name_edit = QtWidgets.QLineEdit(name)
        series_edit = QtWidgets.QLineEdit(series)
        vram_edit = QtWidgets.QLineEdit(vram)
        tdp_edit = QtWidgets.QLineEdit(tdp)
        price_edit = QtWidgets.QLineEdit(price)

        layout.addRow("Name:", name_edit)
        layout.addRow("Series:", series_edit)
        layout.addRow("VRAM:", vram_edit)
        layout.addRow("TDP:", tdp_edit)
        layout.addRow("Price:", price_edit)

        save_btn = QtWidgets.QPushButton("Save")
        save_btn.clicked.connect(lambda: self.save_edit(dialog, id_, name_edit.text(), series_edit.text(), vram_edit.text(), tdp_edit.text(), price_edit.text()))
        layout.addWidget(save_btn)

        dialog.exec()

    def save_edit(self, dialog, id_, name, series, vram, tdp, price):
        connection = sqlite3.connect("data/database/database.sqlite")
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE GPU
            SET Name = ?, Series = ?, VRAM = ?, TDP = ?, Price = ?
            WHERE id = ?
        """, (name, series, vram, tdp, price, id_))

        connection.commit()
        connection.close()

        dialog.accept()
        self.load_gpu_data()


class GPUPage(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget, manager: ComponentSelectionManager):
        super().__init__()
        self.ui = Ui_GPUPage()
        self.ui.manager = manager
        self.ui.setupUi(self)

        self.stacked_widget = stacked_widget

        # Load GPU Data initially
        self.ui.load_gpu_data()

        # Connect buttons
        self.ui.back_btn.clicked.connect(self.go_back)


    def go_back(self):
        self.stacked_widget.setCurrentIndex(3)
