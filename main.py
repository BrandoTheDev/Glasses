from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton, QComboBox
from PyQt5.QtWebEngineWidgets import QWebEngineView

class EmbeddedBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the web browser view
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.example.com"))

        # Create input field for URL
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL and press Enter")
        self.url_input.returnPressed.connect(self.navigate)

        # Create button to trigger navigation
        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.navigate)

        # Create a history dropdown
        self.history_combo = QComboBox()
        self.history_combo.currentIndexChanged.connect(self.load_from_history)

        # Set up the main layout with a QVBoxLayout
        layout = QVBoxLayout()

        # Create a sub-layout for controls (URL input, Go button, history combo)
        controls_layout = QHBoxLayout()

        # Add the URL input with a 2/1 fraction size
        controls_layout.addWidget(self.url_input, 2)

        # Add the Go button with a 1/1 fraction size
        controls_layout.addWidget(self.go_button, 1)

        # Add the history combo with a 1/1 fraction size
        controls_layout.addWidget(self.history_combo, 1)

        # Add the controls sub-layout to the main layout
        layout.addLayout(controls_layout)

        # Add the browser with a 3/1 fraction size
        layout.addWidget(self.browser, 3)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the main window
        self.setCentralWidget(container)

        # Set the initial size of the window
        self.setGeometry(100, 100, 800, 600)

        # Set the window title
        self.setWindowTitle("Glasses")

        # Set the window always on top
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        # Keep track of navigation history
        self.history = []

    def navigate(self):
        # Get the URL from the input field
        url = self.url_input.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            # Prepend "http://" if the URL doesn't start with it
            url = "http://" + url
        # Set the browser to the specified URL
        self.browser.setUrl(QUrl(url))

        # Update history
        if url not in self.history:
            self.history.append(url)
            self.history_combo.addItem(url)

    def load_from_history(self, index):
        # Load a URL from the history dropdown
        if index >= 0 and index < len(self.history):
            url = self.history[index]
            self.browser.setUrl(QUrl(url))

    def changeEvent(self, event):
        # Handle changes in the window state
        if event.type() == event.WindowStateChange and self.windowState() == Qt.WindowMinimized:
            # Default behavior on window minimize (do nothing specific)
            pass

if __name__ == "__main__":
    import sys

    # Create the application instance
    app = QApplication(sys.argv)
    
    # Create the main window instance
    window = EmbeddedBrowser()
    
    # Show the main window
    window.show()
    
    # Start the application event loop
    sys.exit(app.exec_())
