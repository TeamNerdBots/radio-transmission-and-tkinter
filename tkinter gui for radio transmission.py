import tkinter
import serial
from tkinter import *
from serial import *
from tkinter import font

gui = Tk()

accx_x0, accx_y0, accx_x1, accx_y1 = 500, 150, 500, 150
accy_x0, accy_y0, accy_x1, accy_y1 = 500, 200, 500, 200
accz_x0, accz_y0, accz_x1, accz_y1 = 500, 250, 500, 250

gyrox_x0, gyrox_y0, gyrox_x1, gyrox_y1 = 500, 400, 500, 400
gyroy_x0, gyroy_y0, gyroy_x1, gyroy_y1 = 500, 450, 500, 450
gyroz_x0, gyroz_y0, gyroz_x1, gyroz_y1 = 500, 500, 500, 500


def update():
    line = ser.readline()
    val = str(line).split("")[1].spilt("\\")[0]
    print(val)
    data_list = val.spilt(",")
    try:
        accx= data_list[0]
        accy = data_list[1]
        accz = data_list[2]
        gyrox= data_list[3]
        gyroy= data_list[4]
        gyroz= data_list[5]

        v1.set(accx)
        v2.set(accy)
        v3.set(accz)
        v4.set(gyrox)
        v5.set(gyroy)
        v6.set(gyroz)

        w.coords(accx_rect, accx_x0, accx_y0, accx_x1 + (float(accx)/2.00)* 200, accx_y0 + 20)
        w.coords(accy_rect, accx_x0, accy_y0, accy_x1 + (float(accy)/2.00)* 200, accy_y0 + 20)
        w.coords(accz_rect, accz_x0, accz_y0, accz_x1 + (float(accz)/2.00)* 200, accz_y0 + 20)

        w.coords(gyrox_rect, gyrox_x0, gyrox_y0, gyrox_x1 + (float(gyrox)/300.00)* 200, gyrox_y0 + 20)
        w.coords(gyroy_rect, gyroy_x0, gyroy_y0, gyroy_x1 + (float(gyroy)/300.00)* 200, gyroy_y0 + 20)
        w.coords(gyroz_rect, gyroz_x0, gyroz_y0, gyroz_x1 + (float(gyroz)/300.00)* 200, gyroz_y0 + 20)
        
        if float(accx) < 0: 
            w.itemconfig(accx_rect, fill = 'red')
        else:
            w.itemconfig(accx_rect, fill = '#476042')

        if float(accy) < 0: 
            w.itemconfig(accy_rect, fill = 'red')
        else:
            w.itemconfig(accy_rect, fill = '#476042')

        if float(accz) < 0: 
            w.itemconfig(accz_rect, fill = 'red')
        else:
            w.itemconfig(accz_rect, fill = '#476042')

        if float(gyrox) < 0: 
            w.itemconfig(gyrox_rect, fill = 'red')
        else:
            w.itemconfig(gyrox_rect, fill = '#476042')

        if float(gyroy) < 0: 
            w.itemconfig(gyroy_rect, fill = 'red')
        else:
            w.itemconfig(gyroy_rect, fill = '#476042')

        if float(gyroz) < 0: 
            w.itemconfig(gyroz_rect, fill = 'red')
        else:
            w.itemconfig(gyroz_rect, fill = '#476042')

    except:
        print("data may be lost")


    gui.after(50, update)            
            

canvas_width = 1400
canvas_height = 1200

w = Canvas(gui, bg='skyblue', width=canvas_width, height = canvas_height)
w.pack()

accx_rect = w.create_rectangle(accx_x0,accx_y0,accx_x1,accx_y1,fill="#476042")
accy_rect = w.create_rectangle(accy_x0,accy_y0,accy_x1,accy_y1,fill="#476042")
accz_rect = w.create_rectangle(accz_x0,accz_y0,accz_x1,accz_y1,fill="#476042")

gyrox_rect = w.create_rectangle(gyrox_x0, gyrox_y0, gyrox_x1, gyrox_y1, fill="#476042")
gyroy_rect = w.create_rectangle(gyroy_x0, gyroy_y0, gyroy_x1, gyroy_y1, fill="#476042")
gyroz_rect = w.create_rectangle(gyroz_x0, gyroz_y0, gyroz_x1, gyroz_y1, fill="#476042")

ser= serial.Serial("/dev/ttyAcMo", 19200, timeout=2)
v1= StringVar()
v2= StringVar()
v3= StringVar()
v4= StringVar()
v5= StringVar()
v6= StringVar()



gui.geometry('1000x750')
gui.title('Data')

lA1 = Label(text='A2', bg='skyblue', font='Ariel')
lA1.place (x=250,y=150)

lA2 = Label(text='A2', bg='skyblue', font='Ariel')
lA2.place (x=250,y=200)

lA3 = Label(text='A3', bg='skyblue', font='Ariel')
lA3.place (x=250,y=250)

lG1 = Label(text='G1', bg='skyblue', font='Ariel')
lG1.place (x=250,y=400)

lG2 = Label(text='G2', bg='skyblue', font='Ariel')
lG2.place (x=250,y=450)

lG3 = Label(text='G1', bg='skyblue', font='Ariel')
lG3.place (x=250,y=500)

l1 = Label(text='Accelerometer', bg='skyblue', font='Ariel')

l2 = Label(text='Acceleration X', bg='skyblue', font='Ariel')
l3 = Label(text='Acceleration Y', bg='skyblue', font='Ariel')
l4 = Label(text='Acceleration Z', bg='skyblue', font='Ariel')

l5 = Label(text='Gyroscope', bg='skyblue', font='Ariel')

l6 = Label(text='Position X', bg='skyblue', font='Ariel')
l7 = Label(text='Acceleration', bg='skyblue', font='Ariel')
l8 = Label(text='Acceleration', bg='skyblue', font='Ariel')

l1.place(x=50,y=100)
l2.place(x=100,y=150)
l3.place(x=100,y=200)
l4.place(x=100,y=250)

l5.place(x=50,y=350)
l6.place(x=100,y=400)
l7.place(x=100,y=450)
l8.place(x=100,y=500)

gui.after(100, update)

gui.mainloop()