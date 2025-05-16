import sys
from PyQt5.QtWidgets import (
    QWidget, QApplication, QTabWidget, QLabel, QPushButton,
    QVBoxLayout, QLineEdit, QFileDialog, QMessageBox, QComboBox
)
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt
from PIL import Image


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Converter By SergunaQQ")
        self.setGeometry(800, 300, 400, 300)
        self.initUI()
        self.set_dark_theme()

    def initUI(self):
        tab_widget = QTabWidget()
        image_tab = self.create_image_tab()
        tab_widget.addTab(image_tab, "Изображения")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)

    def create_image_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.image_input = QLineEdit()
        self.format_combo = QComboBox()
        self.format_combo.addItems(["PNG → JPG", "JPG → PNG"])

        btn_browse = QPushButton("Выбрать файл")
        btn_convert = QPushButton("Конвертировать")

        btn_browse.clicked.connect(self.browse_file)
        btn_convert.clicked.connect(self.convert_image)

        layout.addWidget(QLabel("Формат конвертации:"))
        layout.addWidget(self.format_combo)
        layout.addWidget(QLabel("Выберите файл:"))
        layout.addWidget(self.image_input)
        layout.addWidget(btn_browse)
        layout.addWidget(btn_convert)

        tab.setLayout(layout)
        return tab

    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Открыть изображение", "", "Изображения (*.png *.jpg *.jpeg)"
        )
        if file_name:
            self.image_input.setText(file_name)

    def convert_image(self):
        input_path = self.image_input.text()
        if not input_path:
            QMessageBox.warning(self, "Ошибка", "Не выбран файл!")
            return

        selected_format = self.format_combo.currentText()

        try:
            img = Image.open(input_path)

            if selected_format == "PNG → JPG":
                if not input_path.lower().endswith(".png"):
                    raise ValueError("Выберите .png файл для конвертации в .jpg")
                output_path = input_path.replace(".png", ".jpg")
                img.convert("RGB").save(output_path, "JPEG")

            elif selected_format == "JPG → PNG":
                if not (input_path.lower().endswith(".jpg") or input_path.lower().endswith(".jpeg")):
                    raise ValueError("Выберите .jpg или .jpeg файл для конвертации в .png")
                output_path = input_path.replace(".jpg", ".png").replace(".jpeg", ".png")
                img.save(output_path, "PNG")

            QMessageBox.information(self, "Готово", f"Файл сохранен как {output_path}")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def set_dark_theme(self):
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)

        app.setPalette(dark_palette)

        app.setStyleSheet("""
            QWidget {
                background-color: #191919;
                color: white;
                font-family: Arial, sans-serif;
                font-size: 12pt;
            }

            QPushButton {
                background-color: #323232;
                border: 1px solid #5a5a5a;
                padding: 5px 10px;
                border-radius: 5px;
                color: white;
            }
            QPushButton:hover {
                background-color: #4a4a4a;
            }
            QPushButton:pressed {
                background-color: #2e2e2e;
            }

            QComboBox {
                background-color: #323232;
                border: 1px solid #5a5a5a;
                padding: 5px;
                border-radius: 5px;
                color: white;
            }

            QLineEdit {
                background-color: #323232;
                border: 1px solid #5a5a5a;
                padding: 5px;
                border-radius: 5px;
                color: white;
            }

            QLabel {
                color: white;
            }

            QMessageBox {
                background-color: #252525;
                color: white;
            }
            QMessageBox QLabel {
                color: white;
            }
            QMessageBox QPushButton {
                background-color: #323232;
                border: 1px solid #5a5a5a;
                padding: 5px 10px;
                border-radius: 5px;
                color: white;
            }
            QMessageBox QPushButton:hover {
                background-color: #4a4a4a;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
