import sys
from PyQt6.QtWidgets import (
    QApplication, QFontComboBox, QLabel, QLineEdit, QMainWindow,
    QPushButton, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy, QFileDialog
)
from PyQt6.QtGui import QPixmap
from PIL import Image, ImageDraw, ImageFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Watermark Image")
        self.resize(400, 400)
        central_widget = QWidget()

        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(20)

        upload_image = QPushButton("Upload Image")
        layout.addWidget(upload_image)
        upload_image.clicked.connect(self.upload_img)

        self.image_label = QLabel('No image uploaded.')
        layout.addWidget(self.image_label)

        self.water_text = QLineEdit()
        self.water_text.setPlaceholderText("Add Watermark")
        layout.addWidget(self.water_text)

        self.button = QPushButton("Save")
        self.button.setFixedHeight(30)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.save_image)

        layout.addStretch(1)

        spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        layout.addItem(spacer)

        self.setCentralWidget(central_widget)

    def upload_img(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.xpm *.jpg)")
        if file_path:
            self.file_path = file_path
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap.scaled(250, 250))

    def save_image(self):
        if self.file_path:
            img = Image.open(self.file_path)
            draw = ImageDraw.Draw(img)
            watermark_text = self.water_text.text()

            my_font = ImageFont.truetype("FreeMono.ttf", 200)

            draw.text((10, 10), watermark_text, font=my_font, fill=(255, 255, 255))

            edited_file_path = "car2.png"
            img.save(edited_file_path)

            pixmap = QPixmap(edited_file_path)
            self.image_label.setPixmap(pixmap.scaled(250, 250))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
