from PySide2.QtWidgets import QMainWindow

from gui.ui_MainWindow import Ui_MainWindow


class WindowNatillera(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        # Window Config
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(1030, 600)
        self.show()
