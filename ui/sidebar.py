from PyQt6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QPushButton,
    QLabel
)

from PyQt6.QtCore import Qt


class Sidebar(QFrame):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(250)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        titulo = QLabel("ARKIH-AI")
        titulo.setObjectName("titulo")

        btn_dashboard = QPushButton("🏠 Dashboard")
        btn_agenda = QPushButton("📅 Agenda")
        btn_ia = QPushButton("🤖 Assistente IA")
        btn_relatorios = QPushButton("📊 Relatórios")
        btn_config = QPushButton("⚙️ Configurações")

        layout.addWidget(titulo)
        layout.addSpacing(30)

        layout.addWidget(btn_dashboard)
        layout.addWidget(btn_agenda)
        layout.addWidget(btn_ia)
        layout.addWidget(btn_relatorios)

        layout.addStretch()

        layout.addWidget(btn_config)

        self.setLayout(layout)