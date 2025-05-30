from PyQt6 import QtCore, QtGui, QtWidgets

from models.component_selection_manager import ComponentSelectionManager
from data.data_loader.build_table import BuildTable
import sqlite3
from models.Session import Session


class Ui_ChoosingPartsPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 1280)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Header Frame
        self.header_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.header_frame.setGeometry(QtCore.QRect(0, 0, 1280, 80))
        self.header_frame.setObjectName("header_frame")

        # Header Text
        self.header_label = QtWidgets.QLabel(parent=self.header_frame)
        self.header_label.setGeometry(QtCore.QRect(0, 0, 1280, 80))
        self.header_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header_label.setObjectName("header_label")

        # Main Layout
        self.heading_text = QtWidgets.QWidget(parent=self.centralwidget)
        self.heading_text.setGeometry(QtCore.QRect(250, 120, 600, 481))  # Increased width from 401 to 600
        self.heading_text.setObjectName("heading_text")

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.heading_text)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # Vertical Layouts for Labels and Buttons
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        # Label Layouts
        self.cpu_label = QtWidgets.QLabel(parent=self.heading_text)
        self.cpu_label.setObjectName("cpu_label")
        self.verticalLayout_7.addWidget(self.cpu_label)

        self.gpu_label = QtWidgets.QLabel(parent=self.heading_text)
        self.gpu_label.setObjectName("gpu_label")
        self.verticalLayout_7.addWidget(self.gpu_label)

        self.hdd_label = QtWidgets.QLabel(parent=self.heading_text)
        self.hdd_label.setObjectName("hdd_label")
        self.verticalLayout_7.addWidget(self.hdd_label)

        self.motherboard_label = QtWidgets.QLabel(parent=self.heading_text)
        self.motherboard_label.setObjectName("motherboard_label")
        self.verticalLayout_7.addWidget(self.motherboard_label)

        self.psu_label = QtWidgets.QLabel(parent=self.heading_text)
        self.psu_label.setObjectName("psu_label")
        self.verticalLayout_7.addWidget(self.psu_label)

        self.ram_label = QtWidgets.QLabel(parent=self.heading_text)
        self.ram_label.setObjectName("ram_label")
        self.verticalLayout_7.addWidget(self.ram_label)

        self.ssd_label = QtWidgets.QLabel(parent=self.heading_text)
        self.ssd_label.setObjectName("ssd_label")
        self.verticalLayout_7.addWidget(self.ssd_label)

        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        # Buttons Layout
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.cpu_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.cpu_button.setObjectName("cpu_button")
        self.verticalLayout_4.addWidget(self.cpu_button)

        self.gpu_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.gpu_button.setObjectName("gpu_button")
        self.verticalLayout_4.addWidget(self.gpu_button)

        # Horizontal layout for HDD buttons
        self.hdd_buttons_layout = QtWidgets.QHBoxLayout()

        self.hdd_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.hdd_button.setObjectName("hdd_button")
        self.hdd_buttons_layout.addWidget(self.hdd_button)

        self.hdd_button_2 = QtWidgets.QPushButton(parent=self.heading_text)
        self.hdd_button_2.setObjectName("hdd_button_2")
        self.hdd_buttons_layout.addWidget(self.hdd_button_2)

        self.verticalLayout_4.addLayout(self.hdd_buttons_layout)  # Add the horizontal layout with both HDD buttons

        self.motherboard_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.motherboard_button.setObjectName("motherboard_button")
        self.verticalLayout_4.addWidget(self.motherboard_button)

        self.psu_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.psu_button.setObjectName("psu_button")
        self.verticalLayout_4.addWidget(self.psu_button)

        # Horizontal layout for RAM buttons
        self.ram_buttons_layout = QtWidgets.QHBoxLayout()

        self.ram_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.ram_button.setObjectName("ram_button")
        self.ram_buttons_layout.addWidget(self.ram_button)

        self.ram_button_2 = QtWidgets.QPushButton(parent=self.heading_text)
        self.ram_button_2.setObjectName("ram_button_2")
        self.ram_buttons_layout.addWidget(self.ram_button_2)

        self.verticalLayout_4.addLayout(self.ram_buttons_layout)  # Add the horizontal layout with both RAM buttons

        # Horizontal layout for SSD buttons
        self.ssd_buttons_layout = QtWidgets.QHBoxLayout()

        self.ssd_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.ssd_button.setObjectName("ssd_button")
        self.ssd_buttons_layout.addWidget(self.ssd_button)

        self.ssd_button_2 = QtWidgets.QPushButton(parent=self.heading_text)
        self.ssd_button_2.setObjectName("ssd_button_2")
        self.ssd_buttons_layout.addWidget(self.ssd_button_2)
        self.verticalLayout_4.addLayout(self.ssd_buttons_layout)  # Add the horizontal layout with both SSD buttons

        self.monitor_label = QtWidgets.QLabel(parent=self.heading_text)
        self.monitor_label.setObjectName("monitor_label")
        self.verticalLayout_7.addWidget(self.monitor_label)
        
        self.cpu_cooler_label = QtWidgets.QLabel(parent=self.heading_text)
        self.cpu_cooler_label.setObjectName("cpu_cooler_label")
        self.verticalLayout_7.addWidget(self.cpu_cooler_label)
        
        self.case_label = QtWidgets.QLabel(parent=self.heading_text)
        self.case_label.setObjectName("case_label")
        self.verticalLayout_7.addWidget(self.case_label)
        
        self.monitor_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.monitor_button.setObjectName("monitor_button")
        self.verticalLayout_4.addWidget(self.monitor_button)
        
        self.cpu_cooler_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.cpu_cooler_button.setObjectName("cpu_cooler_button")
        self.verticalLayout_4.addWidget(self.cpu_cooler_button)
        
        self.case_button = QtWidgets.QPushButton(parent=self.heading_text)
        self.case_button.setObjectName("case_button")
        self.verticalLayout_4.addWidget(self.case_button)
        
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Choose Your PC Parts"))
        self.header_label.setText(_translate("MainWindow", "Choose Your Parts"))
        self.cpu_label.setText(_translate("MainWindow", "CPU"))
        self.gpu_label.setText(_translate("MainWindow", "GPU"))
        self.hdd_label.setText(_translate("MainWindow", "HDD"))
        self.motherboard_label.setText(_translate("MainWindow", "Motherboard"))
        self.psu_label.setText(_translate("MainWindow", "Power Supply"))
        self.ram_label.setText(_translate("MainWindow", "RAM"))
        self.ssd_label.setText(_translate("MainWindow", "SSD"))
        self.monitor_label.setText(_translate("MainWindow", "Monitor"))
        self.cpu_cooler_label.setText(_translate("MainWindow", "CPU Cooler"))
        self.case_label.setText(_translate("MainWindow", "Case"))
        self.monitor_button.setText(_translate("MainWindow", "+ Choose a Monitor"))
        self.cpu_cooler_button.setText(_translate("MainWindow", "+ Choose a CPU Cooler"))
        self.case_button.setText(_translate("MainWindow", "+ Choose a Case"))
        self.cpu_button.setText(_translate("MainWindow", "+ Choose a CPU"))
        self.gpu_button.setText(_translate("MainWindow", "+ Choose a GPU"))
        self.hdd_button.setText(_translate("MainWindow", "+ Choose an HDD"))
        self.hdd_button_2.setText(_translate("MainWindow", "+ Choose an HDD"))
        self.motherboard_button.setText(_translate("MainWindow", "+ Choose a Motherboard"))
        self.psu_button.setText(_translate("MainWindow", "+ Choose a Power Supply"))
        self.ram_button.setText(_translate("MainWindow", "+ Choose a RAM"))
        self.ram_button_2.setText(_translate("MainWindow", "+ Choose a RAM"))
        self.ssd_button.setText(_translate("MainWindow", "+ Choose an SSD"))
        self.ssd_button_2.setText(_translate("MainWindow", "+ Choose an SSD"))


class ChoosingPartsPage(QtWidgets.QMainWindow):
    def __init__(self, stacked_widget, manager: ComponentSelectionManager):
        super(ChoosingPartsPage, self).__init__()
        self.ui = Ui_ChoosingPartsPage()
        self.ui.manager = manager
        self.ui.setupUi(self)
        self.back_button = QtWidgets.QPushButton("<- Back", self)
        self.back_button.setGeometry(10, 10, 100, 40)
        self.back_button.clicked.connect(self.go_back)
        self.stacked_widget = stacked_widget

        self.build_table = BuildTable()

        # Connect existing buttons
        self.ui.cpu_button.clicked.connect(self.show_cpu_page)
        self.ui.gpu_button.clicked.connect(self.show_gpu_page)
        self.ui.hdd_button.clicked.connect(self.show_hdd_page)
        self.ui.hdd_button_2.clicked.connect(self.show_hdd_page)
        self.ui.motherboard_button.clicked.connect(self.show_motherboard_page)
        self.ui.psu_button.clicked.connect(self.show_psu_page)
        self.ui.ram_button.clicked.connect(self.show_ram_page)
        self.ui.ram_button_2.clicked.connect(self.show_ram_page)
        self.ui.ssd_button.clicked.connect(self.show_ssd_page)
        self.ui.ssd_button_2.clicked.connect(self.show_ssd_page)
        self.ui.monitor_button.clicked.connect(self.show_monitor_page)
        self.ui.cpu_cooler_button.clicked.connect(self.show_cpu_cooler_page)
        self.ui.case_button.clicked.connect(self.show_case_page)

        # Add "Build PC" button
        self.build_pc_button = QtWidgets.QPushButton("Build PC", self)
        self.build_pc_button.setGeometry(250, 650, 200, 40)  # Adjust position and size
        self.build_pc_button.setStyleSheet("font: 14pt 'Arial'; background-color: rgb(0, 173, 181); color: white; border-radius: 10px;")
        self.build_pc_button.clicked.connect(self.build_pc)

        # Load QSS for styling
        try:
            with open("./style/choosing_parts_style.qss", "r") as file:
                qss = file.read()
                self.setStyleSheet(qss)
        except FileNotFoundError:
            print("QSS file not found. Make sure the path is correct.")
        self.setFixedSize(1280, 720)

    def build_pc(self):
        # Print all selected components from the ComponentSelectionManager
        selected_components = self.ui.manager.get_component_names()
        print("Selected Components:")
        for component, value in selected_components.items():
            print(f"{component}: {value}")

        # Get the user ID from the session
        try:
            with sqlite3.connect("data/database/database.sqlite") as connection:
                cursor = connection.cursor()

                # Get the user ID from the 'users' table using the username from the session
                username = Session().get_user()  # Get the username from the session
                cursor.execute("SELECT id FROM Users WHERE username = ?", (username,))
                user_id_row = cursor.fetchone()

                if not user_id_row:
                    print(f"Error: User '{username}' not found in the database.")
                    return

                user_id = user_id_row[0]
                print(f"User ID for '{username}': {user_id}")

        except Exception as e:
            print(f"Error retrieving user ID: {e}")
            return

        # Add the build to the database using build_table.add_build
        try:
            self.build_table.add_build(
                user_id=user_id,
                cpu=selected_components.get("CPU"),
                gpu=selected_components.get("GPU"),
                hdd1=selected_components.get("HDD")[0] if len(selected_components.get("HDD", [])) > 0 else None,
                hdd2=selected_components.get("HDD")[1] if len(selected_components.get("HDD", [])) > 1 else None,
                ssd1=selected_components.get("SSD")[0] if len(selected_components.get("SSD", [])) > 0 else None,
                ssd2=selected_components.get("SSD")[1] if len(selected_components.get("SSD", [])) > 1 else None,
                ram1=selected_components.get("RAM")[0] if len(selected_components.get("RAM", [])) > 0 else None,
                ram2=selected_components.get("RAM")[1] if len(selected_components.get("RAM", [])) > 1 else None,
                mobo=selected_components.get("Motherboard"),
                psu=selected_components.get("PSU"),
                monitor=selected_components.get("Monitor"),
                cpu_cooler=selected_components.get("CPU_Cooler"),
                cases=selected_components.get("Case")
            )
            print("Build successfully added to the database.")
        except Exception as e:
            print(f"Error adding build to the database: {e}")
            return

        # Redirect to the BuildDetailsWindow and update it with the latest build
        try:
            with sqlite3.connect("data/database/database.sqlite") as connection:
                cursor = connection.cursor()

                # Get the ID of the most recently added build for the current user
                cursor.execute(
                    "SELECT build_id FROM Builds WHERE user_id = ? ORDER BY build_id DESC LIMIT 1",
                    (user_id,)
                )
                build_id_row = cursor.fetchone()

                if not build_id_row:
                    print("Error: Could not retrieve the latest build ID.")
                    return

                build_id = build_id_row[0]
                print(f"Redirecting to BuildDetailsWindow for Build ID: {build_id}")

                # Redirect to the BuildDetailsWindow
                details_page = self.stacked_widget.widget(15)  # Assuming BuildDetailsWindow is at index 15
                details_page.update_parts(build_id)  # Call the update_parts function with the new build_id
                main_window = self.stacked_widget.window()
                main_window.resize(details_page.size())
                self.stacked_widget.setCurrentWidget(details_page)

        except Exception as e:
            print(f"Error retrieving the latest build ID: {e}")

    def show_cpu_page(self):
        cpu_page = self.stacked_widget.widget(4)
        main_window = self.stacked_widget.window()
        main_window.resize(cpu_page.size())
        self.stacked_widget.setCurrentWidget(cpu_page)

    def show_gpu_page(self):
        gpu_page = self.stacked_widget.widget(5)
        main_window = self.stacked_widget.window()
        main_window.resize(gpu_page.size())
        self.stacked_widget.setCurrentWidget(gpu_page)

    def show_hdd_page(self):
        hdd_page = self.stacked_widget.widget(6)
        main_window = self.stacked_widget.window()
        
        main_window.resize(hdd_page.size())
        self.stacked_widget.setCurrentWidget(hdd_page)
        
    def show_motherboard_page(self):
        motherboard_page = self.stacked_widget.widget(7)
        main_window = self.stacked_widget.window()
        
        main_window.resize(motherboard_page.size())
        self.stacked_widget.setCurrentWidget(motherboard_page)
    
    def show_psu_page(self):
        psu_page = self.stacked_widget.widget(8)
        main_window = self.stacked_widget.window()
        
        main_window.resize(psu_page.size())
        self.stacked_widget.setCurrentWidget(psu_page)
        
    def show_ram_page(self):
        ram_page = self.stacked_widget.widget(9)
        main_window = self.stacked_widget.window()
        
        main_window.resize(ram_page.size())
        self.stacked_widget.setCurrentWidget(ram_page)
        
    def show_ssd_page(self):
        ssd_page = self.stacked_widget.widget(10)
        main_window = self.stacked_widget.window()
        
        main_window.resize(ssd_page.size())
        self.stacked_widget.setCurrentWidget(ssd_page)
    
    def show_monitor_page(self):
        monitor_page = self.stacked_widget.widget(12)
        main_window = self.stacked_widget.window()
        
        main_window.resize(monitor_page.size())
        self.stacked_widget.setCurrentWidget(monitor_page)
    
    def show_cpu_cooler_page(self):
        cpu_cooler_page = self.stacked_widget.widget(13)
        main_window = self.stacked_widget.window()
        main_window.resize(cpu_cooler_page.size())
        self.stacked_widget.setCurrentWidget(cpu_cooler_page)
    
    def show_case_page(self):   
        case_page = self.stacked_widget.widget(14)
        main_window = self.stacked_widget.window()
        
        main_window.resize(case_page.size())
        self.stacked_widget.setCurrentWidget(case_page)
    
    def go_back(self):
        self.stacked_widget.setCurrentIndex(2)