from PySide6.QtWidgets import QWidget,QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from ___Threads___ import ToggleThread
from ___TransParentWidget___ import trans_parent_widget
from ___SettingWidget___ import setting_widget
import keyboard
class MainWidget(QWidget):
    screen = QApplication.primaryScreen()
    x_pos = 200
    y_pos = 0
    width = screen.size().width() - 500
    height = screen.size().height() - 200
    def __init__(self):
        super().__init__()
        self.SetTitle()
        self.SetTitleIcon()
        self.SetSizeandPos()
        self.setFocus()

        self.toggle_thread = ToggleThread()
        self.toggle_thread.start()

        trans_parent_widget.show()
    def SetTitle(self):
        self.setWindowTitle("HotKey Macro")
    def SetTitleIcon(self):
        self.setWindowIcon(QIcon("./Images/Keyboard.png"))
    def SetSizeandPos(self):
        self.move(self.x_pos,self.y_pos)
        self.resize(self.width,self.height)
    def resizeEvent(self, event):
        self.width = event.size().width()
        self.height = event.size().height()

        self.ResizeMainButtons()
        self.ReposMainButtons()

        self.ReizeMainScrollArea()
        self.ReposMainScrollArea()
    def ResizeMainButtons(self):
        from ___MainButtons___ import add_button,delete_button,settings_button,reset_button
        add_button.resize(self.width / 4,self.height / 25)
        delete_button.resize(self.width / 4,self.height / 25)
        reset_button.resize(self.width / 4, self.height / 25)
        settings_button.resize(self.width / 4,self.height / 25)
    def ReposMainButtons(self):
        from ___MainButtons___ import add_button,delete_button,settings_button,reset_button
        add_button.move(0,self.height / 30)
        delete_button.move(add_button.width() * 1,self.height / 30)
        reset_button.move(add_button.width() * 2, self.height / 30)
        settings_button.move(add_button.width() * 3,self.height / 30)
    def ReizeMainScrollArea(self):
        from ___MainScrollArea___ import main_scroll_area
        main_scroll_area.resize(self.width / 1.5,self.height / 1.2)
    def ReposMainScrollArea(self):
        from ___MainScrollArea___ import main_scroll_area
        main_scroll_area.move(self.width / 6,self.height / 10)
    def focusInEvent(self, event):
        pass
    def focusOutEvent(self, event):
        pass
    def closeEvent(self, event):
        trans_parent_widget.close()
        setting_widget.close()

main_widget = MainWidget()

