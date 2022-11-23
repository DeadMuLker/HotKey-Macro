from PySide6.QtWidgets import QPushButton,QMessageBox
from ___MainWidget___ import main_widget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from ___SettingWidget___ import setting_widget
import keyboard

class AddButton(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)
        self.setFocusPolicy(Qt.NoFocus)
        self.ClickTrigger()
    def ClickTrigger(self):
        self.clicked.connect(self.ClickAction)
    def ClickAction(self):
        # print("add button clicked")
        from ___MainScrollArea___ import main_scroll_frame,v_box_layout
        from ___GroupBox___ import GroupBox

        group_box = GroupBox()
        GroupBox.num_of_group += 1
        GroupBox.group_list.append(group_box)
        main_scroll_frame.resize(GroupBox.width,GroupBox.height * GroupBox.num_of_group)

        group_box.resize(group_box.width,group_box.height)
        group_box.setTitle("Key Group")
        v_box_layout.addWidget(group_box)

        # print("cur group num : ",len(GroupBox.group_list),GroupBox.num_of_group)

add_button = AddButton("Add",main_widget)

class DeleteButton(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)
        self.setFocusPolicy(Qt.NoFocus)
        self.ClickTrigger()
    def ClickTrigger(self):
        self.clicked.connect(self.ClickAction)
    def ClickAction(self):
        # print("delete button clicked")
        from ___MainScrollArea___ import main_scroll_frame, v_box_layout
        from ___GroupBox___ import GroupBox

        total_checked = 0
        for_delete_groups = []
        for group in GroupBox.group_list:
            if group.isChecked() == True:
                total_checked += 1
                for_delete_groups.append(group)

                group.hot_key_line.hot_key_list.clear()


        for group in for_delete_groups:
            GroupBox.group_list.remove(group)
            group.deleteLater()

        GroupBox.num_of_group -= total_checked
        main_scroll_frame.resize(GroupBox.width, GroupBox.height * GroupBox.num_of_group)

        # print("cur group num : ", len(GroupBox.group_list), GroupBox.num_of_groups)
        # print("total checked num : ",total_checked)

delete_button = DeleteButton("Delete",main_widget)

class SettingsButton(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)
        self.setFocusPolicy(Qt.NoFocus)
        self.ClickTrigger()
    def ClickTrigger(self):
        self.clicked.connect(self.ClickAction)
    def ClickAction(self):
        setting_widget.show()

settings_button = SettingsButton("Settings",main_widget)

class ResetButton(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)
        self.setFocusPolicy(Qt.NoFocus)
        self.ClickTriiger()
    def ClickTriiger(self):
        self.clicked.connect(self.ClickAction)
    def ClickAction(self):
        self.warning_message = QMessageBox()

        self.warning_message.setWindowTitle("Warning")
        self.warning_message.setWindowIcon(QIcon("./Images/Warning.png"))
        self.warning_message.setText("Do you really want to reset?")
        self.warning_message.setIcon(self.warning_message.Icon.Warning)

        self.warning_message.addButton(self.warning_message.StandardButton.Yes)
        self.warning_message.addButton(self.warning_message.StandardButton.No)

        self.result = self.warning_message.exec()
        if self.result == self.warning_message.StandardButton.Yes:
            self.YesButtonAction()
        elif self.result == self.warning_message.StandardButton.No:
            self.NoButtonAction()
    def YesButtonAction(self):
        # print("yes button clicked")
        from ___MainScrollArea___ import main_scroll_frame,v_box_layout
        from ___GroupBox___ import GroupBox

        GroupBox.num_of_group = 0
        main_scroll_frame.resize(0,0)

        for i in GroupBox.group_list:
            i.hot_key_line.hot_key_list.clear()
            if hasattr(i.hot_key_line, "hot_key_input_thread") == True:
                i.hot_key_line.hot_key_input_thread.terminate()
                i.hot_key_line.hot_key_input_thread.wait(1)
            i.repeat_count_line.repeat_count = ""
            if hasattr(i.repeat_count_line, "repeat_count_input_thread") == True:
                i.repeat_count_line.repeat_count_input_thread.terminate()
                i.repeat_count_line.repeat_count_input_thread.wait(1)

        for i in GroupBox.group_list:
            i.deleteLater()

        GroupBox.group_list.clear()
        # print("cur group num : ", len(GroupBox.group_list), GroupBox.num_of_groups)
    def NoButtonAction(self):
        pass
        # print("no button clicked")

reset_button = ResetButton("Reset",main_widget)


