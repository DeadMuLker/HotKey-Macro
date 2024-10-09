from ___Keys___ import *
from PySide6.QtWidgets import QLineEdit,QGroupBox
from PySide6.QtCore import Qt
from ___GroupBox___ import GroupBox
from ___SettingWidget___ import setting_widget
from ___TransParentWidget___ import trans_parent_widget
import sys
import keyboard
import threading
import time
import ___Keys___
import pynput
import ctypes

class HotKeyInputThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.state = True
        self.delay = 0.01
        self.key_hook = None
        from ___Keys___ import allowed_key_list,toggle_key
        from ___GroupBox___ import GroupBox
    def run(self):
        self.key_hook = keyboard.on_press(callback=self.OnPress)

        while self.state:
            time.sleep(self.delay)
    def stop(self):
        self.state = False
    def OnPress(self,event):
        group = (self.GroupFocused())[1]
        line = group.hot_key_line
        key_list = group.hot_key_line.hot_key_list
        max_count = GroupBox.HotKeyLine.hot_key_max_count
        line.setReadOnly(True)

        if event.name in allowed_key_list and event.name != toggle_key and (self.GroupFocused())[0]:
            if len(key_list) >= max_count:
                del key_list[-1:]
            key_list.append(event.name)
        elif event.name == "backspace" and event.name != toggle_key and (self.GroupFocused())[0]:
            if len(key_list) >= 1:
                del key_list[-1]

        self.DisplayKeyList(key_list, line)
    def GroupFocused(self):
        for group in GroupBox.group_list:
            if group.hot_key_line.hasFocus():
                return True,group
        return False,group
    def DisplayKeyList(self,key_list,line):
        for_display_text = ""
        index = 1
        for key in key_list:
            if key == "+":
                for_display_text += "(+)"
                if index != len(key_list):
                    for_display_text += " + "
            elif key == "right":
                for_display_text += "\u2192"
                if index != len(key_list):
                    for_display_text += " + "
            elif key == "left":
                for_display_text += "\u2190"
                if index != len(key_list):
                    for_display_text += " + "
            elif key == "up":
                for_display_text += "\u2191"
                if index != len(key_list):
                    for_display_text += " + "
            elif key == "down":
                for_display_text += "\u2193"
                if index != len(key_list):
                    for_display_text += " + "
            else:
                for_display_text += key
                if index != len(key_list):
                    for_display_text += " + "
            index += 1
        line.setText(for_display_text)

class RepeatCountInputThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.state = True
        self.delay = 0.01
        self.key_hook = None
        from ___Keys___ import only_number_keys
        from ___GroupBox___ import GroupBox
    def run(self):
        self.key_hook = keyboard.on_press(callback=self.OnPress)

        while self.state:
            time.sleep(self.delay)
    def stop(self):
        self.state = False
    def OnPress(self,event):
        group = (self.GroupFocused())[1]
        line = group.repeat_count_line
        max_count = GroupBox.RepeatCountLine.max_repeat_count
        cur_count = group.repeat_count_line.repeat_count
        line.setReadOnly(True)

        if event.name in only_number_keys and (self.GroupFocused())[0]:
            cur_count += event.name

            if int(cur_count) >= max_count:
                cur_count = str(max_count)
        elif event.name == "backspace" and (self.GroupFocused())[0]:
            if len(cur_count) >= 1:
                temp_list = list(cur_count)
                del temp_list[-1]
                cur_count = "".join(str(item) for item in temp_list)

        group.repeat_count_line.repeat_count = cur_count
        line.setText(cur_count)
    def GroupFocused(self):
        for group in GroupBox.group_list:
            if group.repeat_count_line.hasFocus():
                return True,group
        return False,group

class IntervalDelayInputThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.state = True
        self.delay = 0.01
        self.key_hook = None
        from ___Keys___ import only_number_keys
        from ___GroupBox___ import GroupBox
    def run(self):
        self.key_hook = keyboard.on_press(callback=self.OnPress)

        while self.state:
            time.sleep(self.delay)
    def stop(self):
        self.state = False
    def OnPress(self,event):
        group = (self.GroupFocused())[1]
        line = group.interval_delay_line
        interval_delay = line.interval_delay
        line.setReadOnly(True)

        if event.name == "." or event.name == "decimal" and (self.GroupFocused())[0]:
            if "." not in interval_delay:
                interval_delay += "."
        elif event.name in only_number_keys and (self.GroupFocused())[0]:
            interval_delay += event.name
        elif event.name == "backspace" and (self.GroupFocused())[0]:
            if len(interval_delay) >= 1:
                temp_list = list(interval_delay)
                del temp_list[-1]
                interval_delay = "".join(str(item) for item in temp_list)

        line.interval_delay = interval_delay
        line.setText(interval_delay)
    def GroupFocused(self):
        for group in GroupBox.group_list:
            if group.interval_delay_line.hasFocus():
                return True,group
        return False,group

class KeyListInputThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.state = True
        self.delay = 0.01
        self.key_hook = None
    def run(self):
        self.key_hook = keyboard.on_press(callback=self.OnPress)

        while self.state:
            time.sleep(self.delay)
    def OnPress(self,event):
        group = (self.GroupFocused())[1]
        line = group.key_list_line
        key_list = group.key_list_line.key_list
        max_count = GroupBox.KeyListLine.key_list_max_count
        line.setReadOnly(True)

        if event.name in allowed_key_list and event.name != toggle_key and (self.GroupFocused())[0]:
            if len(key_list) >= max_count:
                del key_list[-1:]
            key_list.append(event.name)
        elif event.name == "backspace" and event.name != toggle_key and (self.GroupFocused())[0]:
            if len(key_list) >= 1:
                del key_list[-1]

        self.DisplayKeyList(key_list, line)
    def stop(self):
        self.state = False
    def GroupFocused(self):
        for group in GroupBox.group_list:
            if group.key_list_line.hasFocus():
                return True, group
        return False, group
    def DisplayKeyList(self, key_list, line):
        for_display_text = ""
        index = 1
        for key in key_list:
            if key == "+":
                for_display_text += "(+)"
                if index != len(key_list):
                    for_display_text += " + "
            elif key == "right":
                for_display_text += "\u2192"
                if index != len(key_list):
                    for_display_text += " + "
            elif key == "left":
                for_display_text += "\u2190"
                if index != len(key_list):
                    for_display_text += " + "
            elif key == "up":
                for_display_text += "\u2191"
                if index != len(key_list):
                    for_display_text += " + "
            elif key == "down":
                for_display_text += "\u2193"
                if index != len(key_list):
                    for_display_text += " + "
            else:
                for_display_text += key
                if index != len(key_list):
                    for_display_text += " + "
            index += 1
        line.setText(for_display_text)

class ToggleThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.state = True
        self.delay = 0.01
        self.key_hook = None
        self.read_thread = ReadGroupThread()
    def run(self):
        self.key_hook = keyboard.on_press(callback=self.OnPress)

        while self.state:
            time.sleep(self.delay)
    def OnPress(self, event):
        if event.name == ___Keys___.toggle_key and self.read_thread.is_alive() == True:
            self.read_thread.stop()
            self.read_thread.join()
            setting_widget.label2.setText("Disabled")
            trans_parent_widget.label2.setText("Macro Status : Disabled")
        elif event.name == ___Keys___.toggle_key and self.read_thread.is_alive() == False:
            self.read_thread = ReadGroupThread()
            self.read_thread.start()
            setting_widget.label2.setText("Enabled")
            trans_parent_widget.label2.setText("Macro Status : Enabled")
    def stop(self):
        self.state = False

class ReadGroupThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.state = True
        self.delay = 0.01
    def run(self):
        while self.state:
            groups = GroupBox.group_list

            for group in groups:
                try:
                    if group.isChecked() == False:
                        pass
                    else:
                        continue
                except:
                    sys.exit("group error has occrued")

                is_readable = None
                is_readable = self.ReadHotKeyList(group)
                if is_readable == True:
                    pass
                else:
                    continue

                is_readable = None
                is_readable = self.ReadRepeatCount(group)
                if is_readable == True:
                    pass
                else:
                    continue

                is_readable = None
                is_readable = self.ReadIntervalDelay(group)
                if is_readable == True:
                    pass
                else:
                    continue

                key_list = group.key_list_line.key_list
                key_delay = float(group.interval_delay_line.interval_delay)
                repeat_count = int(group.repeat_count_line.repeat_count)

                for count in range(repeat_count):
                    if self.state == False: return
                    if ___Keys___.toggle_key in key_list: continue

                    for key in key_list:
                        if self.state == False: return
                        keyboard.press(key)
                        if self.state == False: return
                        time.sleep(key_delay)
                        if self.state == False: return
                        keyboard.release(key)
                        if self.state == False: return
                        time.sleep(key_delay)
                        if self.state == False: return

            time.sleep(self.delay)
    def stop(self):
        self.state = False
    def ReadHotKeyList(self,group):
        key_list = group.hot_key_line.hot_key_list
        correct_count = 0

        try:
            for key, value in mapped_numpad_vk_codes.items():
                if ctypes.windll.user32.GetAsyncKeyState(key) & 0x8000 and value in key_list:
                    correct_count += 1

            for key in key_list:
                scList = keyboard.key_to_scan_codes(key)
                # print(f"key name : {key}                scan code list : {scList}")
                try:
                    for scanCode in scList:
                        vkCode = ctypes.windll.user32.MapVirtualKeyA(scanCode, 1)
                        if ctypes.windll.user32.GetAsyncKeyState(vkCode) & 0x8000:
                            correct_count += 1
                            break
                except:
                    return False
            print(correct_count)
            if correct_count == len(key_list) and correct_count != 0 and ___Keys___.toggle_key not in key_list:
                return True
            else:
                return False
        except:
            return False
    def ReadRepeatCount(self,group):
        try:
            int(group.repeat_count_line.repeat_count)
            if int(group.repeat_count_line.repeat_count) > group.repeat_count_line.max_repeat_count and\
                int(group.repeat_count_line.repeat_count) < 0:
                return False
            return True
        except:
            return False
    def ReadIntervalDelay(self,group):
        try:
            float(group.interval_delay_line.interval_delay)
            return True
        except:
            return False

class ToggleKeyLineThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.state = True
        self.delay = 0.01
        self.key_hook = None
    def run(self):
        self.key_hook = keyboard.on_press(callback=self.OnPress)

        while self.state:
            time.sleep(self.delay)
    def OnPress(self, event):
        setting_widget.toggle_key_input_line.setReadOnly(True)

        if event.name in allowed_key_list:
            setting_widget.toggle_key_input_line.setText(event.name)
            setting_widget.toggle_key_input_line.key = event.name
    def stop(self):
        self.state = False