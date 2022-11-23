from PySide6.QtWidgets import QWidget,QLabel,QApplication
from PySide6.QtCore import Qt
from ___Keys___ import toggle_key


class TransParentWidget(QWidget):
    screen = QApplication.primaryScreen()
    def __init__(self):
        super().__init__()
        self.move(self.screen.size().width() - 200, self.screen.size().height() - 810)
        self.resize(self.screen.size().width(),self.screen.size().height())
        self.setWindowFlag(Qt.WindowStaysOnTopHint, on=True)
        self.setWindowFlag(Qt.FramelessWindowHint, on=True)
        self.setAttribute(Qt.WA_TranslucentBackground, on=True)

        self.AddLabels()
        self.SetLabelsStyle()
    def AddLabels(self):
        self.label1 = QLabel("Toggle Key : {}".format(toggle_key), self)

        self.label2 = QLabel("Macro Status : Disabled",self)
        self.label2.move(self.label1.x(),self.label1.y() + 22)
    def SetLabelsStyle(self):
        self.label1.setStyleSheet(
            "font-size : 15px;"
            "color: red;"
            "background-color: yellow;"
        )
        self.label2.setStyleSheet(
            "font-size : 15px;"
            "color: red;"
            "background-color: yellow;"
        )
    def closeEvent(self, event):
        pass

trans_parent_widget = TransParentWidget()