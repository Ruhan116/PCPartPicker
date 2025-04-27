from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox,
    QFormLayout, QPushButton
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap

class BuildDetailsWindow(QWidget):
    back_signal = pyqtSignal()  # Signal for going back
    
    def __init__(self, build_data):
        super().__init__()
        self.build_data = build_data
        self.setup_ui()
        
    def setup_ui(self):
        self.setWindowTitle('Build Details')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f5f5f5;")
        
        # Create the main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # Header
        header = QLabel(f"Build #{self.build_data['build_id']}")
        header.setStyleSheet("""
            background-color: #2c88c4;
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 15px;
        """)
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)

        # Back button
        back_btn = QPushButton("Back")
        back_btn.setStyleSheet("""
            font-size: 14px;
            padding: 8px 16px;
            background-color: #2c88c4;
            color: white;
            border: none;
            border-radius: 5px;
        """)
        back_btn.clicked.connect(self.go_back)
        main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignLeft)

        # Components section
        components_group = QGroupBox("Components")
        components_layout = QFormLayout()
        
        # Add all components that exist in the build
        components = [
            ('CPU', self.build_data.get('cpu')),
            ('Motherboard', self.build_data.get('mobo')),
            ('GPU', self.build_data.get('gpu')),
            ('RAM 1', self.build_data.get('ram1')),
            ('RAM 2', self.build_data.get('ram2')),
            ('HDD 1', self.build_data.get('hdd1')),
            ('HDD 2', self.build_data.get('hdd2')),
            ('SSD 1', self.build_data.get('ssd1')),
            ('SSD 2', self.build_data.get('ssd2')),
            ('Power Supply', self.build_data.get('psu')),
            ('Case', self.build_data.get('cases')),
            ('CPU Cooler', self.build_data.get('cpu_cooler')),
            ('Monitor', self.build_data.get('monitor'))
        ]
        
        for part, value in components:
            if value:  # Only show if not empty
                part_label = QLabel(f"{part}:")
                value_label = QLabel(value)
                components_layout.addRow(part_label, value_label)

        # Add total price
        price = self.build_data.get('price', 0)
        price_label = QLabel(f"${price:.2f}")
        price_label.setStyleSheet("font-weight: bold; color: green;")
        components_layout.addRow(QLabel("Total Price:"), price_label)

        components_group.setLayout(components_layout)
        main_layout.addWidget(components_group)

    def go_back(self):
        """Handle back button click"""
        self.back_signal.emit()
        self.close()