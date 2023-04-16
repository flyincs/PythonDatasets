#这是第一个Python绘制的图形化测试程序
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('这是第一个Python图形程序')
window.setGeometry(100, 100, 600, 200)

label = QLabel('Hello, PyQt5!', window)
label.move(100, 80)

window.show()
sys.exit(app.exec_())