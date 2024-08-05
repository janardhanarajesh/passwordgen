from tkinter import *
from tkinter import messagebox
from  PIL import Image,ImageTk
import random
main_window=Tk()
main_window.title("password generator")
main_window.minsize(height=200,width=500)
main_window.maxsize(height=200,width=500)
# img=Image.open(r"C:\Users\dell\Downloads\biriyani.jpeg")
# v=ImageTk.PhotoImage(img)
def gen():
    out.config(text="")
    alp=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    Apl=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    num=[0,1,2,3,4,5,6,7,8,9]
    spchar=["!","@","#","$","%","^","&","*"]
    ralp=alp[random.randrange(26)]
    rcap=Apl[random.randrange(26)]
    rnum=str(num[random.randrange(10)])
    rapchar=spchar[random.randrange(7)]
    # print(ralp,rcap,rnum,rapchar)
    ra=[ralp,rcap,rnum,rapchar]
    ran1=ra[random.randrange(4)]
    ran2=ra[random.randrange(4)]
    ran3=ra[random.randrange(4)]
    ran4=ra[random.randrange(4)]
    ran5=ra[random.randrange(4)]
    ran6=ra[random.randrange(4)]
    ran7=ra[random.randrange(4)]
    ran8=ra[random.randrange(4)]
    output=ran1+ran2+ran3+ran4+ran5+ran6+ran7+ran8
    print(ran1+ran2+ran3+ran4+ran5+ran6+ran7+ran8)
    out.config(text=output)
    main_window.clipboard_append(output)
    messagebox.showinfo("pgen","copied to clipboard")
child_window=Frame(main_window,height=500,width=800,bg="orange")
child_window.pack()
out=Label(child_window,font=(20),bg="white",fg="black",width=20,height=5)
out.pack()
but=Button(child_window,text="generate",bg="white",fg="black",cursor="hand2",command=gen)#can use image=v
but.pack()
main_window.mainloop()