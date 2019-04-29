from openpyxl import *
import PIL
from PIL import Image
from PIL import ImageEnhance
import colorsys
from webcolors import *
from math import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from datetime import datetime
def on_button(action):
    try:
        fh = open("log.txt", "r")
    except:
        log = open("log.txt", "w+")
        log.write("Start Of The Log History:")
        log.close()
    progressbar.place(x=300, y=215, anchor="center")
    disable()
    image = txt.get() + variable.get()
    #print(image)
    #image = input("Image Name: ")
    #print(image)
    print("")
    try:
        im = PIL.Image.open(image)
        rgb_im = im.convert('RGB')
        logValue(": File Name: ", image)
        logAction(": Image Opened Successfully \n")
    except:
        messagebox.showerror("Error", "It seems like the image name you put in the field doesn't exist. Try writing it again or make sure that the image is in the same path as this program")
        progressbar.place_forget()
        enable()
        logAction(": Error Finding File \n")
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
    logAction(": Image's pixel color analyzed successfully \n")
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
    logValue(": Filter Name: ", action)
    if (action == "copy"):
        img = copy(nPixel, size, rArr, gArr, bArr)
    elif (action == "grayscale"):
        img = grayscale(nPixel, size, rArr, gArr, bArr)
    elif (action == "sepia"):
        img = sepia(nPixel, size, rArr, gArr, bArr)
    elif (action == "negative"):
        img = negative(nPixel, size, rArr, gArr, bArr)
    elif (action == "saturate"):
        img = saturate(nPixel, size, rArr, gArr, bArr)
    elif (action == "desaturate"):
        img = desaturate(nPixel, size, rArr, gArr, bArr)
    logAction(": Filter Added Successfully \n")
    print("")
    print("Process Completed!")
    print("")
    img.save(action + "-" + str(image))
    logAction(": Process Completed \n")
    messagebox.showinfo("OK!", "Process completed, the file was saved")
    progressbar.place_forget()
    enable()
    
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

def saturate(nPixel, size, rArr, gArr, bArr):
    maxValue = nPixel
    i3 = 0
    img = copy(nPixel, size, rArr, gArr, bArr)
    print("Adding Filters")
    for i1 in range (0, size[1]):
        index = 0
        for i2 in range (0, size[0]):
            i3 = i3 + 1
        currentValue = nPixel
        progressbar["value"] = (maxValue - (maxValue - i3))
        progressbar.update()
    converter = ImageEnhance.Color(img)
    img = converter.enhance(2)
    return(img)

def desaturate(nPixel, size, rArr, gArr, bArr):
    maxValue = nPixel
    i3 = 0
    img = copy(nPixel, size, rArr, gArr, bArr)
    print("Adding Filters")
    for i1 in range (0, size[1]):
        index = 0
        for i2 in range (0, size[0]):
            i3 = i3 + 1
        currentValue = nPixel
        progressbar["value"] = (maxValue - (maxValue - i3))
        progressbar.update()
    converter = ImageEnhance.Color(img)
    img = converter.enhance(0.5)
    return(img)

def cred_start(sender):
    credits()

def credits():
    messagebox.showinfo("About", "Credits: \n Matteo Leggio \n matteo.leggio@tiscali.it")
    
def help():
    messagebox.showinfo("Help", "Insert the name of the image you want to add a filter to (it must be in the same directory as this program) in the 'image name' entry, then click the 'OK' button and watch the program do it's work")
    
def github():
    messagebox.showinfo("GitHub", "Github Repository: \n github.com/ZenT3600/Image-Filterer")
    
    
def f_quitter():
    log = open("log.txt", "a+")
    logAction(": Quit The Program: \n")
    win.destroy()

def func_quitter(sender):
    f_quitter()
    
def on_closing():
    log = open("log.txt", "a+")
    logAction(": Program Closed Prematurely: \n")
    win.destroy()

def func_start(x):
    action = x
    on_button(action)
    
#def bind_func_start(sender, x):
#    action = x
#    on_button(action)
    
def enable():
    btn_copy.config(state=NORMAL)
    btn_gray.config(state=NORMAL)
    btn_sepia.config(state=NORMAL)
    btn_nega.config(state=NORMAL)
    btn_satu.config(state=NORMAL)
    btn_desatu.config(state=NORMAL)
    quitter.config(state=NORMAL)
    txt.config(state=NORMAL)

def disable():
    btn_copy.config(state=DISABLED)
    btn_gray.config(state=DISABLED)
    btn_sepia.config(state=DISABLED)
    btn_nega.config(state=DISABLED)
    btn_satu.config(state=DISABLED)
    btn_desatu.config(state=DISABLED)
    quitter.config(state=DISABLED)
    txt.config(state=DISABLED)
    
def logAction(action):
    now = datetime.now()
    log = open("log.txt", "a+")
    log.write(str(now))
    log.write(action)
    log.close()
    
def logValue(action, value):
    now = datetime.now()
    log = open("log.txt", "a+")
    log.write(str(now))
    log.write(action)
    log.write(value)
    log.write("\n")
    log.close()
    
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
#btn_copy.bind('<Return>', lambda: bind_func_start("copy"))
btn_gray = Button(win, text="Grayscale", command=lambda: func_start("grayscale"))
btn_gray.place(x=300, y=300, anchor="center")
#btn_gray.bind('<Return>', lambda: bind_func_start("grayscale"))
btn_sepia = Button(win, text="Sepia", command=lambda: func_start("sepia"))
btn_sepia.place(x=380, y=260, anchor="center")
#btn_sepia.bind('<Return>', lambda: bind_func_start("sepia"))
btn_nega = Button(win, text="Negative", command=lambda: func_start("negative"))
btn_nega.place(x=380, y=300, anchor="center")
#btn_nega.bind('<Return>', lambda: bind_func_start("negative"))
btn_satu = Button(win, text="Saturate", command=lambda: func_start("saturate"))
btn_satu.place(x=220, y=260, anchor="center")
#btn_satu.bind('<Return>', lambda: bind_func_start("saturate"))
btn_desatu = Button(win, text="Desaturate", command=lambda: func_start("desaturate"))
btn_desatu.place(x=220, y=300, anchor="center")
#btn_desatu.bind('<Return>', lambda: bind_func_start("desaturate"))

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
