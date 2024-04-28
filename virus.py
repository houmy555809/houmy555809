import tkinter
import os
import time
import pathos.multiprocessing as mp
import multiprocessing as sysmp
from selenium import webdriver
import random
import webbrowser
cur_windows=[]
cur_windows_id=[]
closed_cnt=0
def do_closed(window):
    global closed_cnt
    closed_cnt+=1
    window.destroy()
def do_mainloop(winid):
    global cur_windows
    #print(winid)
    cur_windows[winid].mainloop()
def window(x,y):
    global cur_windows
    window=tkinter.Tk()
    window.title("233")
    window.geometry("50x50+{}+{}".format(x,y))
    window.attributes("-topmost",True)
    window.protocol("WM_DELETE_WINDOW",lambda window=window:do_closed(window))
    tkinter.Label(window,text="233").pack()
    cur_windows.append(window)
    cur_windows_id.append(len(cur_windows_id))
def render_windows():
    global cur_windows_id
    pool=mp.ProcessPool()
    for i in cur_windows_id:
        pool.apipe(do_mainloop,i)
HORIZONTAL=0
VERTICAL=1
def windowline(x,y,length,typ):
    if typ==HORIZONTAL:
        for i in range(length//100+1):
            window(x+i*100,y)
    else:
        for i in range(length//40+1):
            window(x,y+i*40)
def do233process():
    print("It's not over yet.")
    time.sleep(1)
    #2
    windowline(0,0,200,HORIZONTAL)
    windowline(200,0,200,VERTICAL)
    windowline(0,200,200,HORIZONTAL)
    windowline(0,200,200,VERTICAL)
    windowline(0,400,200,HORIZONTAL)
    #3
    windowline(500,0,200,HORIZONTAL)
    windowline(700,0,200,VERTICAL)
    windowline(500,200,200,HORIZONTAL)
    windowline(700,200,200,VERTICAL)
    windowline(500,400,200,HORIZONTAL)
    #3
    windowline(1000,0,200,HORIZONTAL)
    windowline(1200,0,200,VERTICAL)
    windowline(1000,200,200,HORIZONTAL)
    windowline(1200,200,200,VERTICAL)
    windowline(1000,400,200,HORIZONTAL)
    print("The interesting thing begins... Now!!!")
    render_windows()
def end233process():
    global cur_windows,cur_windows_id
    for i in cur_windows:
        try:
            i.destroy()
        except:
            pass
    cur_windows=[]
    cur_windows_id=[]
def secondaryprocess():
    global cur_windows,cur_windows_id,closed_cnt
    while closed_cnt<len(cur_windows):
        for i in cur_windows:
            try:
                i.update()
            except:
                pass
        time.sleep(0.1)
    print("Well done!")
    time.sleep(1)
    print("You closed all of them! This is incredible!")
    time.sleep(1)
    print("By the way, how do you fell now?")
    time.sleep(1)
    print("How about trying again?")
    time.sleep(1)
    closed_cnt=0
    cur_windows=[]
    cur_windows_id=[]
def gen233window():
    root=tkinter.Tk()
    root.attributes("-topmost",True)
    root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
    root.resizable(False,False)
    root.attributes("-topmost",False)
    root.overrideredirect(True)
    def work():
        tkinter.Label(text="233",font=("Consolas",30)).place(x=random.randint(0,root.winfo_screenwidth()),y=random.randint(0,root.winfo_screenheight()))
        root.after(250,work)
    work()
    root.mainloop()
def main():
    input("Runtime Error. Please press enter to terminate this program. (Code: 0xfffffffe)")
    for i in range(1000):
        print(chr(random.randint(257,32767)),end="")
    print()
    print(2,end="")
    for i in range(50):
        time.sleep(0.05)
        print(3,end="")
    print()
    do233process()
    print("Close all the windows. Have fun!")
    secondaryprocess()
    print("Just kidding.")
    time.sleep(1)
    print("But let's do something bigger.")
    time.sleep(1)
    print("By the way, you can close this window to end this at any time.")
    time.sleep(1)
    gen233window()
    #driver=webdriver.Chrome()
    #driver.get("houmy555809.github.io/233page")
    #driver.maximize_window()
    
    #webbrowser.open_new("houmy555809.github.io/233page")
main()
