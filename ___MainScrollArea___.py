from PySide6.QtWidgets import QScrollArea,QLabel,QGroupBox,QLineEdit,QFrame,QVBoxLayout
from PySide6.QtCore import Qt
from ___MainWidget___ import main_widget

class MainScrollArea(QScrollArea):
    def __init__(self,parent):
        super().__init__(parent)

main_scroll_area = MainScrollArea(main_widget)

class MainScrollFrame(QFrame):
    def __init__(self):
        super().__init__(main_scroll_area)
        main_scroll_area.setWidget(self)

main_scroll_frame = MainScrollFrame()

class VBoxLayout(QVBoxLayout):
    def __init__(self):
        super().__init__(main_scroll_frame)

v_box_layout = VBoxLayout()


