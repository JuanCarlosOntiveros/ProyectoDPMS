#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:52:28 2023

@author: juancarlosmac
"""
import tkinter as tk
from tkinter import *
from tkinter import Label, Tk, Button
from twilio.rest import Client
from PIL import Image, ImageTk

ventana = Tk()
ventana.title("DPM System")
#ventana.geometry('400x700')

#Imagen

img =tk.PhotoImage(file = '/Users/juancarlosmac/AppDPMS/LogoDPMS.png')
#print(img)
#lab = tk.Label(ventana, image = img)
#lab.pack() 

#img.place(x=10,y=30)


#Funcion
def click_boton(valor):
    if (valor == 1):
        account_sid = 'AC15b3c7291e81312ad579f0bf0c44f2aa'
        auth_token = '754545c12094c5a054862153168e3c70'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
          from_='+12563049682',
          body='ALERTA, TU FAMILIAR ESTA SOLICITANDO AYUDA',
          to='+524331030598'
        )

        print(message.sid)

#Botones
boton1 = Button(ventana, image=img, text="Ayuda", width=400, height=700, command=lambda: click_boton(1))


boton1.grid(row=1 , column=1 , padx=5 , pady=5)

ventana.mainloop()
