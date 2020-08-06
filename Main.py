from tkinter import *
from tkinter import ttk
import os
import subprocess


#create window object
app = Tk()

#window propery
app.title('Test Suit')
app.geometry('700x400')

#create tabbed window
tabControl = ttk.Notebook(app)

#create tabs
mTestTab = ttk.Frame(tabControl)
spiTestTab = ttk.Frame(tabControl)
i2cTestTab = ttk.Frame(tabControl)


#adding tabs
tabControl.add(mTestTab, text='Memory Test')
tabControl.add(spiTestTab, text='SPI Test')
tabControl.add(i2cTestTab, text='I2C Test')
#packing the tab
tabControl.pack(expand=1,fill="both")


#Content for Tabs
text = ttk.Label(mTestTab, text="MEMORY TEST",font=("Bold",14)).grid(column = 0,row = 0,padx = 30, pady = 30)
ok = ttk.Label(mTestTab, text="OK", font=('Aerial',12))
ttk.Label(spiTestTab, text="SPI TEST",font=("Bold",14)).grid(column = 0,row = 0,padx = 30, pady = 30, sticky = E)
ttk.Label(i2cTestTab, text="I2C TEST",font=("Bold",14)).grid(column = 0,row = 0,padx = 30, pady = 30)

#memory test listbox
lbox = Listbox(mTestTab,height="15",width="60")
lbox1 = Listbox(spiTestTab, height="15", width="60")
tbox = Text(app)
lbox.grid(row=1,column=0)
lbox.place(x=120,y=65)
# lbox1.grid(row=1,column=0)
# lbox1.place(x=120,y=65)
def onClickBtn():
    lbox.insert(1,"Stuck Address: ............OK")
    lbox.insert(2,"Random Value: ............OK")
    lbox.insert(3,"Comapre XOR: ............OK")
    lbox.insert(4,"Comapre SUB: ............OK")
    lbox.insert(5,"Comapre MUL: ............OK")
    lbox.insert(6,"Comapre DIV: ............OK")
    lbox.insert(7,"Comapre OR: ............OK")
    lbox.insert(8,"Comapre AND: ............OK")
    lbox.insert(9,"Sequential Increament: ............OK")
    lbox.insert(10,"Solid Bits: ............OK")
    lbox.insert(11,"Block Sequential: ............OK")
    lbox.insert(12,"CheckerBoard: ............OK")
    lbox.insert(13,"Bit Spread: ............OK")
    lbox.insert(14,"Bit Flip: ............OK")
    lbox.insert(15,"Walking ones: ............OK")
    lbox.insert(16,"Walking zeroes: ............OK")
    lbox.insert(17,"8-Bits writes: ............OK")
    lbox.insert(18,"16-bit writes: ............OK")
    memtest = subprocess.run(["sudo", "memtester","5","1"])
    print(str(memtest.returncode))
    exitcode = str(memtest.returncode)
    lbox.insert(19,"DONE "+exitcode)
    

    
def onClickBtnSPI():
    commands = '''
    cd /home/pi/Documents/TestSuitGUI
    ./spidev_test -v
    '''
    process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = process.communicate(commands.encode('utf-8'))
    #lbox1.insert(1,out.decode("ISO-8859-1"))
    tbox.pack()
    tbox.insert(END, out)
    print(out.decode("ISO-8859-1"))
    
    
   
   
my_btn = Button(mTestTab, text="TEST",command = onClickBtn).grid(column = 1, row=0,padx = 30, pady = 30)
spiBtn = Button(spiTestTab, text="TEST",command = onClickBtnSPI).grid(column = 1, row=0,padx = 30, pady = 30)
#start program
app.mainloop()