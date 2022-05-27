# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""
# import tkinter
import tkinter.ttk

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


count = 0


def countUP():
    global count
    count += 1
    label.config(text=str(count))


def cc(self):
    treeview.tag_configure("tag2", background="red")


window = tkinter.Tk()

treeview = tkinter.ttk.Treeview(window, columns=["one", "two"], displaycolumns=["two", "one"])
treeview.pack()

treeview.column("#0", width=70)
treeview.heading("#0", text="num")

treeview.column("one", width=100, anchor="center")
treeview.heading("one", text="문자", anchor="e")

treeview.column("#2", width=100, anchor="w")
treeview.heading("two", text="ASCII", anchor="center")

treelist = [("A", 65), ("B", 66), ("C", 67), ("D", 68), ("E", 69)]

for i in range(len(treelist)):
    treeview.insert('', 'end', text=i, values=treelist[i], iid=str(i) + "번")

top = treeview.insert('', 'end', text=str(len(treelist)), iid="5번", tags="tag1")
top_mid1 = treeview.insert(top, 'end', text="5-2", values=["SOH", 1], iid="5번-1")
top_mid2 = treeview.insert(top, 0, text="5-1", values=["NUL", 0], iid="5번-0", tags="tag2")
top_mid3 = treeview.insert(top, 'end', text="5-3", values=["STX", 2], iid="5번-2", tags="tag2")

treeview.tag_bind("tag1", sequence="<<TreeviewSelect>>", callback=cc)


window.title("elecard video format analyzer 21")
window.geometry("960x1080+0+0")
window.resizable(False, False)


label1 = tkinter.Label(window, text="안녕하세요.")
label2 = tkinter.Label(window, text="파이썬", width=10, height=5, fg="red", relief="solid")

label = tkinter.Label(window, text="0")

label1.pack()
label2.pack()
label.pack()

button = tkinter.Button(window, overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
button.pack()


window.mainloop()
"""


from tkinter import *
# from TkinterDnD2 import *
from tkinterdnd2 import TkinterDnD, DND_FILES


def DisplayText(event):
    # delete entire existing content
    textbox.delete("1.0","end")
    # check the file holds txt extension
    if event.data.endswith(".txt"):
        with open(event.data, "r") as f:
            # getting content in a variable
            for text_line in f:
                text_line=text_line.strip()
                textbox.insert("end",f"{text_line}\n")

win = TkinterDnD.Tk()
win.title('Delftstack')
win.geometry('500x400')
win.config(bg='gold')

frame = Frame(win)
frame.pack()

textbox = Text(frame, height=22, width=50)
textbox.pack(side=LEFT)
textbox.drop_target_register(DND_FILES)
textbox.dnd_bind('<<Drop>>', DisplayText)

scrolbar = Scrollbar(frame, orient=VERTICAL)
scrolbar.pack(side=RIGHT, fill=Y)

textbox.configure(yscrollcommand=scrolbar.set)
scrolbar.config(command=textbox.yview)

win.mainloop()

