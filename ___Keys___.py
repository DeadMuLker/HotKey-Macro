# import keyboard
# import time

allowed_key_list = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                    "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12",
                    "`", "~", "-", "+", "=", "/", "*", "decimal", "<", ">", "?",
                    "[", "]", "\\", ";", "'", ",", ".", "{", "}", "|", ":", "\"", "(", ")",
                    "!", "@", "#", "$", "%", "^", "&", "_",
                    "print screen", "scroll lock", "pause", "delete", "end", "page down", "clear",
                    "insert", "home", "page up",
                    "left", "right", "up", "down",
                    "esc", "caps lock", "shift" , "right shift", "ctrl", "right ctrl", "alt", "enter", "space",
                    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
                    "a", "s", "d" , "f", "g", "h", "j", "j", "k", "l",
                    "z", "x", "c", "v", "b", "n", "m",
                    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
                    "A", "S", "D", "F", "G", "H", "J", "K", "L",
                    "Z", "X", "C", "V", "B", "N", "M")

only_number_keys = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

toggle_key = "f12"

mapped_numpad_vk_codes = {
    0x60: "0",
    0x61: "1",
    0x62: "2",
    0x63: "3",
    0x64: "4",
    0x65: "5",
    0x66: "6",
    0x67: "7",
    0x68: "8",
    0x69: "9",
    0x6E: "decimal",
}