from ___MainWidget___ import main_widget
from PySide6.QtWidgets import QMenu,QMenuBar,QMessageBox,QFileDialog
from PySide6.QtGui import QAction,QIcon
from PySide6.QtCore import Signal,Slot,Qt,QFile,QFileInfo,QIODeviceBase,QIODevice,QByteArray
from ___Keys___ import allowed_key_list
from ___GroupBox___ import GroupBox
from ___MainScrollArea___ import main_scroll_frame,v_box_layout
import keyboard

class FileMenuBar(QMenuBar):
    def __init__(self,parent):
        super().__init__(parent)
        self.setFocusPolicy(Qt.NoFocus)
    def enterEvent(self, event):
        self.setEnabled(True)

file_menubar = FileMenuBar(main_widget)

class FileMenu(QMenu):
    def __init__(self,title,parent):
        super().__init__(title,parent)
        self.setFocusPolicy(Qt.NoFocus)
        self.AddMenu()
    def AddMenu(self):
        file_menubar.addMenu(self)

file_menu = FileMenu("File",file_menubar)

class FileActions():
    save_action = QAction("Save",file_menu)
    load_action = QAction("Load",file_menu)
    def __init__(self):
        self.AddActions()
        self.SaveClickTrigger()
        self.LoadClickTrigger()
        self.file_dialog = QFileDialog()
    def AddActions(self):
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.load_action)
    def SaveClickTrigger(self):
        self.save_action.triggered.connect(self.SaveAction)
    def SaveAction(self):
        self.file_dialog.setWindowTitle("Save")
        self.file_dialog.setNameFilters(["Macro Files (*.mco)"])
        self.file_dialog.setLabelText(self.file_dialog.DialogLabel.Accept, "Save")
        self.file_dialog.setLabelText(self.file_dialog.DialogLabel.Reject, "Cancel")

        result = self.file_dialog.exec()
        self.SaveFile(result)
    def SaveFile(self,result):
        if result == 1:
            print("save activated")
            file_info = QFileInfo(str(self.file_dialog.selectedFiles()[-1]))
            file_name = file_info.fileName()

            is_exist = self.CheckFileExist(file_name,file_info)
            if is_exist:
                message = QMessageBox()
                message.setWindowTitle("Error")
                message.setWindowIcon(QIcon("Error.png"))
                message.setText("file already exists")
                message.exec()
                return

            if ".mco" not in file_name:
                file = QFile("{}.{}".format(file_name,"mco"))
                is_openable = False
                is_openable = file.open(QIODeviceBase.ReadWrite)

                if is_openable == False:
                    print("file open error")
                    read_err_msg = QMessageBox()
                    read_err_msg.setWindowTitle("Error")
                    read_err_msg.setWindowIcon(QIcon("Error.png"))
                    read_err_msg.setText("File open error")
                    read_err_msg.exec()
                    file.close()
                    return
            else:
                file = QFile(file_name)
                is_openable = False
                is_openable = file.open(QIODeviceBase.ReadWrite)

                if is_openable == False:
                    print("file open error")
                    read_err_msg = QMessageBox()
                    read_err_msg.setWindowTitle("Error")
                    read_err_msg.setWindowIcon(QIcon("Error.png"))
                    read_err_msg.setText("File open error")
                    read_err_msg.exec()
                    file.close()
                    return
            
            is_readable = self.ReadGroupCount(GroupBox.group_list,GroupBox.num_of_group)
            if is_readable == True:
                pass
            else:
                read_err_msg = QMessageBox()
                read_err_msg.setWindowTitle("Error")
                read_err_msg.setWindowIcon(QIcon("Error.png"))
                read_err_msg.setText("Read Group Error\n"
                                     "please input data or check data")
                read_err_msg.exec()
                file.close()
                if ".mco" not in file_name:
                    file.remove("{}.{}".format(file_name,"mco"))
                else:
                    file.remove(file_name)
                return

            is_readable = self.ReadGroupHotKeyList(GroupBox.group_list)
            if is_readable == True:
                pass
            else:
                print("is readable :",is_readable)
                read_err_msg = QMessageBox()
                read_err_msg.setWindowTitle("Error")
                read_err_msg.setWindowIcon(QIcon("Error.png"))
                read_err_msg.setText("Read Group Hot Key Error\n"
                                     "please input data or check data")
                read_err_msg.exec()
                file.close()
                if ".mco" not in file_name:
                    file.remove("{}.{}".format(file_name,"mco"))
                else:
                    file.remove(file_name)
                return

            is_readable = self.ReadGroupRepeatCount(GroupBox.group_list,GroupBox.RepeatCountLine.max_repeat_count)
            if is_readable == True:
                pass
            else:
                read_err_msg = QMessageBox()
                read_err_msg.setWindowTitle("Error")
                read_err_msg.setWindowIcon(QIcon("Error.png"))
                read_err_msg.setText("Read Group Repeat Count Error\n"
                                     "please input data or check data")
                read_err_msg.exec()
                file.close()
                if ".mco" not in file_name:
                    file.remove("{}.{}".format(file_name, "mco"))
                else:
                    file.remove(file_name)
                return

            is_readable = self.ReadGroupIntervalDelay(GroupBox.group_list)
            if is_readable == True:
                pass
            else:
                read_err_msg = QMessageBox()
                read_err_msg.setWindowTitle("Error")
                read_err_msg.setWindowIcon(QIcon("Error.png"))
                read_err_msg.setText("Read Interval Delay Error\n"
                                     "please input data or check data")
                read_err_msg.exec()
                file.close()
                if ".mco" not in file_name:
                    file.remove("{}.{}".format(file_name, "mco"))
                else:
                    file.remove(file_name)
                return

            is_readable = self.ReadGroupKeyList(GroupBox.group_list)
            if is_readable == True:
                pass
            else:
                read_err_msg = QMessageBox()
                read_err_msg.setWindowTitle("Error")
                read_err_msg.setWindowIcon(QIcon("Error.png"))
                read_err_msg.setText("Read Group Key List Error\n"
                                     "please input data or check data")
                read_err_msg.exec()
                file.close()
                if ".mco" not in file_name:
                    file.remove("{}.{}".format(file_name, "mco"))
                else:
                    file.remove(file_name)
                return

            self.WriteData(file,GroupBox.group_list)
            file.close()
        else:
            print("save cancelled")
    def CheckFileExist(self,file_name,file_info):
        if ".mco" not in file_name:
            file_name += ".mco"
        result = file_info.exists(file_name)
        return result
    def ReadGroupCount(self,group_list,num_of_group):
        try:
            if num_of_group >= 1:
                return True
            else:
                return False
        except:
            return None
    def ReadGroupHotKeyList(self,group_list):
        try:
            for group in group_list:
                hot_key_list = group.hot_key_line.hot_key_list
                if len(hot_key_list) == 0:
                    return False
            return True
        except:
            return None
    def ReadGroupRepeatCount(self,group_list,max_repeat_count):
        try:
            for group in group_list:
                if len(group.repeat_count_line.repeat_count) == 0 or \
                        int(group.repeat_count_line.repeat_count) > max_repeat_count:
                    return False
                else:
                    return True
        except:
            return None
    def ReadGroupIntervalDelay(self,group_list):
        try:
            for group in group_list:
                interval_delay = float(group.interval_delay_line.interval_delay)
            return True
        except:
            return None
    def ReadGroupKeyList(self,group_list):
        try:
            for group in group_list:
                key_list = group.key_list_line.key_list
                if len(key_list) == 0:
                    return False
            return True
        except:
            return None
    def WriteData(self,file,group_list):
        file.write(QByteArray("num_of_group = {}\r\n".format(len(group_list))))
        file.write(QByteArray("\r\n"))

        for group_index,group in enumerate(group_list,start=1):
            file.write(QByteArray("(group {})\r\n".format(group_index)))

            file.write(QByteArray("hot_key_list = ["))
            hot_key_list = group.hot_key_line.hot_key_list
            for hot_key_index,hot_key in enumerate(hot_key_list,start=1):
                if len(hot_key_list) == hot_key_index:
                    if hot_key == ".":
                        file.write(QByteArray("full stop"))
                        file.write(QByteArray("]\r\n"))
                    elif hot_key == ",":
                        file.write(QByteArray("comma"))
                        file.write(QByteArray("]\r\n"))
                    else:
                        file.write(QByteArray(str(hot_key)))
                        file.write(QByteArray("]\r\n"))
                else:
                    if hot_key == ".":
                        file.write(QByteArray("full stop"))
                        file.write(QByteArray(","))
                    elif hot_key == ",":
                        file.write(QByteArray("comma"))
                        file.write(QByteArray(","))
                    else:
                        file.write(QByteArray(str(hot_key)))
                        file.write(QByteArray(","))

            file.write(QByteArray("repeat_count = {}\r\n".format(int(group.repeat_count_line.repeat_count))))
            file.write(QByteArray("interval_delay = {}\r\n".format(float(group.interval_delay_line.interval_delay))))

            file.write(QByteArray("Key_list = ["))
            key_list = group.key_list_line.key_list
            for key_index,key in enumerate(key_list,start=1):
                if len(key_list) == key_index:
                    if key == ".":
                        file.write(QByteArray("full stop"))
                        file.write(QByteArray("]\r\n\r\n"))
                    elif key == ",":
                        file.write(QByteArray("comma"))
                        file.write(QByteArray("]\r\n\r\n"))
                    else:
                        file.write(QByteArray(str(key)))
                        file.write(QByteArray("]\r\n\r\n"))
                else:
                    if key == ".":
                        file.write(QByteArray("full stop"))
                        file.write(QByteArray(","))
                    elif key == ",":
                        file.write(QByteArray("comma"))
                        file.write(QByteArray(","))
                    else:
                        file.write(QByteArray(str(key)))
                        file.write(QByteArray(","))
    def LoadClickTrigger(self):
        self.load_action.triggered.connect(self.LoadAction)
    def LoadAction(self,result):
        self.file_dialog.setWindowTitle("Load")
        self.file_dialog.setNameFilters(["Macro Files (*.mco)", "All Files (*.*)"])
        self.file_dialog.setLabelText(self.file_dialog.DialogLabel.Accept, "Load")
        self.file_dialog.setLabelText(self.file_dialog.DialogLabel.Reject, "Cancel")
        self.file_dialog.selectFile(".")

        result = self.file_dialog.exec()
        self.LoadFile(result)
    def LoadFile(self,result):
        readed_data = ""
        if result == 1:
            print("Load activated")
            file_info = QFileInfo(str(self.file_dialog.selectedFiles()[-1]))
            file_name = file_info.fileName()

            file = QFile(file_name)
            is_openable = file.open(QIODeviceBase.ReadOnly)
            if is_openable == False:
                open_err_msg = QMessageBox()
                open_err_msg.setWindowTitle("Error")
                open_err_msg.setText("File open error")
                open_err_msg.setWindowIcon(QIcon("Error.png"))
                open_err_msg.exec()
                file.close()
                return

            try:
                while file.atEnd() == False:
                    readed_data += file.read(1)
            except:
                open_err_msg = QMessageBox()
                open_err_msg.setWindowTitle("Error")
                open_err_msg.setText("File read error")
                open_err_msg.setWindowIcon(QIcon("Error.png"))
                open_err_msg.exec()
                file.close()
                return

            #print(readed_data)

            each_data = ""
            global num_of_group
            num_of_group = 0
            global hot_key_lists
            hot_key_lists = []
            global repeat_counts
            repeat_counts = []
            global interval_delays
            interval_delays = []
            global key_lists
            key_lists = []

            for char in readed_data:
                each_data += char

                if "\r\n" in each_data:
                    is_readable = self.ReadFileNumOfGroup(each_data)
                    if is_readable == True:
                        pass
                    elif is_readable == False:
                        pass
                    elif is_readable == None:
                        err_msg = QMessageBox()
                        err_msg.setWindowTitle("Error")
                        err_msg.setText("num_of_group read error")
                        err_msg.setWindowIcon(QIcon("Error.png"))
                        err_msg.exec()
                        file.close()
                        return

                    is_readable = self.ReadFileHotKeyList(each_data)
                    if is_readable == True:
                        pass
                    elif is_readable == False:
                        pass
                    elif is_readable == None:
                        err_msg = QMessageBox()
                        err_msg.setWindowTitle("Error")
                        err_msg.setText("hot_key_list read error")
                        err_msg.setWindowIcon(QIcon("Error.png"))
                        err_msg.exec()
                        file.close()
                        return

                    is_readable = self.ReadFileRepeatCount(each_data)
                    if is_readable == True:
                        pass
                    elif is_readable == False:
                        pass
                    elif is_readable == None:
                        err_msg = QMessageBox()
                        err_msg.setWindowTitle("Error")
                        err_msg.setText("repeat_count read error")
                        err_msg.setWindowIcon(QIcon("Error.png"))
                        err_msg.exec()
                        file.close()
                        return

                    is_readable = self.ReadFileIntervalDelay(each_data)
                    if is_readable == True:
                        pass
                    elif is_readable == False:
                        pass
                    elif is_readable == None:
                        err_msg = QMessageBox()
                        err_msg.setWindowTitle("Error")
                        err_msg.setText("interval delay read error")
                        err_msg.setWindowIcon(QIcon("Error.png"))
                        err_msg.exec()
                        file.close()
                        return

                    is_readable = self.ReadFileKeyList(each_data)
                    if is_readable == True:
                        pass
                    elif is_readable == False:
                        pass
                    elif is_readable == None:
                        err_msg = QMessageBox()
                        err_msg.setWindowTitle("Error")
                        err_msg.setText("Key list read error")
                        err_msg.setWindowIcon(QIcon("Error.png"))
                        err_msg.exec()
                        file.close()
                        return
                    each_data = ""

            ###read last saved each_data
            is_readable = self.ReadFileNumOfGroup(each_data)
            if is_readable == True:
                pass
            elif is_readable == False:
                pass
            elif is_readable == None:
                err_msg = QMessageBox()
                err_msg.setWindowTitle("Error")
                err_msg.setText("num_of_group read error")
                err_msg.setWindowIcon(QIcon("Error.png"))
                err_msg.exec()
                file.close()
                return

            is_readable = self.ReadFileHotKeyList(each_data)
            if is_readable == True:
                pass
            elif is_readable == False:
                pass
            elif is_readable == None:
                err_msg = QMessageBox()
                err_msg.setWindowTitle("Error")
                err_msg.setText("hot_key_list read error")
                err_msg.setWindowIcon(QIcon("Error.png"))
                err_msg.exec()
                file.close()
                return

            is_readable = self.ReadFileRepeatCount(each_data)
            if is_readable == True:
                pass
            elif is_readable == False:
                pass
            elif is_readable == None:
                err_msg = QMessageBox()
                err_msg.setWindowTitle("Error")
                err_msg.setText("repeat_count read error")
                err_msg.setWindowIcon(QIcon("Error.png"))
                err_msg.exec()
                file.close()
                return

            is_readable = self.ReadFileIntervalDelay(each_data)
            if is_readable == True:
                pass
            elif is_readable == False:
                pass
            elif is_readable == None:
                err_msg = QMessageBox()
                err_msg.setWindowTitle("Error")
                err_msg.setText("interval delay read error")
                err_msg.setWindowIcon(QIcon("Error.png"))
                err_msg.exec()
                file.close()
                return

            is_readable = self.ReadFileKeyList(each_data)
            if is_readable == True:
                pass
            elif is_readable == False:
                pass
            elif is_readable == None:
                err_msg = QMessageBox()
                err_msg.setWindowTitle("Error")
                err_msg.setText("Key list read error")
                err_msg.setWindowIcon(QIcon("Error.png"))
                err_msg.exec()
                file.close()
                return

            # print("num of group = ", num_of_group)
            # print("hot key lists = ", hot_key_lists)
            # print("repeat counts = ", repeat_counts)
            # print("interval delays = ", interval_delays)
            # print("key lists = ", key_lists)
            # print("-------------------------------------------")
            result = self.CheckFileDataMatched()
            if result == False:
                err_msg = QMessageBox()
                err_msg.setWindowTitle("Error")
                err_msg.setText("file not matched\r"
                                "please check file")
                err_msg.setWindowIcon(QIcon("Error.png"))
                err_msg.exec()
                file.close()
                return

            self.AddSavedData()
            print("yes")
            file.close()
        else:
            print("load cancelled")
    def ReadFileNumOfGroup(self,each_data):
        global num_of_group
        group_count = ""

        try:
            if "num_of_group" in each_data:
                for char in each_data:
                    if char.isdecimal():
                        group_count += char

                num_of_group = int(group_count)
                return True
            else:
                return False
        except:
            return None
    def ReadFileHotKeyList(self,each_data):
        global hot_key_lists
        hot_key_list = []
        try:
            if "hot_key_list" in each_data and "[" and  "]" in each_data:
                start_index = each_data.index("[")
                for index,char in enumerate(each_data):
                    if each_data[index] == "]":
                        last_index = index

                saved_str = ""
                for index,char in enumerate(each_data[start_index + 1:last_index],start=start_index):
                    saved_str += char

                    if char == ",":
                        saved_str = saved_str[:-1]
                        saved_str = saved_str.strip()

                        for key in allowed_key_list:
                            if saved_str == key:
                                hot_key_list.append(key)
                                break
                            if saved_str == "comma":
                                hot_key_list.append(",")
                                break
                            if saved_str == "full stop":
                                hot_key_list.append(".")
                                break

                        saved_str = ""

                for key in allowed_key_list:
                    if saved_str == key:
                        hot_key_list.append(key)
                        break
                    if saved_str == "comma":
                        hot_key_list.append(",")
                        break
                    if saved_str == "full stop":
                        hot_key_list.append(".")
                        break

                if len(hot_key_list) > GroupBox.HotKeyLine.hot_key_max_count:
                    return False
                else:
                    hot_key_lists.append(hot_key_list)
                return True
            else:
                return False
        except:
            return None
    def ReadFileRepeatCount(self,each_data):
        global repeat_counts
        repeat_count = ""

        try:
            if "repeat_count" in each_data:
                for char in each_data:
                    if char.isdecimal():
                        repeat_count += char

                if int(repeat_count) > GroupBox.RepeatCountLine.max_repeat_count:
                    return False
                else:
                    repeat_counts.append(int(repeat_count))
                    return True
            else:
                return False
        except:
            return None
    def ReadFileIntervalDelay(self,each_data):
        global interval_delays
        interval_delay = ""

        try:
            if "interval_delay" in each_data:
                for char in each_data:
                    if char.isdecimal():
                        interval_delay += char
                    elif char == ".":
                        interval_delay += char

                interval_delays.append(float(interval_delay))
                return True
            else:
                return False
        except:
            return None
    def ReadFileKeyList(self,each_data):
        global key_lists
        key_list = []
        try:
            if "Key_list" in each_data and "[" and "]" in each_data:
                start_index = each_data.index("[")
                for index, char in enumerate(each_data):
                    if each_data[index] == "]":
                        last_index = index

                saved_str = ""
                for index, char in enumerate(each_data[start_index + 1:last_index], start=start_index):
                    saved_str += char

                    if char == ",":
                        saved_str = saved_str[:-1]
                        saved_str = saved_str.strip()

                        for key in allowed_key_list:
                            if saved_str == key:
                                key_list.append(key)
                                break
                            if saved_str == "comma":
                                key_list.append(",")
                                break
                            if saved_str == "full stop":
                                key_list.append(".")
                                break

                        saved_str = ""

                for key in allowed_key_list:
                    if saved_str == key:
                        key_list.append(key)
                        break
                    if saved_str == "comma":
                        key_list.append(",")
                        break
                    if saved_str == "full stop":
                        key_list.append(".")
                        break

                if len(key_list) > GroupBox.KeyListLine.key_list_max_count:
                    return False
                else:
                    key_lists.append(key_list)
                return True
            else:
                return False
        except:
            return None
    def CheckFileDataMatched(self):
        global num_of_group
        global hot_key_lists
        global repeat_counts
        global interval_delays
        global key_lists

        if num_of_group == 0:
            return False
        elif num_of_group > 0:
            if len(hot_key_lists) == num_of_group:
                pass
            else:
                return False
            if len(repeat_counts) == num_of_group:
                pass
            else:
                return False
            if len(interval_delays) == num_of_group:
                pass
            else:
                return False
            if len(key_lists) == num_of_group:
                pass
            else:
                return False

            return True
        else:
            return False
    def AddSavedData(self):
        global num_of_group
        global hot_key_lists
        global repeat_counts
        global interval_delays
        global key_lists
        self.ResetGroup()

        for i in range(num_of_group):
            group_box = GroupBox()
            GroupBox.num_of_group += 1
            GroupBox.group_list.append(group_box)
            main_scroll_frame.resize(GroupBox.width, GroupBox.height * GroupBox.num_of_group)

            group_box.resize(group_box.width, group_box.height)
            group_box.setTitle("Key Group")
            v_box_layout.addWidget(group_box)

        self.AddHotKeyList()
        self.AddRepeatCount()
        self.AddIntervalDelay()
        self.AddKeyList()
    def ResetGroup(self):
        GroupBox.num_of_group = 0
        main_scroll_frame.resize(0, 0)

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
    def AddHotKeyList(self):
        global hot_key_lists

        for group in GroupBox.group_list:
            hot_key_list = hot_key_lists[0]

            for hot_key in hot_key_list:
                group.hot_key_line.hot_key_list.append(hot_key)

            for_display_text = ""
            index = 1
            for key in group.hot_key_line.hot_key_list:
                if key == "+":
                    for_display_text += "(+)"
                    if index != len(group.hot_key_line.hot_key_list):
                        for_display_text += " + "
                elif key == "right":
                    for_display_text += "\u2192"
                    if index != len(group.hot_key_line.hot_key_list):
                        for_display_text += " + "
                elif key == "left":
                    for_display_text += "\u2190"
                    if index != len(group.hot_key_line.hot_key_list):
                        for_display_text += " + "
                elif key == "up":
                    for_display_text += "\u2191"
                    if index != len(group.hot_key_line.hot_key_list):
                        for_display_text += " + "
                elif key == "down":
                    for_display_text += "\u2193"
                    if index != len(group.hot_key_line.hot_key_list):
                        for_display_text += " + "
                else:
                    for_display_text += key
                    if index != len(group.hot_key_line.hot_key_list):
                        for_display_text += " + "
                index += 1

            group.hot_key_line.setText(for_display_text)
            del hot_key_lists[0]
    def AddRepeatCount(self):
        global repeat_counts

        for group in GroupBox.group_list:
            repeat_count = repeat_counts[0]
            group.repeat_count_line.repeat_count = str(repeat_count)

            group.repeat_count_line.setText(str(repeat_count))
            del repeat_counts[0]
    def AddIntervalDelay(self):
        global interval_delays

        for group in GroupBox.group_list:
            interval_delay = interval_delays[0]
            group.interval_delay_line.interval_delay = str(interval_delay)

            group.interval_delay_line.setText(str(interval_delay))
            del interval_delays[0]
    def AddKeyList(self):
        global key_lists

        for group in GroupBox.group_list:
            key_list = key_lists[0]

            for key in key_list:
                group.key_list_line.key_list.append(key)

            for_display_text = ""
            index = 1
            for key in group.key_list_line.key_list:
                if key == "+":
                    for_display_text += "(+)"
                    if index != len(group.key_list_line.key_list):
                        for_display_text += " + "
                elif key == "right":
                    for_display_text += "\u2192"
                    if index != len(group.key_list_line.key_list):
                        for_display_text += " + "
                elif key == "left":
                    for_display_text += "\u2190"
                    if index != len(group.key_list_line.key_list):
                        for_display_text += " + "
                elif key == "up":
                    for_display_text += "\u2191"
                    if index != len(group.key_list_line.key_list):
                        for_display_text += " + "
                elif key == "down":
                    for_display_text += "\u2193"
                    if index != len(group.key_list_line.key_list):
                        for_display_text += " + "
                else:
                    for_display_text += key
                    if index != len(group.key_list_line.key_list):
                        for_display_text += " + "
                index += 1

            group.key_list_line.setText(for_display_text)
            del key_lists[0]

file_actions = FileActions()
