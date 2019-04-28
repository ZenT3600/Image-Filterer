from openpyxl import *
import PIL
from PIL import Image
from webcolors import *
from math import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from datetime import datetime
def on_button(action):
    now = datetime.now()
    try:
        fh = open("log.txt", "r")
        log = open("log.txt", "a+")
    except:
        log = open("log.txt", "w+")
        log.write("Start Of The Log History:")
        log.close()
        log = open("log.txt", "a+")
    progressbar.place(x=300, y=215, anchor="center")
    disable()
    image = txt.get() + variable.get()
    #print(image)
    #image = input("Image Name: ")
    #print(image)
    print("")
    try:
        now = datetime.now()
        im = PIL.Image.open(image)
        rgb_im = im.convert('RGB')
        log.write(str(now))
        log.write(": File Name: ")
        log.write(image)
        log.write("\n")
        log.write(str(now))
        log.write(": File Found Succesfully \n")
    except:
        now = datetime.now()
        messagebox.showerror("Error", "It seems like the image name you put in the field doesn't exist. Try writing it again or make sure that the image is in the same path as this program")
        progressbar.place_forget()
        enable()
        log.write(str(now))
        log.write(": Error Finding File \n")
        log.close()
    size = im.size
    print("Width:", size[0])
    print("Height:", size[1])
    print("")
    #print(size)
    nPixel = size[0] * size[1]
    progressbar['maximum'] = nPixel
    #print(nPixel)
    rArr = []
    gArr = []
    bArr = []
    x = 0
    y = 0
    print("Getting colors, this action could take some time depending on the image size")
    for i1 in range (0, size[1]):
        for i2 in range (0, size[0]):
            #print("Coordinate:", x, y)
            r, g, b = rgb_im.getpixel((x, y))
            rArr.append(r)
            gArr.append(g)
            bArr.append(b)
            x = x + 1
        x = 0
        y = y + 1
    now = datetime.now()
    log.write(str(now))
    log.write(": Image's pixel color analized succesfully \n")
    print("")
    print("The image contains", nPixel, "pixels")
    print("")
    index = 0
    index_color = 0
    num = 1
    #n_alf = int(len(alfabeto))
    #if (size[0] >= len(alfabeto)):
        #lettera = floor(size[0] / n_alf)
        #l = 0
        #for i in range (0, lettera):
            #for i in range (0, 26):
                #alfabeto.append(alfabeto[l] + alfabeto[i])
            #l = l + 1
        #print(alfabeto)
    log.write(str(now))
    log.write(": Filter Name: ")
    log.write(action)
    log.write("\n")
    if (action == "copy"):
        img = copy(nPixel, size, rArr, gArr, bArr)
    elif (action == "grayscale"):
        img = grayscale(nPixel, size, rArr, gArr, bArr)
    elif (action == "sepia"):
        img = sepia(nPixel, size, rArr, gArr, bArr)
    elif (action == "negative"):
        img = negative(nPixel, size, rArr, gArr, bArr)
    now = datetime.now()
    log.write(str(now))
    log.write(": Filter Added \n")
    print("")
    print("Process Completed!")
    print("")
    img.save(action + "-" + str(image))
    now = datetime.now()
    log.write(str(now))
    log.write(": Process Completed \n")
    messagebox.showinfo("OK!", "Process completed, the file was saved")
    progressbar.place_forget()
    enable()
    log.close()
    
def copy(nPixel, size, rArr, gArr, bArr):
    maxValue = nPixel
    i3 = 0
    img = PIL.Image.new( 'RGB', (size[0],size[1]), "black")
    pixels = img.load()
    print("Adding Filters")
    for i1 in range (0, size[1]):
        index = 0
        for i2 in range (0, size[0]):
            pixels[i2, i1] = (rArr[i3], gArr[i3], bArr[i3])
            i3 = i3 + 1
        currentValue = nPixel
        progressbar["value"] = (maxValue - (maxValue - i3))
        progressbar.update()
    return(img)

def grayscale(nPixel, size, rArr, gArr, bArr):
    maxValue = nPixel
    i3 = 0
    img = PIL.Image.new( 'RGB', (size[0],size[1]), "black")
    pixels = img.load()
    print("Adding Filters")
    for i1 in range (0, size[1]):
        index = 0
        for i2 in range (0, size[0]):
            r = rArr[i3]
            g = gArr[i3]
            b = bArr[i3]
            rg = round((r + g  + b)/3)
            gg = rg
            bg = rg
            pixels[i2, i1] = (rg, gg, bg)
            i3 = i3 + 1
        currentValue = nPixel
        progressbar["value"] = (maxValue - (maxValue - i3))
        progressbar.update()
    return(img)

def sepia(nPixel, size, rArr, gArr, bArr):
    maxValue = nPixel
    i3 = 0
    img = PIL.Image.new( 'RGB', (size[0],size[1]), "black")
    pixels = img.load()
    print("Adding Filters")
    for i1 in range (0, size[1]):
        index = 0
        for i2 in range (0, size[0]):
            r = rArr[i3]
            g = gArr[i3]
            b = bArr[i3]
            rs = round(0.393 * r + 0.769 * g + 0.189 * b)
            gs = round(0.349 * r + 0.686 * g + 0.168 * b)
            bs = round(0.272 * r + 0.534 * g + 0.131 * b)
            if (rs > 255):
                pixels[i2, i1] = (255, gs, bs)
            else:
                pixels[i2, i1] = (rs, gs, bs)
            if (gs > 255):
                pixels[i2, i1] = (rs, 255, bs)
            else:
                pixels[i2, i1] = (rs, gs, bs)
            if (bs > 255):
                pixels[i2, i1] = (rs, gs, 255)
            else:
                pixels[i2, i1] = (rs, gs, bs)
            i3 = i3 + 1
        currentValue = nPixel
        progressbar["value"] = (maxValue - (maxValue - i3))
        progressbar.update()
    return(img)

def negative(nPixel, size, rArr, gArr, bArr):
    maxValue = nPixel
    i3 = 0
    img = PIL.Image.new( 'RGB', (size[0],size[1]), "black")
    pixels = img.load()
    print("Adding Filters")
    for i1 in range (0, size[1]):
        index = 0
        for i2 in range (0, size[0]):
            r = rArr[i3]
            g = gArr[i3]
            b = bArr[i3]
            rn = 255 - r
            gn = 255 - g
            bn = 255 - b
            pixels[i2, i1] = (rn, gn, bn)
            i3 = i3 + 1
        currentValue = nPixel
        progressbar["value"] = (maxValue - (maxValue - i3))
        progressbar.update()
    return(img)

#Funzioni Di Crediti E Aiuti
def cred_start(sender):
    credits()

def credits():
    messagebox.showinfo("About", "Credits: \n Matteo Leggio \n matteo.leggio@tiscali.it")
    
def help():
    messagebox.showinfo("Help", "Insert the name of the image you want to add a filter to (it must be in the same directory as this program) in the 'image name' entry, then click the 'OK' button and watch the program do it's work")
    
def github():
    messagebox.showinfo("GitHub", "Github Repository: \n github.com/ZenT3600/Image-Filterer")
#Fine Funzioni Di Crediti E Aiuti
    
    
def f_quitter():
    log = open("log.txt", "a+")
    now = datetime.now()
    log.write(str(now))
    log.write(": Quit The Program \n")
    log.close()
    win.destroy()

def func_quitter(sender):
    f_quitter()
    
def on_closing():
    log = open("log.txt", "a+")
    now = datetime.now()
    log.write(str(now))
    log.write(": Program Closed Prematurely \n")
    log.close()
    win.destroy()

def func_start(x):
    action = x
    on_button(action)
    
def bind_func_start(sender, x):
    action = x
    on_button(action)
    
def enable():
    btn_copy.config(state=NORMAL)
    btn_gray.config(state=NORMAL)
    btn_sepia.config(state=NORMAL)
    btn_nega.config(state=NORMAL)
    quitter.config(state=NORMAL)
    txt.config(state=NORMAL)

def disable():
    btn_copy.config(state=DISABLED)
    btn_gray.config(state=DISABLED)
    btn_sepia.config(state=DISABLED)
    btn_nega.config(state=DISABLED)
    quitter.config(state=DISABLED)
    txt.config(state=DISABLED)
    
win = Tk()
log = open("log.txt", "a+")
log.write("*******************\n")
log.close()
win.protocol("WM_DELETE_WINDOW", on_closing)
win.resizable(False, False)
win.title("Image Filterer")
win.geometry("600x400")

lbl = Label(win, text="Image Filterer", font=("Verdana", 30, "bold"))
lbl.place(x=300, y=25, anchor="center")

lbl_2 = Label(win, text="Image Name", font=("Verdana", 10, "bold"))
lbl_2.place(x=300, y=155, anchor="center")

desc = Label(win, text="Add a filter to any image you want", font=("Verdana", 10), justify=CENTER)
desc.place(x=300, y=80, anchor="center")

txt = Entry(win ,width=70)
txt.place(x=300, y=175, anchor="center")

variable = StringVar(win)
variable.set(".png")

dropdown = OptionMenu(win, variable, ".png", ".png", ".jpg", ".jpeg")
dropdown.place(x=545, y=175, anchor="center")

progressbar = Progressbar(win,orient="horizontal",length=300,mode="determinate")

btn_copy = Button(win, text="Copy", command=lambda: func_start("copy"))
btn_copy.place(x=300, y=260, anchor="center")
btn_copy.bind('<Return>', lambda: bind_func_start("copy"))
btn_gray = Button(win, text="Grayscale", command=lambda: func_start("grayscale"))
btn_gray.place(x=300, y=300, anchor="center")
btn_gray.bind('<Return>', lambda: bind_func_start("grayscale"))
btn_sepia = Button(win, text="Sepia", command=lambda: func_start("sepia"))
btn_sepia.place(x=300, y=340, anchor="center")
btn_sepia.bind('<Return>', lambda: bind_func_start("sepia"))
btn_nega = Button(win, text="Negative", command=lambda: func_start("negative"))
btn_nega.place(x=300, y=380, anchor="center")
btn_nega.bind('<Return>', lambda: bind_func_start("negative"))

menubar = Menu(win)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=help)
helpmenu.add_command(label="About", command=credits)
helpmenu.add_command(label="Github", command=github)
menubar.add_cascade(label="Help & Links", menu=helpmenu)
win.config(menu=menubar)

quitter = Button(win, width=6, text = "Quit", command=f_quitter)
quitter.place(x=560, y=380, anchor="center")
quitter.bind('<Return>', func_quitter)
win.mainloop()
