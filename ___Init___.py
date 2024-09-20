from PySide6.QtWidgets import QApplication

app = QApplication([])

from ___MainWidget___ import *
from ___Menu___ import *
from ___MainButtons___ import *
from ___MainScrollArea___ import *

main_widget.show()
app.exec()
