from PyQt6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel
)

from PyQt6.QtCore import Qt


class Dashboard(QFrame):

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        titulo = QLabel("Dashboard")
        titulo.setObjectName("titulo_dashboard")

        texto = QLabel(
            "Bem-vindo à sua Agenda Inteligente 🚀"
        )

        layout.addWidget(titulo)
        layout.addWidget(texto)

        self.setLayout(layout)