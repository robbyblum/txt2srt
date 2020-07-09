# written by deciMae, minorly edited by glumbaron

import sys

import tkinter as tk
import tkinter.filedialog as fd





numlines = 0
importf = ""
timedelta = 0
total = 0
updating = False

def openfile():
    global importf 
    global timedelta
    global total 
    
    importf = fd.askopenfilename()
    if(importf == ""): 
        return 0
    
    getnumlines()
    
    importfVar.set(importf)
    
    
    
    if(timedelta == 5 and total != 0):
        updatefromtotal()
    else:
        updatefromdelta()
    
    return importf

def getnumlines():
    global numlines
    if(importf == ""):
        numlines = 0
    else:
        numlines = sum(1 if line != "\n" else 0 for line in open(importf, "r"))
    numlinesVar.set(numlines)

def updatefromdelta(*args):
    global total
    global timedelta
    global updating

    if(updating):
        print("hi")
        return
    updating = True
    if((not timedeltaVar.get().isnumeric()) or int(timedeltaVar.get()) <= 0):
        timedeltaVar.set(str(timedelta))
    else :
        timedelta = int(timedeltaVar.get())
        if(importf != ""):
            total = timedelta * numlines
            seconds = total % 60
            totalsVar.set("%02d"% (seconds) )
            totalmVar.set(str(int(total/60)))
    updating = False

def updatefromtotal(*args):
    global updating 
    global timedelta
    global total

    if(updating):
        return
    updating = True
    if ( (not totalsVar.get().isnumeric()) or (not totalmVar.get().isnumeric()) or int(totalsVar.get()) > 59 or int(totalsVar.get()) < 0 or int(totalmVar.get()) < 0 or int(totalmVar.get()) + int(totalsVar.get()) == 0):
        seconds = total % 60
        totalsVar.set("%02d"% (seconds))
        totalmVar.set(str(int(total/60)))
    else:
        total = int(totalsVar.get()) + int(totalmVar.get())*60
        if(importf != ""):
            timedelta = int(total/numlines)
            timedeltaVar.set(str(timedelta))
    updating = False

def run():
    exportf = fd.asksaveasfilename(defaultextension = ".srt")
    file = open(importf, "r")
    outfile = open(exportf, "w")
    i = 0
    for x in file:
        if x == "\n":
            continue
        outfile.write(str(i) + "\n")
        time = i * timedelta
        nexttime = (i + 1) * timedelta
        hour = int(time / 3600)
        min = int(time / 60) % 60
        sec = int(time) % 60
        nexthour = int(nexttime / 3600)
        nextmin = int(nexttime / 60) % 60
        nextsec = int(nexttime) % 60
        outfile.write("%02d:%02d:%02d,000 --> %02d:%02d:%02d,000\n" %
                      (hour, min, sec, nexthour, nextmin, nextsec))
        outfile.write(x + "\n")
        i += 1
    exit()
    



window = tk.Tk()
window.title("txt2srt")
window.resizable(False,False)

tk.Label(window, text = "Import from:").grid(row = 0,column = 0)
importfVar = tk.StringVar()
tk.Entry(window, width = 60, textvariable = importfVar, state = "disabled").grid(row = 0, column = 1,columnspan = 5)
tk.Button(window, text = "Select", command = openfile).grid(row = 0, column = 6, columnspan = 3)

tk.Label(window, text = "Number of lines:").grid(row = 1, column = 0, columnspan = 2)
numlinesVar = tk.IntVar()
tk.Entry(window, width = 5, textvariable = numlinesVar, state = "disabled", justify = "right").grid(row = 1, column = 2)

tk.Label(window, text = "Time per line (seconds):").grid(row = 1, column = 3)
timedeltaVar = tk.StringVar()
timedeltaVar.set("5")
timedeltaVar.trace("w",updatefromdelta)
tk.Entry(window, width = 5, validate = "focusout", textvariable = timedeltaVar, justify = "right").grid(row = 1, column = 4)

tk.Label(window, text = "Total time (min:seconds)").grid(row = 1, column = 5)
totalmVar = tk.StringVar()
totalmVar.set("0")
totalmVar.trace("w",updatefromtotal)
tk.Entry(window, width = 5, validate = "focusout", textvariable = totalmVar, justify = "right").grid(row = 1, column = 6)

tk.Label(window, text = ":").grid(row = 1, column = 7)
totalsVar = tk.StringVar()
totalsVar.set("00")
totalsVar.trace("w",updatefromtotal)
tk.Entry(window, width = 2, validate = "focusout", textvariable = totalsVar, justify = "right").grid(row = 1, column = 8)

tk.Button(window, text = "Convert", command = run).grid(row = 2, column = 6, columnspan = 3)
window.mainloop()




# exportf = sys.argv[2]
# importf = sys.argv[1]
# if len(sys.argv) - 1 == 3:
    # maxmins, maxsecs = sys.argv[3].split(":")
    # maxtime = int(maxmins) * 60 + int(maxsecs)
# else:
    # maxtime = 0

# try:
    # file = open(importf, "r")
# except:
    # print("Error: file not found")

# numlines = sum(1 if line != "\n" else 0 for line in open(importf, "r"))

# if maxtime != 0:
    # timedelta = maxtime / numlines
# else:
    # timedelta = 2

# outfile = open(exportf, "w")
# i = 0
# for x in file:
    # if x == "\n":
        # continue
    # outfile.write(str(i) + "\n")
    # time = i * timedelta
    # nexttime = (i + 1) * timedelta
    # hour = int(time / 3600)
    # min = int(time / 60) % 60
    # sec = int(time) % 60
    # nexthour = int(nexttime / 3600)
    # nextmin = int(nexttime / 60) % 60
    # nextsec = int(nexttime) % 60
    # outfile.write("%02d:%02d:%02d,000 --> %02d:%02d:%02d,000\n" %
                  # (hour, min, sec, nexthour, nextmin, nextsec))
    # outfile.write(x + "\n")
    # i += 1