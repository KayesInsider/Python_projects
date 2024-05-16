import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a label for the title
        self.title_label = QLabel('Welcome to Key Drawing Sign Australia', self)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")

        # Create buttons for uploading and recording videos
        self.upload_button = QPushButton('Upload Video', self)
        self.record_button = QPushButton('Record Video', self)

        # Create a submit button
        self.submit_button = QPushButton('Submit', self)

        # Create a layout and add the widgets to it
        layout = QVBoxLayout(self)
        layout.addWidget(self.title_label)
        layout.addWidget(self.upload_button)
        layout.addWidget(self.record_button)
        layout.addWidget(self.submit_button)

        # Set window size and title
        self.setWindowTitle('Key Drawing Sign Australia')
        self.setGeometry(100, 100, 400, 300)

if __name__ == '__main__':
    # Create the application instance
    app = QApplication(sys.argv)

    # Create the main window
    window = MainWindow()
    window.show()

    # Execute the application
    sys.exit(app.exec())
