from tkinter import *
import random
import time

tk = Tk()
tk.title("Projeto simples, apenas com o proposito de aprender mais sobre a tkinter")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=500,height=500,bd=0,highlightthickness=0)
canvas.configure(bg="Purple")
canvas.pack()
tk.update()

class Ball:
    def __init__(self,canvas,defesa,color):
        self.canvas = canvas
        self.defesa = defesa
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        start = [-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_Bottom = False


    def hit_defesa(self,pos):
        defesa_pos = self.canvas.coords(self.defesa.id)
        if pos[2] >= defesa_pos[0] and pos[0] <= defesa_pos[2]:
            if pos[3] >= defesa_pos[1] and pos[3] <= defesa_pos[3]:
                return True
        return False


    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        print(pos)
        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3
            self.hit_Bottom = True
            canvas.create_text(245,100,text="GAME OVER !",font=('arial',16))

        if pos[0] <= 0:
            self.x = 3

        if pos[2] >= self.canvas_width:
            self.x = -3

        if self.hit_defesa(pos) == True:
            self.y =  -3

class Defesa:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill = color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        '''
            Observar que as definiçoes das teclas de comando parecem mudar
            de acordo com o sistema operacional, deve ter uma forma mais elegante de
            prever isso
        '''
        self.canvas.bind_all("<Left>",self.turn_left)
        self.canvas.bind_all("<Right>",self.turn_right)

    def drawdefesa(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0

        if pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self,evt):
        self.x = -2

    def turn_right(self,evt):
        self.x = 2

defesa = Defesa(canvas,'black')
ball = Ball(canvas,defesa,'yellow')

while 1:
    if ball.hit_Bottom == False:
        ball.draw()
        defesa.drawdefesa()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
