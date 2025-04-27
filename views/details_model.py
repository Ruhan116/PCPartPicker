from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox,
    QFormLayout, QPushButton
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys

class BuildDetailsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Build Details')
        self.setGeometry(100, 100, 900, 600)

        # Set main background color
        self.setStyleSheet("background-color: #f5f5f5;")

        # Main layout
        main_layout = QVBoxLayout()

        # Header Section (with title)
        header_layout = QVBoxLayout()

        # Header text
        header_label = QLabel('Flip #11, RTX 3060, Ryzen 5 3600')
        header_label.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: white; padding: 10px;"
        )
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add header to a container with a blue background
        header_container = QWidget()
        header_container.setStyleSheet("background-color: #4a4a80;")  # Blue background
        header_container.setLayout(header_layout)
        header_layout.addWidget(header_label)
        header_container.setFixedHeight(100)

        main_layout.addWidget(header_container)

        # Back Button Layout (under the header, aligned left)
        back_button_layout = QHBoxLayout()

        # Back Button (placed on the left side, under the header)
        back_button = QPushButton("Back")
        back_button.setStyleSheet("""
            font-size: 16px; font-weight: bold; color: white;
            background-color: #4a4a80; padding: 10px; border-radius: 5px;
        """)
        back_button.setFixedWidth(100)  # Set a fixed width for the back button
        back_button.setFixedHeight(40)  # Set a fixed height for the back button
        back_button.clicked.connect(self.go_back)  # Connect button to go_back method
        back_button_layout.addWidget(back_button)  # Add the back button to the left

        # Set the alignment of the back_button_layout to the left
        back_button_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Add the back button layout to the main layout
        main_layout.addLayout(back_button_layout)

        # Image and Description Layout (Vertical)
        content_layout = QVBoxLayout()

        # Adjust layout margins and spacing
        content_layout.setContentsMargins(0, 0, 0, 0)  # No outer margins
        content_layout.setSpacing(5)  # Small space between image and description

        # Image Section
        image_label = QLabel(self)
        pixmap = QPixmap('02.png')  # Make sure this image exists
        image_label.setPixmap(pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Align image to the center
        image_label.setStyleSheet("margin: 0px; padding: 0px;")  # Remove margin and padding

        # Description Section
        description_label = QLabel(
            'A nice flip. Listed on Jawa and marketplace.\n\n'
            'This build is optimized for gaming and everyday multitasking. '
            'This build is optimized for gaming and everyday multitasking.'
        )
        description_label.setWordWrap(True)
        description_label.setStyleSheet("font-size: 14px; color: #4a4a4a; margin: 0px; padding: 0px;")
        description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Align description to the center

        # Add the widgets to the layout
        content_layout.addWidget(image_label)
        content_layout.addWidget(description_label)

        # Create a container widget for the content
        content_container = QWidget(self)
        content_container.setLayout(content_layout)

        # Add the content container to the main layout
        main_layout.addWidget(content_container)

        # Part List Section
        parts_layout = QFormLayout()
        parts = {
            'CPU': 'AMD Ryzen 5 3600', 'GPU': 'Radeon RX 7900 XTX',
            'Motherboard': 'ASRock A520M-HDV', 'Memory': 'Corsair Vengeance LPX 16GB',
            'Storage': 'KingSpec NVMe SSD 1TB', 'Video Card': 'PNY VERTO GeForce RTX 3060',
        }
        prices = {
            'CPU': 55.00, 'GPU': 10.00, 'Motherboard': 58.00,
            'Memory': 20.00, 'Storage': 47.00, 'Video Card': 180.00,
        }
        total_price = sum(prices.values())

        for part, name in parts.items():
            part_label = QLabel(f'{part}:')
            part_details = QLabel(f'{name} - ${prices[part]:.2f}')
            parts_layout.addRow(part_label, part_details)

        total_label = QLabel(f'Total: ${total_price:.2f}')
        total_label.setStyleSheet("font-weight: bold; font-size: 14px; color: green;")
        parts_layout.addRow('', total_label)

        parts_group_box = QGroupBox('Part List')
        parts_group_box.setLayout(parts_layout)

        main_layout.addWidget(parts_group_box)

        # Set main layout
        self.setLayout(main_layout)

    def go_back(self):
        """Handle navigation back to the building page."""
        self.close()  # Close the details window
        # Assuming this is the main window, you would want to switch to the previous page
        self.parent().setCurrentIndex(0)  # This assumes the main window is using QStackedWidget to switch pages


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BuildDetailsWindow()
    window.show()
    sys.exit(app.exec())
