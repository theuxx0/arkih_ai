from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QFrame
)

from ui.sidebar import Sidebar
from ui.dashboard import Dashboard

from themes.theme_manager import apply_theme


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ARKIH-AI")
        self.resize(1400, 800)

        self.setup_ui()

        apply_theme(self, "neon_purple")

    def setup_ui(self):

        layout = QHBoxLayout()

        self.sidebar = Sidebar()
        self.dashboard = Dashboard()

        layout.addWidget(self.sidebar)
        layout.addWidget(self.dashboard)

        self.setLayout(layout)