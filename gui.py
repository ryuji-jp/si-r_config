import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import main

a = ""
b = ""

# 参照ボタンのイベント
# button1クリック時の処理 上部参照ボタン
def button1_clicked():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    file1.set(filepath)
    global a
    a = filepath

# 下部参照ボタン
def button3_clicked():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath2 = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    file2.set(filepath2)
    global b
    b = filepath2

# startボタン
def button2_clicked():
    main.confmake(a,b)
    messagebox.showinfo('FileReference Tool', u'コンフィグ作成完了\n')

    root.mainloop()

if __name__ == '__main__':
    # rootの作成
    root = Tk()
    root.title('FileReference Tool')
    root.resizable(False, False)

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # 参照ボタンの作成
    button1 = ttk.Button(root, text=u'参照', command=button1_clicked)
    button1.grid(row=0, column=3)

    #フレーム3作成
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=1)

    button2 = ttk.Button(root, text=u'参照', command=button3_clicked)
    button2.grid(row=1, column=3)

    # ラベルの作成
    # 「ファイル」ラベルの作成
    s = StringVar()
    s.set('事前コンフィグ>>')
    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=0, column=0)
    #ラベル作成
    s2 = StringVar()
    s2.set('事後コンフィグ>>')
    label2 = ttk.Label(frame3, textvariable=s2)
    label2.grid(row=1, column=0)

    # 参照ファイルパス表示ラベルの作成
    file1 = StringVar()
    file1_entry = ttk.Entry(frame1, textvariable=file1, width=50)
    file1_entry.grid(row=0, column=2)


    file2 = StringVar()
    file2_entry = ttk.Entry(frame3, textvariable=file2, width=50)
    file2_entry.grid(row=1, column=2)

    # Frame2の作成
    frame2 = ttk.Frame(root, padding=(0,5))
    frame2.grid(row=2)

    # Startボタンの作成
    button2 = ttk.Button(frame2, text='Start', command=button2_clicked)
    button2.pack(side=LEFT)

    # Cancelボタンの作成
    button3 = ttk.Button(frame2, text='Cancel', command=quit)
    button3.pack(side=LEFT)

    root.mainloop()