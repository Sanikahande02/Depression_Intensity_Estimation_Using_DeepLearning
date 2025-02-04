from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import Depressionprediction

def center_window():
    # get screen width and height
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()
    #setting tkinter window size
    root.geometry("%dx%d" % (width, height))
    return width,height
    
root=Tk()
#root.configure(background='#6495ED')
root.title("Depression Prediction System")
w,h=center_window()
# Read the Image
image = Image.open("main3.jpg")

# Resize the image using resize() method
resize_image = image.resize((w, h))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()

 
def read_input():
    filepath=textBox1.get()
    vlsname,lsname,msname,hsname,vhsname=Depressionprediction.initProcess(filepath)
    label2 = Label(root,text = "Students With Very Low Depression",fg='#FFFFFF',bg='#000000',font=("Ariel", 10)).place(x = 2,y = 360)
    T1 = Text(root, height = 15, width = 30)
    T1.place(x = 2,y = 400)
    T1.insert(tk.END, vlsname)

    label3 = Label(root,text = "Students With Low Depression",fg='#FFFFFF',bg='#000000',font=("Ariel", 10)).place(x = 310,y = 360)
    T2 = Text(root, height = 15, width = 30)
    T2.place(x = 290,y = 400)
    T2.insert(tk.END, lsname)

    label4 = Label(root,text = "Students With Medium Depression",fg='#FFFFFF',bg='#000000',font=("Ariel", 10)).place(x = 580,y = 360)
    T3 = Text(root, height = 15, width = 30)
    T3.place(x = 570,y = 400)
    T3.insert(tk.END, msname)

    label5 = Label(root,text = "Students With High Depression",fg='#FFFFFF',bg='#000000',font=("Ariel", 10)).place(x = 875,y = 360)
    T4 = Text(root, height = 15, width = 30)
    T4.place(x = 860,y = 400)
    T4.insert(tk.END, hsname)

    label6 = Label(root,text = "Students With Very High Depression",fg='#FFFFFF',bg='#000000',font=("Ariel", 10)).place(x = 1140,y = 360)
    T5 = Text(root, height = 15, width = 25)
    T5.place(x = 1150,y = 400)
    T5.insert(tk.END, vhsname)
     
       
     
  

    

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                        ("all files",
                                                        "*.*")))
      
    textBox1.insert(0, filename)

    

# code to create label 
label1 = Label(root,text = "Select File: ",fg='#FFFFFF',bg='#000000',font=("Ariel", 12)).place(x = 550,y = 110)



#code to insert textbox
textBox1 = tk.Entry(root, width = 60)
textBox1.place(x = 720,y = 105,height=35)







browsebutton=Button(root, height=1, width=13, font=("Ariel", 10,'bold'),fg='#FFFFFF',bg='#FF5F1F',text="Browse",  command=lambda: browseFiles()).place(x=1100,y=105)
#command=lambda: retrieve_input() >>> just means do this when i press the button
submitebutton=Button(root, height=1, width=13, font=("Ariel", 10,'bold'),fg='#FFFFFF',bg='#FF5F1F',text="Submit", command=lambda: read_input()).place(x=720,y=200)
# Button for closing
exit_button = Button(root, height=1, width=13, font=("Ariel", 10,'bold'),fg='#FFFFFF',bg='#FF5F1F',text="Exit", command=root.destroy).place(x=920,y=200)


 
 

mainloop()