# HotKey Macro
This is a keyboard macro.
# Support OS
`Windows`(I have not tested other os).
# Requirements
`pip install pyside6`

`pip install keyboard`

`pip install pynput`
# How To Use
1. Click Add button, and you can see the KeyGroupBox.
2. Check the Key Group by clicking.
3. If you click the input box, the keyboard listener will be activated.
4. Before insert the keys, please check the `___Key___.py`.
5. The `___Key___.py` includes all acceptable keys, and you can change the key list
as you want.
6. Write to each input box, and you should make sure each input box. If you
don`t write properly, the macro will not execute your Key Group.
7. Also, you must Uncheck all Key Groups to run. If you don`t,
like said before, It will be not executed. (I inserted this function to prevent access to Key Group)

# Caution
If you set the interval delay too long, even though you pressed the macro status to stop, the macro
will not stop immediately. Because the macro stop check statements are placed after the interval delay.
so, make the delay short. (recommend 0.01s)

# Save and Load
This macro support save and load options, and the file extension is `.mco`.

To do save or load, click the `File` button. It is above the Add button.

Before to save, you must write data to all input boxes, otherwise you will get an error.

To make look good, the two keywords are replaced to easy keywords. `,` is replaced to `comma` and `.` is replaced to `full stop`.

You should know the two keywords to handle saved file.

# Main
`___init___.py` is the starting point of this macro. To start, run `___init___.py` as an administrator.