from tkinter import *#載入函示庫
from time import sleep
import math
import serial
ser = serial.Serial("COM8",115200)
a=1
Q=[]
root = Tk()#建立視窗
#自行定義的函式
e0 = StringVar() #變動文字變數
e1 = StringVar() #變動文字變數
e2 = StringVar() #變動文字變數
e3 = StringVar() #變動文字變數
e4 = StringVar() #變動文字變數
e5 = StringVar() #變動文字變數
cmd = StringVar()

print(ser.readline())
print(ser.readline())
ser.readline()

def out():
    cmd = e0.get() + ' ' + e1.get() + ' ' + e2.get() + ' ' + e3.get() + ' ' + e4.get() + '\n'
    print(cmd)
    ser.write(cmd.encode())
    print(ser.readline())
    print(ser.readline())
    print(ser.readline())
    Q.append(e1.get())
    Label(root,text = Q)
    
#     ser.readline()
    sleep(1)


def enter():
    R=str(e5.get())
    Q.append(e5.get())
    Label(root,text = Q)
def down0():
    t0=float(e0.get())
    t0=t0-0.1
    t0=round(t0,1)
    e0.set(t0)
    print("X座標",":",e0.get())
    out()
def down1():
    t1=float(e1.get())
    t1=t1-0.1
    t1=round(t1,1)
    e1.set(t1)
    print("Y座標",":",e1.get())
    out()
def down2():
    t2=float(e2.get())
    t2=t2-0.1
    t2=round(t2,1)
    e2.set(t2)
    print("Z座標",":",e2.get())
    out()
def down3():
    t3=float(e3.get())
    t3=t3-0.1
    t3=round(t3,1)
    e3.set(t3)
    print("S座標",":",e3.get())
    out()
def down4():
    t4=float(e4.get())
    t4=t4-0.1
    t4=round(t4,1)
    e4.set(t4)
    print("D座標",":",e4.get())
    out()
def up0():
    t0=float(e0.get())
    t0=t0+0.1
    t0=round(t0,1)
    e0.set(t0)
    print("X座標",":",e0.get())
    out()
def up1():
    t1=float(e1.get())
    t1=t1+0.1
    t1=round(t1,1)
    e1.set(t1)
    print("Y座標",":",e1.get())
    out()
def up2():
    t2=float(e2.get())
    t2=t2+0.1
    t2=round(t2,1)
    e2.set(t2)
    print("Z座標",":",e2.get())
    out()
def up3():
    t3=float(e3.get())
    t3=t3+0.1
    t3=round(t3,1)
    e3.set(t3)
    print("S座標",":",e3.get())
    out()
def up4():
    t4=float(e4.get())
    t4=t4+0.1
    t4=round(t4,1)
    e4.set(t4)
    print("D座標",":",e4.get())
    out()
def upone():
    t0=float(e0.get())
    t0=t0+1
    t0=round(t0,1)
    e0.set(t0)
    print("X座標",":",e0.get())
    out()
def upone1():
    t1=float(e1.get())
    t1=t1+1
    t1=round(t1,1)
    e1.set(t1)
    print("X座標",":",e1.get())
    out()
def upone2():
    t2=float(e2.get())
    t2=t2+1
    t2=round(t2,1)
    e2.set(t2)
    print("X座標",":",e2.get())
    out()
def upone3():
    t3=float(e3.get())
    t3=t3+1
    t3=round(t3,1)
    e3.set(t3)
    print("X座標",":",e3.get())
    out()
def upone4():
    t4=float(e4.get())
    t4=t4+1
    t4=round(t4,1)
    e4.set(t4)
    print("X座標",":",e4.get())
    out()
def downone():
    t0=float(e0.get())
    t0=t0-1
    t0=round(t0,1)
    e0.set(t0)
    print("X座標",":",e0.get())
    out()
def downone1():
    t1=float(e1.get())
    t1=t1-1
    t1=round(t1,1)
    e1.set(t1)
    print("X座標",":",e1.get())
    out()
def downone2():
    t2=float(e2.get())
    t2=t2-1
    t2=round(t2,1)
    e2.set(t2)
    print("X座標",":",e2.get())
    out()
def downone3():
    t3=float(e3.get())
    t3=t3-1
    t3=round(t3,1)
    e3.set(t3)
    print("X座標",":",e3.get())
    out()
def downone4():
    t4=float(e4.get())
    t4=t4-1
    t4=round(t4,1)
    e4.set(t4)
    print("X座標",":",e4.get())
    out()
def upten():
    t0=float(e0.get())
    t0=t0+10
    t0=round(t0,1)
    e0.set(t0)
    print("X座標",":",e0.get())
    out()
def upten1():
    t1=float(e1.get())
    t1=t1+10
    t1=round(t1,1)
    e1.set(t1)
    print("X座標",":",e1.get())
    out()
def upten2():
    t2=float(e2.get())
    t2=t2+10
    t2=round(t2,1)
    e2.set(t2)
    print("X座標",":",e2.get())
    out()
def upten3():
    t3=float(e3.get())
    t3=t3+10
    t3=round(t3,1)
    e3.set(t3)
    print("X座標",":",e3.get())
    out()
def upten4():
    t4=float(e4.get())
    t4=t4+10
    t4=round(t4,1)
    e4.set(t4)
    print("X座標",":",e4.get())
    out()
def downten():
    t0=float(e0.get())
    t0=t0-10
    t0=round(t0,1)
    e0.set(t0)
    print("X座標",":",e0.get())
    out()
def downten1():
    t1=float(e1.get())
    t1=t1-10
    t1=round(t1,1)
    e1.set(t1)
    print("X座標",":",e1.get())
    out()
def downten2():
    t2=float(e2.get())
    t2=t2-10
    t2=round(t2,1)
    e2.set(t2)
    print("X座標",":",e2.get())
    out()
def downten3():
    t3=float(e3.get())
    t3=t3-10
    t3=round(t3,1)
    e3.set(t3)
    print("X座標",":",e3.get())
    out()
def downten4():
    t4=float(e4.get())
    t4=t4-10
    t4=round(t4,1)
    e4.set(t4)
    print("X座標",":",e4.get())
    out()
#print (entry.get())

o1=Button(root,text = "+10",command = upten,width=4)
o1.grid(row=0, column=0)

o2=Button(root,text = "+10",command = upten1,width=4)
o2.grid(row=0, column=1)

o3=Button(root,text = "+10",command = upten2,width=4)
o3.grid(row=0, column=2)

o4=Button(root,text = "+10",command = upten3,width=4)
o4.grid(row=0, column=3)

o5=Button(root,text = "+10",command = upten4,width=4)
o5.grid(row=0, column=4)

o6=Button(root,text = "-10",command = downten,width=4)
o6.grid(row=6, column=0)

o7=Button(root,text = "-10",command = downten1,width=4)
o7.grid(row=6, column=1)

o8=Button(root,text = "-10",command = downten2,width=4)
o8.grid(row=6, column=2)

o9=Button(root,text = "-10",command = downten3,width=4)
o9.grid(row=6, column=3)

o10=Button(root,text = "-10",command = downten4,width=4)
o10.grid(row=6, column=4)
#建立一個Button按下後會呼叫validateText函式
a1=Button(root,text = "+1",command = upone,width=4)
a1.grid(row=1, column=0)

a2=Button(root,text = "+1",command = upone1,width=4)
a2.grid(row=1, column=1)

a3=Button(root,text = "+1",command = upone2,width=4)
a3.grid(row=1, column=2)

a4=Button(root,text = "+1",command = upone3,width=4)
a4.grid(row=1, column=3)

a5=Button(root,text = "+1",command = upone4,width=4)
a5.grid(row=1, column=4)

a6=Button(root,text = "-1",command = downone,width=4)
a6.grid(row=5, column=0)

a7=Button(root,text = "-1",command = downone1,width=4)
a7.grid(row=5, column=1)

a8=Button(root,text = "-1",command = downone2,width=4)
a8.grid(row=5, column=2)

a9=Button(root,text = "-1",command = downone3,width=4)
a9.grid(row=5, column=3)

a10=Button(root,text = "-1",command = downone4,width=4)
a10.grid(row=5, column=4)

b1=Button(root,text = "+0.1",command = up0)
b1.grid(row=2, column=0)

b2=Button(root,text = "+0.1",command = up1)
b2.grid(row=2, column=1)

b3=Button(root,text = "+0.1",command = up2)
b3.grid(row=2, column=2)

b4=Button(root,text = "+0.1",command = up3)
b4.grid(row=2, column=3)

b5=Button(root,text = "+0.1",command = up4)
b5.grid(row=2, column=4)

b6=Button(root,text = "-0.1",command = down0,width=4)
b6.grid(row=4, column=0)

b7=Button(root,text = "-0.1",command = down1,width=4)
b7.grid(row=4, column=1)

b8=Button(root,text = "-0.1",command = down2,width=4)
b8.grid(row=4, column=2)

b9=Button(root,text = "-0.1",command = down3,width=4)
b9.grid(row=4, column=3)

b10=Button(root,text = "-0.1",command = down4,width=4)
b10.grid(row=4, column=4)

c1=Button(root,text = "確定",command = enter,width=4)
c1.grid(row=5, column=10)

entry1 = Entry(root,textvariable = e0,width=5)
e0.set(0.0)
entry1.grid(row=3, column=0)

entry2 = Entry(root,textvariable = e1,width=5)
e1.set(0.0)
entry2.grid(row=3, column=1)

entry3 = Entry(root,textvariable = e2,width=5)
e2.set(0.0)
entry3.grid(row=3, column=2)

entry4 = Entry(root,textvariable = e3,width=5)
e3.set(0.0)
entry4.grid(row=3, column=3)

entry5 = Entry(root,textvariable = e4,width=5)
e4.set(0.0)
entry5.grid(row=3, column=4)

entry6 = Entry(root,textvariable = e5,width=15)
e5.set("請輸入")
entry6.grid(row=5, column=5)

label=Label(root,text = "",bg = "gray",width=20,height=9,wraplength = 60)
label.grid(row=0, column=5,columnspan=8,rowspan=5)

root.mainloop()
