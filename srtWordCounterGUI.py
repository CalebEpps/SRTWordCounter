import sys
from tkinter import *
from tkinter import ttk, filedialog, messagebox

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

filetypes = (
    ('SRT Files', '*.srt'),
    ('All Files', '*.*')
)


def count_words(file):
    try:
        srt = open(file)

        lines = [line.strip() for line in srt]

        srt.close()

        raw = []

        row = 0

        for line in lines:
            row += 1

            if row <= 2:
                continue

            if line == "":
                row = 0
                continue

            raw.append(line)

        text = " ".join(raw)
        text = text.split(" ")

        return text

    except FileNotFoundError:
        messagebox.showinfo(title="File Error", message="Please ensure you have chosen an srt file.")


def open_SRT():
    file = filedialog.askopenfilename(filetypes=filetypes)
    srt_Txt = count_words(file)
    ttk.Label(frm, text=len(srt_Txt)).grid(column=0, row=2)

    text = Text(frm)
    text.grid(column=0, row=0)

    fileText = ""
    for i in srt_Txt:
        fileText += i
        fileText += " "

    text.insert('0.0', fileText)
    text.config(state=DISABLED)


ttk.Label(frm, text="Sing's SRT Word Counter", ).grid(column=0, row=1, sticky='ew')
ttk.Label(frm, text="Word Count: ").grid(column=0, row=2, sticky='ew')
ttk.Button(frm, text="Open File", command=open_SRT).grid(column=0, row=3, sticky='ew')

root.geometry('800x600')


frm.place(anchor="center", relx=.5, rely=.5)

root.mainloop()
