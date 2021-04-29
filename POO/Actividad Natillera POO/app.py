import sys

from PySide2.QtWidgets import QApplication

from gui.gui import WindowNatillera


# Bootstrap
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WindowNatillera()
    
    sys.exit(app.exec_())