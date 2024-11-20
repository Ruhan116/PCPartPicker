from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QFrame, QLineEdit, QHBoxLayout, QLabel, QLayout, QStackedWidget
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from PyQt6.QtGui import QPixmap
import sys
from details_model import BuildDetailsWindow  # Import the details page

class QFlowLayout(QLayout):
    """A custom layout that allows widgets to wrap automatically into new rows."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.items = []
        self.spacing = 10

    def addItem(self, item):
        self.items.append(item)

    def count(self):
        return len(self.items)

    def itemAt(self, index):
        return self.items[index] if index < len(self.items) else None

    def takeAt(self, index):
        return self.items.pop(index) if index < len(self.items) else None

    def setGeometry(self, rect):
        super().setGeometry(rect)
        x, y = rect.left() + self.spacing, rect.top() + self.spacing
        row_height = 0

        for item in self.items:
            widget = item.widget()
            if widget is None:
                continue

            widget.setGeometry(x, y, widget.width(), widget.height())
            x += widget.width() + self.spacing
            row_height = max(row_height, widget.height())

            if x + widget.width() > rect.right():  # New row
                x = rect.left() + self.spacing
                y += row_height + self.spacing
                row_height = widget.height()

    def sizeHint(self):
        return QSize(200, 200)


class CompletedBuildsUI(QWidget):
    build_selected = pyqtSignal()  # Signal for navigation

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Completed Builds")
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("background-color: #f5f5f5;")

        self.builds = [
            {"username": "MrIT84", "name": "7800X3D Build", "cpu": "AMD Ryzen 7 7800X3D", "gpu": "Radeon RX 7900 XTX", "cost": "$6024.65"},
            {"username": "PcGuyFinny", "name": "My first PC I built", "cpu": "AMD Ryzen 5 7600X", "gpu": "GeForce RTX 4060", "cost": "$1053.03"},
            {"username": "TechLover", "name": "Gaming Beast", "cpu": "Intel Core i9-13900K", "gpu": "RTX 4090", "cost": "$4500.00"},
            {"username": "BuildWizard", "name": "Budget Build", "cpu": "Intel Core i5-12400", "gpu": "RTX 3050", "cost": "$800.00"}
        ]
        self.filtered_builds = self.builds.copy()

        self.setLayout(self.create_main_layout())

    def create_main_layout(self):
        main_layout = QVBoxLayout()

        # Header
        header_label = QLabel("Completed Builds")
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            background-color: #5f5c88;
            color: white;
            padding: 15px;
            margin: 0;
        """)
        main_layout.addWidget(header_label)

        # Search bar
        search_layout = QHBoxLayout()
        search_label = QLabel("Search")
        search_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #333;margin-left: 5px;")
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Enter build name or username...")
        search_bar.textChanged.connect(self.filter_builds)
        search_bar.setStyleSheet("""
            font-size: 14px;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 5px;
            margin-left: 5px;
        """)
        search_layout.addWidget(search_label)
        search_layout.addWidget(search_bar)
        main_layout.addLayout(search_layout)

        # Scroll area for builds
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QFlowLayout()  # Using QFlowLayout here
        self.scroll_layout.setSpacing(10)  # Set spacing between cards
        self.update_builds()

        self.scroll_content.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_content)
        main_layout.addWidget(self.scroll_area)

        return main_layout

    def create_build_card(self, build):
        card = QFrame()
        card.setFixedSize(300, 300)
        card.setStyleSheet("""
            background-color: white;
            border-radius: 10px;
            border: 1px solid #e0e0e0;
        """)

        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(5, 5, 5, 5)

        image_label = QLabel()
        pixmap = QPixmap("02.png").scaled(380, 100, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
        image_label.setPixmap(pixmap)
        image_label.setStyleSheet("border: none;")
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        user_label = QLabel(build["username"])
        user_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #555; border: none;")
        user_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        user_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)  # Enable text selection

        name_label = QLabel(build["name"])
        name_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #333;border: none")
        name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        name_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)  # Enable text selection

        cost_label = QLabel(f"Cost: {build['cost']}")
        cost_label.setStyleSheet("font-size: 14px; color: #007BFF; font-weight: bold;")
        cost_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        cost_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)  # Enable text selection

        card_layout.addWidget(image_label)
        card_layout.addWidget(user_label)
        card_layout.addWidget(name_label)
        card_layout.addWidget(cost_label)
        card.setLayout(card_layout)

        # Add release event handler to navigate to details window
        card.mouseReleaseEvent = lambda event: self.build_selected.emit()

        return card

    def update_builds(self):
        """Update the layout with the current filtered builds."""
        # Clear the layout
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Add filtered builds
        for build in self.filtered_builds:
            build_card = self.create_build_card(build)
            self.scroll_layout.addWidget(build_card)

    def filter_builds(self, text):
        """Filter builds based on the search bar input."""
        text = text.lower()
        self.filtered_builds = [
            build for build in self.builds
            if text in build["name"].lower() or text in build["username"].lower()
        ]
        self.update_builds()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Completed Builds")
        self.setGeometry(100, 100, 1200, 800)

        # Stacked widget for switching between pages
        self.stacked_widget = QStackedWidget(self)
        
        # Create the completed builds page and build details page
        self.completed_builds_page = CompletedBuildsUI()
        self.build_details_page = BuildDetailsWindow()

        # Add pages to stacked widget
        self.stacked_widget.addWidget(self.completed_builds_page)
        self.stacked_widget.addWidget(self.build_details_page)

        # Layout for the main window
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)

        # Connect signal from completed builds page to show the build details page
        self.completed_builds_page.build_selected.connect(self.show_build_details)

    def show_build_details(self):
        self.stacked_widget.setCurrentIndex(1)  # Switch to BuildDetailsPage


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Show main window which handles page navigation
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
