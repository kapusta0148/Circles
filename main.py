import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint

class CircleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.circles = []
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        x = random.randint(50, self.width() - 50)
        y = random.randint(100, self.height() - 50)
        radius = random.randint(10, 80)
        self.circles.append((x, y, radius))
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        for circle in self.circles:
            x, y, radius = circle
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(QPoint(x, y), radius, radius)
        qp.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleWindow()
    window.show()
    sys.exit(app.exec())
