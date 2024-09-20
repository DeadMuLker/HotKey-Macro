from PySide6.QtWidgets import QLabel,QLineEdit,QGroupBox
from PySide6.QtCore import Qt
import keyboard
import asyncio
import time

class GroupBox(QGroupBox):
    num_of_group = 0
    group_list = []
    width = 1000
    height = 100
    def __init__(self):
        super().__init__()
        self.setCheckable(True)
        self.setChecked(False)

        self.InitHotKeyLabel()
        self.InitHotKeyLine()

        self.InitRepeatCountLabel()
        self.InitRepeatCountLine()

        self.InitIntervalDelayLabel()
        self.InitIntervalDelayLine()

        self.InitKeyListLabel()
        self.InitKeyListLine()
    def InitHotKeyLabel(self):
        self.hot_key_label = GroupBox.Label(self)
        self.hot_key_label.setFixedWidth(105)
        self.hot_key_label.setText("Hot Key (max : {}) :".format(GroupBox.HotKeyLine.hot_key_max_count))
        self.hot_key_label.move(0, 20)
    def InitHotKeyLine(self):
        self.hot_key_line = GroupBox.HotKeyLine(self)
        self.hot_key_line.setFixedWidth(250)
        self.hot_key_line.move(self.hot_key_label.x() + self.hot_key_label.width(),self.hot_key_label.y())
    def InitRepeatCountLabel(self):
        self.repeat_count_label = GroupBox.Label(self)
        self.repeat_count_label.setFixedWidth(142)
        self.repeat_count_label.setText("Repeat Count (max : {}) :".format(GroupBox.RepeatCountLine.max_repeat_count))
        self.repeat_count_label.move(self.hot_key_line.x() + self.hot_key_line.width() + 10,self.hot_key_line.y())
    def InitRepeatCountLine(self):
        self.repeat_count_line = GroupBox.RepeatCountLine(self)
        self.repeat_count_line.setFixedWidth(100)
        self.repeat_count_line.move(self.repeat_count_label.x() + self.repeat_count_label.width(),self.repeat_count_label.y())
    def InitIntervalDelayLabel(self):
        self.interval_delay_label = GroupBox.Label(self)
        self.interval_delay_label.setFixedWidth(112)
        self.interval_delay_label.setText("Interval Delay (sec) :")
        self.interval_delay_label.move(self.repeat_count_line.x() + self.repeat_count_line.width() + 10,self.repeat_count_line.y())
    def InitIntervalDelayLine(self):
        self.interval_delay_line = GroupBox.IntervalDelayLine(self)
        self.interval_delay_line.move(self.interval_delay_label.x() + self.interval_delay_label.width(),self.interval_delay_label.y())
    def InitKeyListLabel(self):
        self.key_list_label = GroupBox.Label(self)
        self.key_list_label.setFixedWidth(110)
        self.key_list_label.setText("Key List (max : {}) :".format(GroupBox.KeyListLine.key_list_max_count))
        self.key_list_label.move(self.hot_key_label.x(),self.hot_key_label.y() + 35)
    def InitKeyListLine(self):
        self.key_list_line = GroupBox.KeyListLine(self)
        self.key_list_line.setFixedWidth(500)
        self.key_list_line.move(self.key_list_label.x() + self.key_list_label.width(),self.key_list_label.y())
    class HotKeyLine(QLineEdit):
        hot_key_max_count = 3
        def __init__(self,parent):
            super().__init__(parent)
            self.hot_key_list = []
            self.input_thread = None
        # def enterEvent(self, event):
        #     from ___Threads___ import HotKeyInputThread
        #     from ___Menu___ import file_menubar
        #     file_menubar.setEnabled(False)
        #     self.setReadOnly(False)
        #     self.input_thread = HotKeyInputThread()
        #     self.input_thread.start()
        #     print(self.input_thread)
        # def leaveEvent(self,event):
        #     keyboard.unhook(self.input_thread.key_hook)
        #     from ___Menu___ import file_menubar
        #     file_menubar.setEnabled(True)
        #     self.setReadOnly(True)
        #     self.deselect()
        #     self.input_thread.stop()
        #     self.input_thread.join()
        #     self.input_thread = None
        def focusInEvent(self, event):
            from ___Threads___ import HotKeyInputThread
            from ___Menu___ import file_menubar
            file_menubar.setEnabled(False)
            self.setReadOnly(False)
            self.input_thread = HotKeyInputThread()
            self.input_thread.start()
        def focusOutEvent(self, event):
            keyboard.unhook(self.input_thread.key_hook)
            from ___Menu___ import file_menubar
            file_menubar.setEnabled(True)
            self.setReadOnly(True)
            self.deselect()
            self.input_thread.stop()
            self.input_thread.join()
            self.input_thread = None
    class RepeatCountLine(QLineEdit):
        max_repeat_count = 10
        def __init__(self,parent):
            super().__init__(parent)
            self.repeat_count = ""
            self.input_thread = None
        # def enterEvent(self,event):
        #     from ___Threads___ import RepeatCountInputThread
        #     from ___Menu___ import file_menubar
        #     file_menubar.setEnabled(False)
        #     self.setReadOnly(False)
        #     self.input_thread = RepeatCountInputThread()
        #     self.input_thread.start()
        # def leaveEvent(self,event):
        #     keyboard.unhook(self.input_thread.key_hook)
        #     from ___Menu___ import file_menubar
        #     file_menubar.setEnabled(True)
        #     self.setReadOnly(True)
        #     self.deselect()
        #     self.input_thread.stop()
        #     self.input_thread.join()
        def focusInEvent(self, event):
            from ___Threads___ import RepeatCountInputThread
            from ___Menu___ import file_menubar
            file_menubar.setEnabled(False)
            self.setReadOnly(False)
            self.input_thread = RepeatCountInputThread()
            self.input_thread.start()
        def focusOutEvent(self, event):
            keyboard.unhook(self.input_thread.key_hook)
            from ___Menu___ import file_menubar
            file_menubar.setEnabled(True)
            self.setReadOnly(True)
            self.deselect()
            self.input_thread.stop()
            self.input_thread.join()
            self.input_thread = None
    class IntervalDelayLine(QLineEdit):
        def __init__(self,parent):
            super().__init__(parent)
            self.interval_delay = ""
            self.setMaxLength(20)
            self.input_thread = None
        # def enterEvent(self, event):
        #     self.setReadOnly(False)
        #     from ___Threads___ import IntervalDelayInputThread
        #     from ___Menu___ import file_menubar
        #     file_menubar.setEnabled(False)
        #     self.setReadOnly(False)
        #     self.input_thread = IntervalDelayInputThread()
        #     self.input_thread.start()
        # def leaveEvent(self, event):
        #     keyboard.unhook(self.input_thread.key_hook)
        #     from ___Menu___ import file_menubar
        #     file_menubar.setEnabled(True)
        #     self.setReadOnly(True)
        #     self.deselect()
        #     self.input_thread.stop()
        #     self.input_thread.join()
        def focusInEvent(self, event):
            self.setReadOnly(False)
            from ___Threads___ import IntervalDelayInputThread
            from ___Menu___ import file_menubar
            file_menubar.setEnabled(False)
            self.setReadOnly(False)
            self.input_thread = IntervalDelayInputThread()
            self.input_thread.start()
        def focusOutEvent(self, event):
            keyboard.unhook(self.input_thread.key_hook)
            from ___Menu___ import file_menubar
            file_menubar.setEnabled(True)
            self.setReadOnly(True)
            self.deselect()
            self.input_thread.stop()
            self.input_thread.join()
            self.input_thread = None
    class KeyListLine(QLineEdit):
        key_list_max_count = 10
        def __init__(self,parent):
            super().__init__(parent)
            self.key_list = []
            self.input_thread = None
        # def enterEvent(self,event):
        #     from ___Threads___ import KeyListInputThread
        #     from ___Menu___ import file_menubar
        #     file_menubar.setEnabled(False)
        #     self.setReadOnly(False)
        #     self.input_thread = KeyListInputThread()
        #     self.input_thread.start()
        # def leaveEvent(self,event):
        #     keyboard.unhook(self.input_thread.key_hook)
        #     from ___Menu___ import file_menubar
        #     file_menubar.setEnabled(True)
        #     self.setReadOnly(True)
        #     self.deselect()
        #     self.input_thread.stop()
        #     self.input_thread.join()
        def focusInEvent(self, event):
            from ___Threads___ import KeyListInputThread
            from ___Menu___ import file_menubar
            file_menubar.setEnabled(False)
            self.setReadOnly(False)
            self.input_thread = KeyListInputThread()
            self.input_thread.start()
        def focusOutEvent(self, event):
            keyboard.unhook(self.input_thread.key_hook)
            from ___Menu___ import file_menubar
            file_menubar.setEnabled(True)
            self.setReadOnly(True)
            self.deselect()
            self.input_thread.stop()
            self.input_thread.join()
            self.input_thread = None
    class Label(QLabel):
        def __init__(self,parent):
            super().__init__(parent)

