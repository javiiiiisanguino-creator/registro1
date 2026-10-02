import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QDialog,
    QLabel, QPushButton, QLineEdit, QTextEdit,
    QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout,
    QCheckBox, QRadioButton, QComboBox, QMessageBox,
    QTabWidget, QButtonGroup
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor, QPalette

BLUE_DARK = "#1a237e"
BLUE_MED = "#283593"
BLUE_LIGHT = "#3949ab"
BLUE_ACCENT = "#5c6bc0"
BLUE_PALE = "#e8eaf6"
WHITE = "#ffffff"
GRAY_LIGHT = "#f5f5f5"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Farmacia - Registro de Clientes")
        self.setMinimumSize(700, 650)
        self.setStyleSheet(self._main_style())

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 15, 20, 15)

        # Header
        header = QLabel("Farmacia Vida Sana")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setFont(QFont("Segoe UI", 22, QFont.Weight.Bold))
        header.setStyleSheet(f"color: {WHITE}; background: {BLUE_DARK}; padding: 18px; border-radius: 8px;")
        layout.addWidget(header)

        subtitle = QLabel("Formulario de Registro de Clientes")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setFont(QFont("Segoe UI", 11))
        subtitle.setStyleSheet(f"color: {BLUE_DARK}; padding: 4px;")
        layout.addWidget(subtitle)

        # Tabs area using QTabWidget
        tabs = QTabWidget()
        tabs.setStyleSheet(self._tab_style())
        tabs.addTab(self._tab_datos_personales(), "Datos Personales")
        tabs.addTab(self._tab_datos_contacto(), "Contacto")
        tabs.addTab(self._tab_datos_salud(), "Salud")
        tabs.addTab(self._tab_observaciones(), "Observaciones")
        layout.addWidget(tabs)

        # Botones inferiores
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)

        btn_cancelar = QPushButton("Cancelar")
        btn_cancelar.setFixedHeight(40)
        btn_cancelar.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_cancelar.setStyleSheet(self._btn_style("#b0bec5", "#78909c"))
        btn_cancelar.clicked.connect(self.close)
        btn_layout.addWidget(btn_cancelar)

        btn_limpiar = QPushButton("Limpiar")
        btn_limpiar.setFixedHeight(40)
        btn_limpiar.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_limpiar.setStyleSheet(self._btn_style(BLUE_ACCENT, BLUE_LIGHT))
        btn_limpiar.clicked.connect(self._limpiar)
        btn_layout.addWidget(btn_limpiar)

        btn_registrar = QPushButton("Registrar Cliente")
        btn_registrar.setFixedHeight(40)
        btn_registrar.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_registrar.setStyleSheet(self._btn_style(BLUE_MED, BLUE_DARK))
        btn_registrar.clicked.connect(self._registrar)
        btn_layout.addWidget(btn_registrar)

        layout.addLayout(btn_layout)

        # Footer
        footer = QLabel("Realizado por Javier Sanguino - 2026")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer.setFont(QFont("Segoe UI", 9))
        footer.setStyleSheet(f"color: {BLUE_DARK}; background: {BLUE_PALE}; padding: 6px; border-radius: 6px;")
        layout.addWidget(footer)

    # ── Pestaña 1: Datos Personales ──────────────────────────
    def _tab_datos_personales(self):
        w = QWidget()
        outer = QVBoxLayout(w)
        outer.setContentsMargins(15, 15, 15, 15)

        form = QFormLayout()
        form.setSpacing(10)
        form.setLabelAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Nombre completo")
        form.addRow("Nombre:", self.input_nombre)

        self.input_dpi = QLineEdit()
        self.input_dpi.setPlaceholderText("N. de identificacion")
        form.addRow("DPI / ID:", self.input_dpi)

        self.input_fecha_nac = QLineEdit()
        self.input_fecha_nac.setPlaceholderText("DD/MM/AAAA")
        form.addRow("Fecha nacimiento:", self.input_fecha_nac)

        # Radio buttons: sexo
        sexo_layout = QHBoxLayout()
        self.radio_masculino = QRadioButton("Masculino")
        self.radio_femenino = QRadioButton("Femenino")
        self.radio_otro = QRadioButton("Otro")
        sexo_layout.addWidget(self.radio_masculino)
        sexo_layout.addWidget(self.radio_femenino)
        sexo_layout.addWidget(self.radio_otro)
        sexo_layout.addStretch()

        self.grupo_sexo = QButtonGroup(self)
        self.grupo_sexo.setExclusive(True)
        for i, boton in enumerate(
            (self.radio_masculino, self.radio_femenino, self.radio_otro)
        ):
            self.grupo_sexo.addButton(boton, i)
        form.addRow("Sexo:", sexo_layout)

        # Combo: tipo de sangre
        self.combo_sangre = QComboBox()
        self.combo_sangre.addItems(["Seleccione...", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        form.addRow("Tipo de sangre:", self.combo_sangre)

        # Combo: estado civil
        self.combo_estado_civil = QComboBox()
        self.combo_estado_civil.addItems(["Seleccione...", "Soltero(a)", "Casado(a)", "Divorciado(a)", "Viudo(a)", "Union libre"])
        form.addRow("Estado civil:", self.combo_estado_civil)

        outer.addLayout(form)
        return w

    # ── Pestaña 2: Contacto ──────────────────────────────────
    def _tab_datos_contacto(self):
        w = QWidget()
        outer = QVBoxLayout(w)
        outer.setContentsMargins(15, 15, 15, 15)

        form = QFormLayout()
        form.setSpacing(10)
        form.setLabelAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.input_telefono = QLineEdit()
        self.input_telefono.setPlaceholderText("+502 0000-0000")
        form.addRow("Telefono:", self.input_telefono)

        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("correo@ejemplo.com")
        form.addRow("Email:", self.input_email)

        self.input_direccion = QLineEdit()
        self.input_direccion.setPlaceholderText("Direccion completa")
        form.addRow("Direccion:", self.input_direccion)

        self.input_municipio = QLineEdit()
        self.input_municipio.setPlaceholderText("Municipio / Ciudad")
        form.addRow("Municipio:", self.input_municipio)

        self.combo_departamento = QComboBox()
        self.combo_departamento.addItems([
            "Seleccione...", "Guatemala", "Alta Verapaz", "Baja Verapaz",
            "Chimaltenango", "Chiquimula", "El Progreso", "Escuintla",
            "Huehuetenango", "Izabal", "Jalapa", "Jutiapa", "Petén",
            "Quetzaltenango", "Quiché", "Retalhuleu", "Sacatepéquez",
            "San Marcos", "Santa Rosa", "Sololá", "Suchitepéquez",
            "Totonicapán", "Zacapa"
        ])
        form.addRow("Departamento:", self.combo_departamento)

        self.chk_notificaciones = QCheckBox("Recibir notificaciones por email")
        self.chk_notificaciones.setChecked(True)
        form.addRow(self.chk_notificaciones)

        self.chk_sms = QCheckBox("Recibir alertas por SMS")
        form.addRow(self.chk_sms)

        outer.addLayout(form)
        return w

    # ── Pestaña 3: Salud ─────────────────────────────────────
    def _tab_datos_salud(self):
        w = QWidget()
        outer = QVBoxLayout(w)
        outer.setContentsMargins(15, 15, 15, 15)

        form = QFormLayout()
        form.setSpacing(10)
        form.setLabelAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.combo_seguro = QComboBox()
        self.combo_seguro.addItems([
            "Seleccione...", "Ninguno", "IGSS", "Medicross",
            "GNN Palic", "Aseguradora General", "Mapfre", "Otro"
        ])
        form.addRow("Seguro medico:", self.combo_seguro)

        self.input_num_seguro = QLineEdit()
        self.input_num_seguro.setPlaceholderText("Numero de poliza")
        form.addRow("N. Poliza:", self.input_num_seguro)

        self.chk_diabetes = QCheckBox("Diabetes")
        self.chk_hipertension = QCheckBox("Hipertension")
        self.chk_asma = QCheckBox("Asma")
        self.chk_alergias = QCheckBox("Alergias")
        self.chk_cardiaco = QCheckBox("Enfermedad cardiaca")
        self.chk_otras = QCheckBox("Otras")

        grid = QGridLayout()
        grid.addWidget(self.chk_diabetes, 0, 0)
        grid.addWidget(self.chk_hipertension, 0, 1)
        grid.addWidget(self.chk_asma, 0, 2)
        grid.addWidget(self.chk_alergias, 1, 0)
        grid.addWidget(self.chk_cardiaco, 1, 1)
        grid.addWidget(self.chk_otras, 1, 2)
        form.addRow("Cond. medicas:", grid)

        self.input_alergias = QLineEdit()
        self.input_alergias.setPlaceholderText("Describa sus alergias si aplica")
        form.addRow("Alergias:", self.input_alergias)

        self.input_medicamentos = QLineEdit()
        self.input_medicamentos.setPlaceholderText("Medicamentos que toma actualmente")
        form.addRow("Medicamentos actuales:", self.input_medicamentos)

        outer.addLayout(form)
        return w

    # ── Pestaña 4: Observaciones ─────────────────────────────
    def _tab_observaciones(self):
        w = QWidget()
        outer = QVBoxLayout(w)
        outer.setContentsMargins(15, 15, 15, 15)

        lbl = QLabel("Observaciones adicionales:")
        lbl.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        lbl.setStyleSheet(f"color: {BLUE_DARK};")
        outer.addWidget(lbl)

        self.text_observaciones = QTextEdit()
        self.text_observaciones.setPlaceholderText(
            "Escriba aqui cualquier informacion adicional relevante...\n\n"
            "- Preferencias del cliente\n"
            "- Restricciones alimentarias\n"
            "- Notas del farmaceutico"
        )
        self.text_observaciones.setStyleSheet(
            f"QTextEdit {{ border: 2px solid {BLUE_ACCENT}; border-radius: 6px; "
            f"padding: 8px; font-size: 10pt; background: {WHITE}; }}"
        )
        outer.addWidget(self.text_observaciones)

        grid = QGridLayout()
        grid.setSpacing(8)

        self.chk_acepto_terminos = QCheckBox("Acepto los terminos y condiciones")
        grid.addWidget(self.chk_acepto_terminos, 0, 0, 1, 2)

        self.chk_habeas_data = QCheckBox("Acepto el tratamiento de mis datos personales")
        grid.addWidget(self.chk_habeas_data, 1, 0, 1, 2)

        self.chk_venta_controlada = QCheckBox("Entiendo las normas de medicamentos controlados")
        grid.addWidget(self.chk_venta_controlada, 2, 0, 1, 2)

        outer.addLayout(grid)
        return w

    # ── Acciones ─────────────────────────────────────────────
    def _limpiar(self):
        for w in self.findChildren(QLineEdit):
            w.clear()
        for w in self.findChildren(QTextEdit):
            w.clear()
        for w in self.findChildren(QCheckBox):
            w.setChecked(False)
        for w in self.findChildren(QComboBox):
            w.setCurrentIndex(0)
        self.grupo_sexo.setExclusive(False)
        for b in self.grupo_sexo.buttons():
            b.setChecked(False)
        self.grupo_sexo.setExclusive(True)

    def _registrar(self):
        nombre = self.input_nombre.text().strip()
        dpi = self.input_dpi.text().strip()

        if not nombre or not dpi:
            QMessageBox.warning(self, "Campos obligatorios",
                                "Por favor complete al menos el Nombre y el DPI/ID.")
            return

        if not self.chk_acepto_terminos.isChecked():
            QMessageBox.warning(self, "Terminos",
                                "Debe aceptar los terminos y condiciones.")
            return

        QMessageBox.information(self, "Registro exitoso",
                                f"Cliente '{nombre}' registrado correctamente.")

    # ── Estilos ──────────────────────────────────────────────
    def _main_style(self):
        return f"""
            QMainWindow {{ background: {GRAY_LIGHT}; }}
            QTabWidget::pane {{
                border: 2px solid {BLUE_ACCENT};
                border-radius: 6px;
                background: {WHITE};
            }}
        """

    def _tab_style(self):
        return f"""
            QTabBar::tab {{
                background: {BLUE_PALE};
                color: {BLUE_DARK};
                padding: 10px 22px;
                margin-right: 3px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                font-weight: bold;
            }}
            QTabBar::tab:selected {{
                background: {BLUE_MED};
                color: {WHITE};
            }}
            QTabBar::tab:hover {{
                background: {BLUE_LIGHT};
                color: {WHITE};
            }}
            QLineEdit, QComboBox, QTextEdit {{
                border: 2px solid {BLUE_ACCENT};
                border-radius: 5px;
                padding: 6px;
                font-size: 10pt;
                background: {WHITE};
                selection-background-color: {BLUE_LIGHT};
            }}
            QLineEdit:focus, QComboBox:focus, QTextEdit:focus {{
                border: 2px solid {BLUE_DARK};
            }}
            QComboBox::drop-down {{
                border: none;
                width: 24px;
            }}
            QCheckBox, QRadioButton {{
                spacing: 6px;
                font-size: 10pt;
            }}
            QCheckBox::indicator, QRadioButton::indicator {{
                width: 16px;
                height: 16px;
            }}
            QLabel {{
                font-size: 10pt;
            }}
        """

    def _btn_style(self, bg, hover):
        return f"""
            QPushButton {{
                background: {bg};
                color: {WHITE};
                border: none;
                border-radius: 6px;
                padding: 8px 18px;
                font-weight: bold;
                font-size: 10pt;
            }}
            QPushButton:hover {{
                background: {hover};
            }}
            QPushButton:pressed {{
                background: {BLUE_DARK};
            }}
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    palette = app.palette()
    palette.setColor(QPalette.ColorRole.Window, QColor(GRAY_LIGHT))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(BLUE_DARK))
    palette.setColor(QPalette.ColorRole.Base, QColor(WHITE))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(BLUE_LIGHT))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(WHITE))
    app.setPalette(palette)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
