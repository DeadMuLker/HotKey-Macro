from PySide6.QtWidgets import QWidget,QLabel,QApplication,QPushButton,QLineEdit
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from ___Keys___ import toggle_key
from ___TransParentWidget___ import trans_parent_widget
import keyboard
import ___Keys___

class SettingWidget(QWidget):
    screen = QApplication.primaryScreen()
    def __init__(self):
        super().__init__()
        self.setFocus()

        self.SetTitle()
        self.SetTitleIcon()
        self.SetSize()

        self.AddLabels()
        self.SetLabelsStyle()

        self.AddLines()
        self.SetLinesStyle()

        self.AddButtons()
        self.SetButtonsStyle()
    def SetTitle(self):
        self.setWindowTitle("Settings")
    def SetTitleIcon(self):
        self.setWindowIcon(QIcon("./Images/Setting.png"))
    def SetSize(self):
        self.resize(self.screen.size().width() / 2,self.screen.size().height() / 3)
    def AddLabels(self):
        self.label1 = QLabel("Macro Status :",self)

        self.label2 = QLabel("Disabled",self)
        self.label2.move(self.label1.x() + 170,self.label1.y())

        self.label3 = QLabel("Toggle Key :",self)
        self.label3.move(self.label1.x(),self.label1.y() + 50)

        self.label4 = QLabel("TransParent Widget :",self)
        self.label4.move(self.label3.x(),self.label3.y() + 50)
    def SetLabelsStyle(self):
        self.label1.setStyleSheet(
             "font-size : 25px;"
        )
        self.label2.setStyleSheet(
            "font-size : 25px;"
        )
        self.label3.setStyleSheet(
            "font-size : 25px;"
        )
        self.label4.setStyleSheet(
            "font-size : 25px;"
        )
    def AddLines(self):
        self.toggle_key_input_line = ToggleKeyLine(self)
        self.toggle_key_input_line.setText(toggle_key)
        self.toggle_key_input_line.move(self.label3.x() + 150,self.label3.y() + 5)
        self.toggle_key_input_line.setFixedSize(250, 30)
    def SetLinesStyle(self):
        self.toggle_key_input_line.setStyleSheet(
            "font-size : 25px;"
            "selection-color : yellow;"
        )
    def AddButtons(self):
        self.button1 = QPushButton("Hide",self)
        self.button1.move(self.label4.x() + 245,self.label4.y())
        self.button1.clicked.connect(self.Button1ClickAction)
    def SetButtonsStyle(self):
        self.button1.setStyleSheet(
            "font-size : 25px;"
        )
    def mousePressEvent(self, event):
        self.setFocus()
        trans_parent_widget.label1.setText("Toggle Key : {}".format(___Keys___.toggle_key))
    def focusOutEvent(self, event):
        trans_parent_widget.label1.setText("Toggle Key : {}".format(___Keys___.toggle_key))
    def Button1ClickAction(self):
        if self.button1.text() == "Hide":
            self.button1.setText("Show")
            trans_parent_widget.hide()
        else:
            self.button1.setText("Hide")
            trans_parent_widget.show()

class ToggleKeyLine(QLineEdit):
    def __init__(self,parent):
        super().__init__(parent)
    def focusInEvent(self, event):
        self.setReadOnly(True)
        from ___Threads___ import ToggleKeyLineThread
        self.setReadOnly(False)

        self.input_thread = ToggleKeyLineThread()
        self.input_thread.start()
    def focusOutEvent(self, event):
        keyboard.unhook(self.input_thread.key_hook)

        self.setReadOnly(True)
        self.deselect()
        self.input_thread.stop()
        self.input_thread.join()

        ___Keys___.toggle_key = self.text()
        trans_parent_widget.label1.setText("Toggle Key : {}".format(___Keys___.toggle_key))
        setting_widget.setFocus()

setting_widget = SettingWidget()
