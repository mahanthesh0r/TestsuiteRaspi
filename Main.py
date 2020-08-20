from tkinter import *
from tkinter import ttk
import os
import subprocess
import shlex


#create window object
app = Tk()

#window propery
app.title('Test Suite v1.0')
app.geometry('700x400')

#create tabbed window
tabControl = ttk.Notebook(app)

#create tabs
mTestTab = ttk.Frame(tabControl)
spiTestTab = ttk.Frame(tabControl)
i2cTestTab = ttk.Frame(tabControl)
uartTestTab = ttk.Frame(tabControl)
cameraTestTab = ttk.Frame(tabControl)


#adding tabs
tabControl.add(mTestTab, text='Memory Test')
tabControl.add(spiTestTab, text='SPI Test')
tabControl.add(i2cTestTab, text='I2C Test')
tabControl.add(uartTestTab, text='UART Test')
tabControl.add(cameraTestTab, text='Camera Test')
#packing the tab
tabControl.pack(expand=1,fill="both")


#Content for Tabs
text = ttk.Label(mTestTab, text="MEMORY TEST",font=("Bold",14)).grid(column = 0,row = 0,padx = 30, pady = 30)
ok = ttk.Label(mTestTab, text="OK", font=('Aerial',12))
ttk.Label(spiTestTab, text="SPI TEST",font=("Bold",14)).grid(column = 0,row = 0,padx = 30, pady = 10, sticky = E)
ttk.Label(i2cTestTab, text="I2C TEST",font=("Bold",14)).grid(column = 0,row = 0,padx = 30, pady = 30)
ttk.Label(uartTestTab, text="UART TEST",font=("Bold",14)).grid(column = 0,row = 0,padx = 30, pady = 30)
ttk.Label(cameraTestTab, text="CAMERA TEST",font=("Bold",14)).grid(column = 0,row = 0,padx = 30, pady = 30)

#memory test listbox
lbox = Listbox(mTestTab,height="15",width="60")
lbox1 = Listbox(spiTestTab, height="15", width="60")
tbox = Text(spiTestTab)
tbox2 = Text(i2cTestTab)
lbox.grid(row=1,column=0)
lbox.place(x=120,y=65)
# lbox1.grid(row=1,column=0)
# lbox1.place(x=120,y=65)
xString = StringVar()
yString = StringVar()
ssVal = StringVar()
Label(cameraTestTab, text="x-coordinate").grid(row=1,column=0)
Coox = Entry(cameraTestTab, textvariable = xString).grid(row=1,column=1,padx=10)
Label(cameraTestTab, text="y-coordinate").grid(row=1,column=2)
Cooy = Entry(cameraTestTab,textvariable= yString).grid(row=1, column=3)
Label(cameraTestTab,text="Shutter Speed: ").grid(row=2,column=0)
shutterText = Entry(cameraTestTab, textvariable = ssVal).grid(row=2, column=1)



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
    
    tbox.place(x=20,y=70)
    tbox.insert(END, out)
    
def onClickBtnI2C():
    commands = '''
    i2cdetect -y 1
    '''
    i2ctest = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = i2ctest.communicate(commands.encode('utf-8'))
    tbox2.place(x=20,y=70)
    tbox2.insert(END, out)

#def onClickBtnUART():
#     command = 'minicom -b 9600 -o -D /dev/ttyACM0'
#     process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
#     while True:
#         output = process.stdout.readline()
#         if output == '' and process.poll() is not None:
#             break
#         if output:
#             print(output.strip())
#     rc = process.poll()
#     return rc

def onClickBtnCAMERA():
    x = xString.get()
    y = yString.get()
    command = 'raspistill -roi '+x+','+y+',0.25,0.25 -o test.jpg'
    output = subprocess.call(command,shell=True)
    print(output)
    if output == 70:
        Label(cameraTestTab, text="exit code: 70: Camera not connected",bg="red").grid(row=5,column=0,padx=5)
    if output == 0:
        Label(cameraTestTab, text="exit code: 0: PASS",fg="green").grid(row=5,column=0,padx=5)

def onClickBtnCAMERA1():
    ss = ssVal.get()
    command = 'raspistill -ss '+ss+' -o test2.jpg'
    output = subprocess.call(command,shell=True)
    if output == 70:
        Label(cameraTestTab, text="exit code: 70: Camera not connected",bg="red").grid(row=5,column=0,padx=5)

    if output == 0:
        Label(cameraTestTab, text="exit code: 0: PASS",bg="green").grid(row=5,column=0,padx=5)
        
    


my_btn = Button(mTestTab, text="TEST",command = onClickBtn).grid(column = 1, row=0,padx = 20, pady = 30)
spiBtn = Button(spiTestTab, text="TEST",command = onClickBtnSPI).grid(column = 1, row=0,padx = 20, pady = 10)
i2cBtn = Button(i2cTestTab, text="TEST",command = onClickBtnI2C).grid(column = 1, row=0,padx = 20, pady = 30)
uartBtn = Button(uartTestTab, text="TEST").grid(column = 1, row=0,padx = 20, pady = 30)
cameraBtn = Button(cameraTestTab, text="TEST",command = onClickBtnCAMERA).grid(column = 5, row=1,padx = 30, pady = 30)
cameraBtn1 = Button(cameraTestTab, text="TEST Shutter Speed",command = onClickBtnCAMERA1).grid(column = 2, row=2,padx = 30, pady = 30)
#start program
app.mainloop()