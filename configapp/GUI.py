import tkinter as tk
import os,json

root = tk.Tk()
root.title("PRD Config")
root.geometry("400x300")
root.resizable(False,False)

Intro = tk.Label(root, text="Pico Rubber Ducky Config")
Intro.pack()
fpl = tk.Label(root, text="File Path:")
fpl.pack()
fp = tk.Entry(root, width = 20)
fp.pack()
instrl = tk.Label(root, text="Executed Command:")
instrl.pack()
ins = tk.Entry(root, width=60)
ins.pack()
osl = tk.Label(root, text="OS (first three letters of OS): ")
osl.pack()
osv = tk.Entry(root, width=20)
osv.pack()

def save(fp=fp, ins=ins, osv=osv ):
    osv = osv.get().lower()
    data = {"instruction": ins.get(), "os": osv}
    fp = fp.get() + "/pico_conf.json"
    with open(fp, 'w') as f:
        json.dump(data, f)


saveb = tk.Button(root, text="Save Config", command=save)
saveb.pack()

root.mainloop()
