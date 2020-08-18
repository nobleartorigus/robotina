import tkinter as tk
from tkinter import ttk
import time
import numpy as np
import utils

class GameBoard(tk.Frame):

    def __init__(self, parent, rows=20, columns=30, size=38, color1="#4995D8", color2="blue"):
     
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}
        self.basura_items = {}
        self.comida_items = {}
        self.bateria_items = {}
        self.wc_items = {}
        self.pared_items = {}
        self.cama_item = {}
        self.initx = 0
        self.inity = 0
        self.prior = 'Basura'
        self.coords = [0, 0]
    

        self.timecounter = 100
        self.wccounter = 0
        self.Robotina = tk.PhotoImage(file=robotina)
        self.Basura = tk.PhotoImage(file=basura)
        self.Pared = tk.PhotoImage(file=pared)
        self.Cama = tk.PhotoImage(file=cama)
        self.Comida = tk.PhotoImage(file=comida)
        self.WC = tk.PhotoImage(file=wc)
        self.Bateria = tk.PhotoImage(file=bateria)

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width*1.3, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)
        self.canvas.bind("<Configure>", self.refresh)

        self.addpiece("Robotina", self.Robotina, 0,0)

        #Basura
        self.addpiece("Basura1", self.Basura, 5,7)
        self.addpiece("Basura2", self.Basura, 2,7)
        self.addpiece("Basura3", self.Basura, 4,4)
        self.addpiece("Basura4", self.Basura, 2,0)
        self.addpiece("Basura5", self.Basura, 14,21)
        self.addpiece("Basura6", self.Basura, 13,15)
        self.addpiece("Basura7", self.Basura, 9,7)
        self.addpiece("Basura8", self.Basura, 17,23)
        self.addpiece("Basura9", self.Basura, 19, 25)
        self.addpiece("Basura10", self.Basura, 7, 22)

        #Comida
        self.addpiece("Comida1", self.Comida, 6, 8)
        self.addpiece("Comida2", self.Comida, 3, 7)
        self.addpiece("Comida3", self.Comida, 4, 5)
        self.addpiece("Comida4", self.Comida, 9, 6)
        self.addpiece("Comida5", self.Comida, 15, 21)
        self.addpiece("Comida6", self.Comida, 10, 8)
        self.addpiece("Comida7", self.Comida, 9, 20)
        self.addpiece("Comida8", self.Comida, 3, 23)
        self.addpiece("Comida9", self.Comida, 5, 18)
        self.addpiece("Comida10", self.Comida, 17, 10)

        #WC 
        self.addpiece("WC1", self.WC, 9, 1)
        self.addpiece("WC2", self.WC, 10, 28)
        self.addpiece("WC3", self.WC, 12, 14)
        self.addpiece("WC4", self.WC, 17, 15)

        #Baterias 
        self.addpiece("Bateria1", self.Bateria, 13, 2)
        self.addpiece("Bateria2", self.Bateria, 2, 14)
        self.addpiece("Bateria3", self.Bateria, 9, 14)
        self.addpiece("Bateria4", self.Bateria, 15, 13)
        self.addpiece("Bateria5", self.Bateria, 8, 7)
        self.addpiece("Bateria6", self.Bateria, 3, 28)
    

        # #Paredes
        # self.addpiece("Pared1", self.Pared, 15, 3)
        # self.addpiece("Pared2", self.Pared, 16, 3)
        # self.addpiece("Pared3", self.Pared, 11, 6)
        # self.addpiece("Pared4", self.Pared, 12, 6)
        # self.addpiece("Pared5", self.Pared, 9, 8)
        # self.addpiece("Pared6", self.Pared, 9, 9)
        # self.addpiece("Pared7", self.Pared, 6, 10)
        # self.addpiece("Pared8", self.Pared, 6, 11)
        # self.addpiece("Pared9", self.Pared, 6, 15)
        # self.addpiece("Pared10", self.Pared, 5, 15)

        #Cama 
        self.addpiece("Cama", self.Cama, 16, 27)

        #Inicio
        self.boton=ttk.Button(self.canvas, text="mover robotina", command= self.eval)
        self.boton.place(x=1250,y=325,width=100,height=50)
        self.label1 = tk.Label(self.canvas, text= 'Basura = -5')
        self.label1.place(x=1150,y= 450, width=100, height=50)
        self.label2 = tk.Label(self.canvas, text= 'Comida = -3')
        self.label2.place(x=1250,y= 450, width=100, height=50)
        self.label3 = tk.Label(self.canvas, text= 'Bateria = +50')
        self.label3.place(x=1350,y= 450, width=100, height=50)
        self.label4 = tk.Label(self.canvas, text= 'WC = -3')
        self.label4.place(x=1150,y= 500, width=100, height=50)
        self.label5 = tk.Label(self.canvas, text= 'Cama = Bateria completa')
        self.label5.place(x=1250,y= 500, width=200, height=50)
     

    def addpiece(self, name, image, row=0, column=0):
        self.canvas.create_image(0,0, image=image, tags=(name), anchor="c")
        self.placepiece(name, row, column)
        if (name[0:-1] == 'Basura') or (name[0:-2] == 'Basura') :
            self.basura_items.update({name:(row, column)})
        elif (name[0:-1] == 'Comida') or (name[0:-2] == 'Comida') :
            self.comida_items.update({name:(row, column)})
        elif (name[0:-1] == 'Bateria'):
            self.bateria_items.update({name:(row, column)})
        elif (name[0:-1] == 'WC'):
            self.wc_items.update({name:(row, column)})
        elif (name[0:-1] == 'Pared'):
            self.pared_items.update({name:(row, column)})
        elif (name == 'Cama'):
            self.cama_item.update({name:(row, column)})

    def placepiece(self, name, row, column):
        if row or column < 8:
            self.pieces[name] = (row, column)
            x0 = (column * self.size) + int(self.size/2)
            y0 = (row * self.size) + int(self.size/2)
            self.canvas.coords(name, x0, y0)

    def move_robotina(self, row, column):
        if row or column < 8:
            self.pieces["Robotina"] = (row, column)
            x0 = (column * self.size) + int(self.size/2)
            y0 = (row * self.size) + int(self.size/2)
            self.canvas.coords("Robotina", x0, y0)

        
    def rerender(self, y, x):
        self.move_robotina(y, x)
        self.canvas.after(100, self.eval) 
    
    def eval(self):
        coords_priority, key = self.prioritize(self.prior)
        self.timecounter -= 1
        time.sleep(0.5)
        self.coords = [self.inity, self.initx]

        if self.timecounter > 25:
            if self.wccounter != 40:
                if self.timecounter > 25 and self.timecounter < 60:
                    self.prior = 'Comida'
                elif self.timecounter > 60:
                    self.prior = 'Basura'
                self.wccounter += 1
            else:
                self.prior = 'WC'
        else:
            self.prior = 'Bateria'

        if self.coords[0] < coords_priority[0]:
            self.inity += 1
        elif self.coords[0] > coords_priority[0]:
            self.inity -= 1
        elif self.coords[1] < coords_priority[1]:
            self.initx += 1
        elif self.coords[1] > coords_priority[1]:
            self.initx -= 1
        # FUNCION PARA BORRAR ELEMENTOS
        if self.coords == coords_priority:
            self.delete_task(key)

        self.printBattery(self.timecounter)
        self.rerender(self.inity, self.initx)


    
    def prioritize(self, prior):
 
        if self.prior != 'WC':
            if self.prior == 'Basura':
                list_to_search = list(self.basura_items.values())
                key_items = self.basura_items
            elif self.prior == 'Comida':
                list_to_search = list(self.comida_items.values())
                if len(list_to_search) == 0:
                    list_to_search = list(self.basura_items.values())
                    key_items = self.basura_items
                else:
                    key_items = self.comida_items

            elif self.prior == 'Bateria':
                list_to_search = list(self.bateria_items.values())
                if len(list_to_search) == 0:
                    list_to_search = list(self.cama_item.values())
                    key_items = self.cama_item
                    if len(list_to_search) == 0:
                        list_to_search = list(self.basura_items.values())
                        key_items = self.basura_items
                    else:
                        key_items = self.cama_item
                else:
                    key_items = self.bateria_items
        else:
            list_to_search = list(self.wc_items.values())
            if len(list_to_search) == 0:
                self.wccounter = 0
                list_to_search = list(self.basura_items.values())
                key_items = self.basura_items
            else:
                key_items = self.wc_items
        
        sorted_list = sorted(list_to_search, key=lambda x: x[1])
        x, y = sorted_list[0]
        key = utils.get_key(key_items, sorted_list[0])
        return([x, y], key)
        
    
    def delete_task(self, key):
        if key[0:-1] == 'Basura' or key[0:-2] == 'Basura':
            self.timecounter -= 3 
            time.sleep(1)
            remove_list = self.basura_items
        elif key[0:-1] == 'Comida' or key[0:-2] == 'Comida':
            self.timecounter -= 5 
            time.sleep(2)
            remove_list = self.comida_items
        elif key[0:-1] == 'Bateria' or key[0:-2] == 'Bateria':
            self.timecounter += 50
            remove_list = self.bateria_items
            time.sleep(5)
        elif key[0:-1] == 'WC':
            self.timecounter -= 3 
            remove_list = self.wc_items
            time.sleep(3)
            self.wccounter = 0
        elif key == 'Cama':
            self.timecounter = 100 
            time.sleep(7)
            remove_list = self.cama_item
        self.canvas.delete(key)
        remove_list = utils.removekey(remove_list, key)

    def printBattery(self, time_counter):
        self.label = tk.Label(self.canvas, text= str(time_counter))
        self.label.place(x=1250,y= 550, width=100, height=50)
    

    def refresh(self, event):
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")


robotina = './img/robotina.png'
basura = './img/basura.png'
pared = './img/pared.png'
cama = './img/cama.png'
comida = './img/comida.png'
wc = './img/wc.png'
bateria = './img/bateria.png'



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Robotina")
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
   
    root.mainloop()