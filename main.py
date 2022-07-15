#form
from time import sleep
import tkinter as tk
from PIL import ImageTk,Image

#my lib
import cvTest


#button click event
def btn_process_click():
    print("click")    
    global img_resize_3
    img=cvTest.MatchTempate()
    img_resize_3=ImageTk.PhotoImage(img.resize((w-30,h-30),Image.ANTIALIAS))
    img_label_2=tk.Label(lf2,image=img_resize_3)
    img_label_2.pack(fill="both")


#cvpicture

#config window
root=tk.Tk()
root.title("OpenCV")
root.geometry("830x500")
root.resizable(False,False)

#configure the grid
#    ////////////////
#    /      /       /
#    /      /       /
#    ////////////////
#    /      /       /
#    ////////////////

root.columnconfigure(index=0,weight=1)
root.columnconfigure(index=1,weight=1)
root.rowconfigure(index=0,weight=4)
root.columnconfigure(index=1,weight=1)



# picture
w=400
h=400
lf=tk.LabelFrame(root, text="Picture",width=w,height=h,background="gray")
lf.grid(column=0, row=0, padx=10, pady=10)
img=Image.open("1.PNG")
img_resize=ImageTk.PhotoImage(Image.open("1.PNG").resize((w-30,h-30),Image.ANTIALIAS))
img_label=tk.Label(lf,image=img_resize)
img_label.pack(fill="both")

# cvpicture
lf2=tk.LabelFrame(root, text="CV Picture",width=400,height=400,background="gray")
lf2.grid(column=1, row=0, padx=10, pady=10)


# button
bn_process=tk.Button(root, text="Process", command=btn_process_click)
bn_process.grid(column=1,row=1,padx=5,pady=5)

root.mainloop()