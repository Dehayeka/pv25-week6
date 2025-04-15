import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette

class FontAdjuster(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Font Slider - Week 6 Assignment")

        self.label = QLabel("F1D022105")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 30))
        self.label.setAutoFillBackground(True)

        self.font_slider = self.create_slider(20, 60, 30, self.update_font_size, "Font Size")
        self.font_color_slider = self.create_slider(0, 255, 0, self.update_font_color, "Font Color (Grayscale)")
        self.bg_color_slider = self.create_slider(0, 255, 255, self.update_bg_color, "Background Color (Grayscale)")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(self.font_slider["layout"])
        layout.addLayout(self.font_color_slider["layout"])
        layout.addLayout(self.bg_color_slider["layout"])

        self.setLayout(layout)
        self.update_font_color()
        self.update_bg_color()

    def create_slider(self, min_val, max_val, default, callback, title):
        title_label = QLabel(title)
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue(default)
        slider.valueChanged.connect(callback)

        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(slider)

        return {"slider": slider, "layout": layout}

    def update_font_size(self):
        size = self.font_slider["slider"].value()
        font = self.label.font()
        font.setPointSize(size)
        self.label.setFont(font)

    def update_font_color(self):
        value = self.font_color_slider["slider"].value()
        color = QColor(value, value, value)
        palette = self.label.palette()
        palette.setColor(QPalette.WindowText, color)
        self.label.setPalette(palette)

    def update_bg_color(self):
        value = self.bg_color_slider["slider"].value()
        color = QColor(value, value, value)
        palette = self.label.palette()
        palette.setColor(QPalette.Window, color)
        self.label.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FontAdjuster()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec_())
