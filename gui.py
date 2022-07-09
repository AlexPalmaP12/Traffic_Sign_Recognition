"""
Created on Tue Jun 28 02:31:41 2022

@author: benke
"""


import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
from keras.models import load_model

# Load your model
model = load_model('./training/TSR.h5') # Path to your model

# Diccionaria de Datos
classes = { 1:'Limite de velocidad (20km/h)',
            2:'Limite de velocidad  (30km/h)', 
            3:'Limite de velocidad  (50km/h)', 
            4:'Limite de velocidad  (60km/h)', 
            5:'Limite de velocidad  (70km/h)', 
            6:'Limite de velocidad (80km/h)', 
            7:'Fin del límite de velocidad (80km/h)', 
            8:'Limite de velocidad (100km/h)', 
            9:'Limite de velocidad (120km/h)', 
            10:'No pasar', 
            11:'Peso mayor a 3.5 toneladas prohibido', 
            12:'Derecho de paso en la intersección', 
            13:'Camino prioritario', 
            14:'Ceda el paso', 
            15:'Stop', 
            16:'Sin vehiculos', 
            17:'Peso mayor a 3.5 toneladas prohibido', 
            18:'Prohibida la entrada', 
            19:'Precaucion', 
            20:'Curva a la izquierda peligrosa', 
            21:'Curva a la derecha peligrosa', 
            22:'Doble curva', 
            23:'Camino lleno de baches', 
            24:'Camino resbaloso', 
            25:'El camino se estrecha a la derecha', 
            26:'Trabajo en la carretera', 
            27:'Señales de tráfico', 
            28:'Peatones', 
            29:'Niños cruzando', 
            30:'Cruce de bicicletas', 
            31:'Cuidado con el hielo/la nieve',
            32:'Cruce de animales salvajes', 
            33:'Velocidad final + límites de paso', 
            34:'Adelante, gire a la derecha', 
            35:'Adelante, gire a la izquierda', 
            36:'Solo adelante', 
            37:'Seguir recto o a la derecha',
            38:'Seguir recto o a la izquierda',
            39:'Manténgase a la derecha',
            40:'Manténgase a la izquierda',
            41:'Rotonda obligatoria',
            42:'Fin de no pasar',
            43:'Termina sin vehículos de paso > 3,5 toneladas' }


# Initialise GUI
top=tk.Tk()
# Window dimensions (800x600)
top.geometry('800x600')
# Window title
top.title('Identificador de señales de transito')
# Window background color
top.configure(background='#CDCDCD')
# Window label
label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
# Sign image
sign_image = Label(top)


def classify(file_path):
    global label_packed
    # Abrir imagen
    image = Image.open(file_path)
    # Modificar tamaño de la imagen
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = model.predict_classes([image])[0]
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#011638', text=sign) 
    
def show_classify_button(file_path):
    classify_b=Button(top,text="Identificar imagen",command=lambda: classify(file_path),padx=10,pady=15)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)
    
# Funcion para la carga de imagen
def upload_image():
    try:
       
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
    
# Boton de subir
upload=Button(top,text="Carga una imagen",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
# Window title text
heading = Label(top, text="Conoce tus señales de trafico",pady=20, font=('arial',20,'bold'))
# Window colors
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()