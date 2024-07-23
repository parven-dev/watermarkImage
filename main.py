from PyQt6.QtGui import QPixmap

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QFontComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QSpacerItem,
    QSizePolicy,
    QFileDialog
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Water Mark Image")
        self.resize(400, 400)
        central_widget = QWidget()

        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(10, 10, 10, 10)

        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        upload_image = QPushButton("Upload Image")
        layout.addWidget(upload_image)
        upload_image.clicked.connect(self.upload_img)

        self.image_label = QLabel()
        layout.addWidget(self.image_label)

        self.water_text = QLineEdit()
        self.water_text.setPlaceholderText("Add Watermark")
        layout.addWidget(self.water_text)

        self.font = QFontComboBox()
        self.font.currentFontChanged.connect(self.fontChange)
        layout.addWidget(self.font)

        self.button = QPushButton("save")
        self.button.setFixedHeight(30)
        layout.addWidget(self.button)

        layout.addStretch(1)

        layout.addLayout(layout)

        spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        layout.addItem(spacer)

        self.setCentralWidget(central_widget)

    def upload_img(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Image Files(*.jpg *gif *png *.bmp")

        if fname:
            pxmap = QPixmap(fname)
            self.image_label.setPixmap(pxmap.scaled(250, 250))

    def fontChange(self, font):
        self.water_text.setFont(font)
        print(font)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
