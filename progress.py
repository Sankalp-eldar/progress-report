from tkinter import Tk,Text,Message,Frame,Label,Menu,Toplevel
from tkinter.ttk import Button,Scrollbar,Entry#,Style
from tkinter.colorchooser import askcolor
import time
import os

root = Tk()
root.title("Progress Reporter😑")
root.geometry("322x336")
root.minsize(322,336)
root.config(bg="white")

# style = Style()
# style.configure(".",border=0,highlightthickness=0)
def color(which):
    cord,col = askcolor()
    if col:
        if which == "box":
            a.config(bg=col)
        elif which == "font":
            a.config(fg=col)

def front():
    old = os.getcwd()
    os.chdir("..")
    files = os.listdir()
    if "front.py" in files:os.startfile("front.py")
    elif "front.pyw" in files:os.startfile("front.pyw")
    else:
        from tkinter.messagebox import showerror as mb
        mb("Error","File not found!",detail=f"( At {os.getcwd()} )",master=root)
    os.chdir(old)

# _________________ MENU __________________
men = Menu(root)
root.config(menu=men)

File = Menu(men,tearoff=0)
File.add_command(label="Open Report",command=lambda:os.startfile("Report.txt"))
File.add_command(label="Run front.py",command=front)


def custom():
    base = Toplevel(root)
    base.transient(root)
    base.geometry(f"+{root.winfo_pointerx()-100}+{root.winfo_pointery()-50}")
    base.focus_set()

    c = Entry(base,width=74);c.pack()
    def done():
        global end
        if len(c.get()) > 20:end = c.get();base.destroy()
        else:c.insert("end"," (MORE THAN 20 Character) ")
    Button(base,text="Close",command=base.destroy).pack(side="right")
    Button(base,text="Done",command=done).pack(side="right")
    Button(base,text="Insert 'END...'",command=lambda:c.insert("end","END OF ABOVE"
        ) if "END OF ABOVE" not in c.get() else None).pack(side="left")


def change(opt):
    global end
    if opt == 1:
        end = "_______________________________END OF ABOVE_______________________________"
    elif opt == 2:
        end = "<><><><><><><><><><><><><><><><END OF ABOVE><><><><><><><><><><><><><><><>"
    elif opt == 3:
        end = "=_= =_= =_= =_= =_= =_= =_= =_=END OF ABOVE=_= =_= =_= =_= =_= =_= =_= =_="
    else:
        end ="+++++++++++++++++++++++++++++++END OF ABOVE+++++++++++++++++++++++++++++++"
change(1)

Edit = Menu(men,tearoff=0)
Change = Menu(Edit,tearoff=0)
Change.add_command(label="Custom (won't be saved)",command=custom)
Change.add_separator()
Change.add_command(label="____...END OF ABOVE...___",command=lambda:change(1))
Change.add_command(label="<><...END OF ABOVE...><>",command=lambda:change(2))
Change.add_command(label="===...END OF ABOVE...===",command=lambda:change(3))
Change.add_command(label="+++...END OF ABOVE...++++",command=lambda:change(4))

Edit.add_command(label="Pick TextBox color",command=lambda:color("box"))
Edit.add_command(label="Pick Font color",command=lambda:color("font"))
Edit.add_separator()
Edit.add_cascade(label="End of Line (Report.txt)",menu=Change)

men.add_cascade(label="File",menu=File)
men.add_cascade(label="Edit",menu=Edit)
# _______________ Menu END ______________



Label(root,text="🎅 Progress Update 🎅",bg="white",font=("Arial",14)).pack(side="top",padx=1)
text1 = "Just type in whatever changes were made \n To keep track of all Edits with time."
Label(root,text=text1,bg="white",width=100).pack(fill="x",side="top")

fr = Frame(root,border=0,bg="white")
fr.pack(side="top",fill="both",expand=1)


a = Text(fr,bg="white",height=8,width=36)
axis_y = Scrollbar(fr,orient="vertical",command=a.yview)
#axis_x = Scrollbar(fr,orient="horizontal",command=a.xview)
a.config(yscrollcommand=axis_y.set) #xscrollcommand=axis_x.set,

#axis_x.pack(side="bottom",fill="x")
a.pack(side="left",fill="both",expand=1,padx=4,pady=1)
axis_y.pack(side="right",fill="y")

def save(dest=False):
    with open("Report.txt","r+") as f:
        data = (i for i in f.readlines())
        f.write("\n")
        f.seek(0)
        f.write("*"*35+"\n")
        f.write(time.strftime("(%I:%M:%S %p)  %A, %d %B %Y.\n"))
        f.write("*"*35+'\n')
        f.write(a.get(1.0,"end"))
        f.write(end)
        f.write("\n\n\n")
        for i in data:
            f.write(i)
        b.pack(side="left",padx=3)
        root.after(5000,b.pack_forget)
        if dest:root.destroy()


Button(root,text="Quit",command=root.destroy).pack(pady=4,side="right")
Button(root,text="Save and Quit",command=lambda:save(True)).pack(pady=4,side="right")
Button(root,text="Save",command=save).pack(pady=4,padx=3,side="right")

b = Label(root,text="Saved",bg="white",fg="green")

root.mainloop()
