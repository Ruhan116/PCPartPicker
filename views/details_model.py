from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox,
    QFormLayout, QPushButton
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys
import sqlite3

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
        self.header_label = QLabel('Flip #11, RTX 3060, Ryzen 5 3600')
        self.header_label.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: white; padding: 10px;"
        )
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add header to a container with a blue background
        header_container = QWidget()
        header_container.setStyleSheet("background-color: #4a4a80;")  # Blue background
        header_container.setLayout(header_layout)
        header_layout.addWidget(self.header_label)
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
            'This build is optimized for gaming and everyday multitasking. '
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
        self.parts_layout = QFormLayout()  # Make parts_layout an instance variable
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
            self.parts_layout.addRow(part_label, part_details)

        total_label = QLabel(f'Total: ${total_price:.2f}')
        total_label.setStyleSheet("font-weight: bold; font-size: 14px; color: green;")
        self.parts_layout.addRow('', total_label)

        parts_group_box = QGroupBox('Part List')
        parts_group_box.setLayout(self.parts_layout)

        main_layout.addWidget(parts_group_box)

        # Set main layout
        self.setLayout(main_layout)

    def update_parts(self, build_id):
        """Retrieve build details from the database and update the UI."""
        try:
            connection = sqlite3.connect("data/database/database.sqlite")
            cursor = connection.cursor()

            # Query the build details
            cursor.execute("SELECT * FROM Builds WHERE build_id = ?", (build_id,))
            build = cursor.fetchone()

            if not build:
                self.header_label.setText("Build Not Found")
                self.parts_layout.addRow(QLabel("Error:"), QLabel("The selected build could not be found in the database."))
                return

            # Extract build details
            (
                user_id, build_id, cpu, mobo, gpu, ram1, ram2, hdd1, hdd2,
                ssd1, ssd2, psu, cases, cpu_cooler, monitor, price
            ) = build

            # Replace None values with "Not Available" or 0.00
            cpu = cpu or "Not Available"
            mobo = mobo or "Not Available"
            gpu = gpu or "Not Available"
            ram1 = ram1 or "Not Available"
            ram2 = ram2 or "Not Available"
            hdd1 = hdd1 or "Not Available"
            hdd2 = hdd2 or "Not Available"
            ssd1 = ssd1 or "Not Available"
            ssd2 = ssd2 or "Not Available"
            psu = psu or "Not Available"
            cases = cases or "Not Available"
            cpu_cooler = cpu_cooler or "Not Available"
            monitor = monitor or "Not Available"
            price = price or 0.00

            # Update header
            self.header_label.setText(f"Build #{build_id} - User ID: {user_id}")

            # Clear previous parts layout
            while self.parts_layout.count():
                item = self.parts_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

            # Add parts to the layout
            parts = {
                "CPU": cpu, "Motherboard": mobo, "GPU": gpu,
                "RAM1": ram1, "RAM2": ram2, "HDD1": hdd1, "HDD2": hdd2,
                "SSD1": ssd1, "SSD2": ssd2, "PSU": psu, "Case": cases,
                "CPU Cooler": cpu_cooler, "Monitor": monitor
            }

            for part, name in parts.items():
                self.parts_layout.addRow(QLabel(f"{part}:"), QLabel(name))

            # Add total price
            self.parts_layout.addRow(QLabel("Total Price:"), QLabel(f"${price:.2f}"))

            connection.close()

        except Exception as e:
            self.header_label.setText("Error")
            self.parts_layout.addRow(QLabel("Error:"), QLabel(f"An error occurred: {e}"))
            print(f"Error occurred while fetching build details: {e}")  # Log the error for debugging
    
    def go_back(self):
        """Handle navigation back to the building page."""
        self.close()  # Close the details window
        # Assuming this is the main window, you would want to switch to the previous page
        self.parent().setCurrentIndex(0)  # This assumes the main window is using QStackedWidget to switch pages


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BuildDetailsWindow()
    window.update_parts(1)  # Load build with ID 1 for testing
    window.show()
    sys.exit(app.exec())
