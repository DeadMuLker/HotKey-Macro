import keyboard
import time
import pynput

allowed_key_list = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                    "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12",
                    "`", "~", "-", "+", "=", "/", "*", "decimal", "<", ">", "?",
                    "[", "]", "\\", ";", "'", ",", ".", "{", "}", "|", ":", "\"", "(", ")",
                    "!", "@", "#", "$", "%", "^", "&", "_",
                    "print screen", "scroll lock", "pause", "delete", "end", "page down", "clear"
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

KEY = pynput.keyboard.Key

key_list_for_pynput = {
    48: ("0", ")"),
    96: "0", #numpad 0
    49: ("1", "!"),
    97: "1", #numpad 1
    50: ("2", "@"),
    98: "2", #numpad 2
    51: ("3", "#"),
    99: "3", #numpad 3
    52: ("4", "$"),
    100: "4", #numpad 4
    53: ("5", "^"),
    101: "5", #numpad 5
    54: ("6", "&"),
    102: "6", #numpad 6
    55: ("7", "&"),
    103: "7", #numpad 7
    56: ("8", "*"),
    104: "8", #numpad 8
    57: ("9" , "("),
    105: "9", #numpad 9
    81: ("q", "Q"),
    87: ("w", "W"),
    69: ("e", "E"),
    82: ("r", "R"),
    84: ("t", "T"),
    89: ("y", "Y"),
    85: ("u", "U"),
    73: ("i", "I"),
    79: ("o", "O"),
    80: ("p", "P"),
    219: ("[", "{"),
    221: ("]", "}"),
    220: ("\\", "|"),
    65: ("a", "A"),
    83: ("s", "S"),
    68: ("d", "D"),
    70: ("f", "F"),
    71: ("g", "G"),
    72: ("h", "H"),
    74: ("j", "J"),
    75: ("k", "K"),
    76: ("l", "L"),
    186: (";", ":"),
    222: ("'", "\""),
    90: ("z", "Z"),
    88: ("x", "X"),
    67: ("c", "C"),
    86: ("v", "V"),
    66: ("b", "B"),
    78: ("n", "N"),
    77: ("m", "M"),
    188: (",", "<"),
    190: (".", ">"),
    191: ("/", "?"),
    KEY.f1: "f1",
    KEY.f2: "f2",
    KEY.f3: "f3",
    KEY.f4: "f4",
    KEY.f5: "f5",
    KEY.f6: "f6",
    KEY.f7: "f7",
    KEY.f8: "f8",
    KEY.f9: "f9",
    KEY.f10: "f10",
    KEY.f11: "f11",
    KEY.f12: "f12",
    192: ("`", "~"),
    189: ("-", "_"),
    109: "-", # numpad -
    187: "=",
    107: "+", # numpad +
    12: "clear",
    110: "decimal", # numpad .
    111: "/", # numpad /
    106: "*", # numpad *
    KEY.print_screen: "print screen",
    KEY.scroll_lock: "scroll lock",
    KEY.pause: "pause",
    KEY.insert: "insert",
    KEY.home: "home",
    KEY.page_up: "page up",
    KEY.delete: "delete",
    KEY.end: "end",
    KEY.page_down: "page down",
    KEY.left: "left",
    KEY.right: "right",
    KEY.up: "up",
    KEY.down: "down",
    KEY.caps_lock: "caps lock",
    KEY.shift: "shift",
    KEY.shift_l: "left shift",
    KEY.shift_r: "right shift",
    KEY.ctrl: "ctrl",
    KEY.ctrl_l: "ctrl",
    KEY.ctrl_r: "right ctrl",
    KEY.alt: "alt",
    KEY.alt_l: "alt",
    KEY.alt_r: "alt right",
    KEY.enter: "enter",
    KEY.space: "space",
}







